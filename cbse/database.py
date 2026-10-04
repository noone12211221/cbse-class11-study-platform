import sqlite3
import hashlib

DB_NAME = "study_app.db"


def _hash_password(password):
    """Hashes a password with SHA-256 before it ever touches the database."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def init_db():
    """Initializes the SQLite database tables."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # User Profile & Stats Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            total_xp INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0,
            total_attempted INTEGER DEFAULT 0,
            total_correct INTEGER DEFAULT 0
        )
    ''')
    
    # Chapter-level Performance Breakdown Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS chapter_stats (
            username TEXT,
            subject TEXT,
            chapter TEXT,
            attempted INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0,
            PRIMARY KEY (username, subject, chapter)
        )
    ''')
    
    conn.commit()
    conn.close()

def register_user(username, password):
    """Registers a new user in the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, _hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    """Verifies user login credentials."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = c.fetchone()
    conn.close()
    return row is not None and row[0] == _hash_password(password)

def update_user_stats(username, xp_gained, is_correct, subject, chapter):
    """Updates overall XP, streak, and chapter-specific statistics."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Fetch current user data
    c.execute('SELECT streak, total_xp, total_attempted, total_correct FROM users WHERE username = ?', (username,))
    res = c.fetchone()
    if not res:
        conn.close()
        return
        
    current_streak, total_xp, total_attempted, total_correct = res
    
    # Calculate updated overall values
    new_streak = (current_streak + 1) if is_correct else 0
    new_xp = total_xp + (xp_gained if is_correct else 0)
    new_attempted = total_attempted + 1
    new_correct = total_correct + (1 if is_correct else 0)
    
    c.execute('''
        UPDATE users 
        SET total_xp = ?, streak = ?, total_attempted = ?, total_correct = ? 
        WHERE username = ?
    ''', (new_xp, new_streak, new_attempted, new_correct, username))
    
    # Upsert chapter-specific performance
    c.execute('''
        INSERT INTO chapter_stats (username, subject, chapter, attempted, correct)
        VALUES (?, ?, ?, 1, ?)
        ON CONFLICT(username, subject, chapter) DO UPDATE SET
            attempted = attempted + 1,
            correct = correct + ?
    ''', (username, subject, chapter, 1 if is_correct else 0, 1 if is_correct else 0))
    
    conn.commit()
    conn.close()

def get_leaderboard():
    """Retrieves top 10 users ranked by total XP."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT username, total_xp, streak, total_attempted, total_correct
        FROM users 
        ORDER BY total_xp DESC 
        LIMIT 10
    ''')
    rows = c.fetchall()
    conn.close()
    
    return [
        {
            "Username": r[0],
            "Total XP": r[1],
            "Current Streak": r[2],
            "Attempted": r[3],
            "Correct": r[4]
        }
        for r in rows
    ]

def get_user_chapter_analytics(username):
    """Retrieves chapter accuracy breakdown for a specific user."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT subject, chapter, attempted, correct
        FROM chapter_stats
        WHERE username = ?
    ''', (username,))
    rows = c.fetchall()
    conn.close()
    
    analytics = []
    for r in rows:
        subject, chapter, attempted, correct = r
        accuracy = (correct / attempted * 100) if attempted > 0 else 0
        analytics.append({
            "subject": subject,
            "chapter": chapter,
            "attempted": attempted,
            "correct": correct,
            "accuracy": round(accuracy, 1)
        })
    return analytics