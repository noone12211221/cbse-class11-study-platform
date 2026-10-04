MATHS_QUESTIONS = {   'Chapter 1: Sets': [   {   'question': 'Which of the following collection of elements '
                                           'represents a well-defined set?',
                               'options': [   'The collection of all difficult problems in a '
                                              'textbook',
                                              'The collection of all intelligent students in a '
                                              'class',
                                              'The collection of all prime numbers less than 20',
                                              'The collection of good cricket players in India'],
                               'answer': 'c',
                               'Difficulty': 'Easy',
                               'Explanation': 'A set is a well-defined collection of objects. The '
                                              "condition 'prime numbers less than 20' is definite "
                                              'and non-subjective.'},
                           {   'question': 'If a set $A$ has $n$ elements, then the total number '
                                           'of subsets in the power set $P(A)$ is:',
                               'options': ['n', '2^n', '2^(n-1)', 'n^2'],
                               'answer': 'b',
                               'Difficulty': 'Easy',
                               'Explanation': 'The power set of $A$ contains all possible subsets '
                                              'of $A$. If $|A| = n$, the total number of subsets '
                                              'is $2^n$.'},
                           {   'question': 'Let $A = \\{1, 2, 3\\}$ and $B = \\{3, 4, 5\\}$. What '
                                           'is $A \\cap B$?',
                               'options': [   '\\{1, 2, 3, 4, 5\\}',
                                              '\\{3\\}',
                                              '\\{1, 2\\}',
                                              '\\{4, 5\\}'],
                               'answer': 'b',
                               'Difficulty': 'Easy',
                               'Explanation': 'The intersection $A \\cap B$ contains elements '
                                              'common to both set $A$ and set $B$, which is '
                                              '$\\{3\\}$.'},
                           {   'question': 'If $A$ and $B$ are two disjoint sets, then $A \\cap B$ '
                                           'is equal to:',
                               'options': ['A', 'B', '\\emptyset', 'U'],
                               'answer': 'c',
                               'Difficulty': 'Easy',
                               'Explanation': 'Disjoint sets have no elements in common, so their '
                                              'intersection is the empty set $\\emptyset$.'},
                           {   'question': 'For any two sets $A$ and $B$, $A - B$ is equal to:',
                               'options': ["A \\cap B'", "A' \\cap B", "A \\cup B'", "A' \\cup B"],
                               'answer': 'a',
                               'Difficulty': 'Moderate',
                               'Explanation': 'The set difference $A - B$ consists of elements in '
                                              '$A$ that are not in $B$, which equals $A \\cap '
                                              "B'$."},
                           {   'question': 'If $n(A) = 15$, $n(B) = 20$, and $n(A \\cup B) = 30$, '
                                           'find $n(A \\cap B)$.',
                               'options': ['5', '10', '15', '0'],
                               'answer': 'a',
                               'Difficulty': 'Moderate',
                               'Explanation': 'By the inclusion-exclusion principle, $n(A \\cup B) '
                                              '= n(A) + n(B) - n(A \\cap B) \\implies 30 = 15 + 20 '
                                              '- n(A \\cap B) \\implies n(A \\cap B) = 5$.'},
                           {   'question': 'The set of all real numbers $x$ satisfying $x^2 + 1 = '
                                           '0$ is:',
                               'options': ['\\{1, -1\\}', '\\{0\\}', '\\emptyset', '\\{1\\}'],
                               'answer': 'c',
                               'Difficulty': 'Easy',
                               'Explanation': 'No real number squared gives $-1$, so the set of '
                                              'real solutions is empty (null set).'},
                           {   'question': "According to De Morgan's Law, $(A \\cup B)'$ is equal "
                                           'to:',
                               'options': ["A' \\cup B'", "A' \\cap B'", 'A \\cap B', "A' - B'"],
                               'answer': 'b',
                               'Difficulty': 'Moderate',
                               'Explanation': "De Morgan's first law states that the complement of "
                                              'the union of two sets is the intersection of their '
                                              "complements: $(A \\cup B)' = A' \\cap B'$."},
                           {   'question': 'If $A \\subset B$, then $A \\cup B$ is equal to:',
                               'options': ['A', 'B', '\\emptyset', 'A \\cap B'],
                               'answer': 'b',
                               'Difficulty': 'Easy',
                               'Explanation': 'If every element of $A$ is in $B$, then taking the '
                                              'union of $A$ and $B$ simply yields $B$.'},
                           {   'question': 'The interval represented by $\\{x \\in \\mathbb{R} : '
                                           '-3 < x \\le 5\\}$ is:',
                               'options': ['[-3, 5]', '(-3, 5)', '(-3, 5]', '[-3, 5)'],
                               'answer': 'c',
                               'Difficulty': 'Easy',
                               'Explanation': "Strict inequality at $-3$ uses a parenthesis '(' "
                                              'and non-strict inequality at $5$ uses a square '
                                              "bracket ']'."}],
    'Chapter 2: Relations and Functions': [   {   'question': 'If set $A$ has 3 elements and set '
                                                              '$B$ has 2 elements, how many total '
                                                              'relations can be defined from $A$ '
                                                              'to $B$?',
                                                  'options': ['6', '8', '32', '64'],
                                                  'answer': 'd',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'Number of elements in $A \\times '
                                                                 'B = 3 \\times 2 = 6$. The total '
                                                                 'number of relations is $2^6 = '
                                                                 '64$.'},
                                              {   'question': 'What is the domain of the '
                                                              'real-valued function $f(x) = '
                                                              '\\sqrt{x - 3}$?',
                                                  'options': [   '(3, \\infty)',
                                                                 '[3, \\infty)',
                                                                 '(-\\infty, 3]',
                                                                 '(\\mathbb{R})'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'For $\\sqrt{x - 3}$ to be '
                                                                 'defined in real numbers, $x - 3 '
                                                                 '\\ge 0 \\implies x \\ge 3$, '
                                                                 'giving domain $[3, \\infty)$.'},
                                              {   'question': 'The range of the signum function '
                                                              '$f(x) = \\text{sgn}(x)$ is:',
                                                  'options': [   '\\{-1, 0, 1\\}',
                                                                 '[-1, 1]',
                                                                 '(0, \\infty)',
                                                                 '\\mathbb{R}'],
                                                  'answer': 'a',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'The signum function takes only '
                                                                 'three output values: $-1$ for '
                                                                 'negative inputs, $0$ for zero, '
                                                                 'and $1$ for positive inputs.'},
                                              {   'question': 'If $(x + 1, y - 2) = (3, 1)$, then '
                                                              'the values of $x$ and $y$ are '
                                                              'respectively:',
                                                  'options': ['2, 3', '3, 2', '1, 3', '2, 1'],
                                                  'answer': 'a',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Equating corresponding '
                                                                 'components: $x + 1 = 3 \\implies '
                                                                 'x = 2$, and $y - 2 = 1 \\implies '
                                                                 'y = 3$.'},
                                              {   'question': 'What is the domain of the modulus '
                                                              'function $f(x) = |x|$?',
                                                  'options': [   '[0, \\infty)',
                                                                 '(-\\infty, 0]',
                                                                 '\\mathbb{R}',
                                                                 '(0, \\infty)'],
                                                  'answer': 'c',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'The absolute value function '
                                                                 '$|x|$ is defined for all real '
                                                                 'numbers $\\mathbb{R}$.'},
                                              {   'question': 'What is the range of the function '
                                                              '$f(x) = x^2 + 2$ for $x \\in '
                                                              '\\mathbb{R}$?',
                                                  'options': [   '\\mathbb{R}',
                                                                 '[0, \\infty)',
                                                                 '[2, \\infty)',
                                                                 '(2, \\infty)'],
                                                  'answer': 'c',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'Since $x^2 \\ge 0$ for all real '
                                                                 '$x$, $x^2 + 2 \\ge 2$. Thus, the '
                                                                 'minimum value is $2$ and range '
                                                                 'is $[2, \\infty)$.'},
                                              {   'question': 'If $f(x) = x^2$ and $g(x) = 2x + '
                                                              '1$, then $(f + g)(2)$ equals:',
                                                  'options': ['7', '9', '8', '5'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': '$f(2) = 2^2 = 4$ and $g(2) = '
                                                                 '2(2) + 1 = 5$. Thus, $(f + g)(2) '
                                                                 '= f(2) + g(2) = 4 + 5 = 9$.'},
                                              {   'question': 'Which of the following ordered '
                                                              'pairs represents a valid function '
                                                              'from $A = \\{1, 2, 3\\}$ to $B = '
                                                              '\\{a, b\\}$?',
                                                  'options': [   '\\{(1, a), (2, b)\\}',
                                                                 '\\{(1, a), (1, b), (2, a), (3, '
                                                                 'b)\\}',
                                                                 '\\{(1, a), (2, a), (3, b)\\}',
                                                                 '\\{(1, b), (3, a)\\'],
                                                  'answer': 'c',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'For a valid function from $A$ to '
                                                                 '$B$, every element in $A$ must '
                                                                 'be paired with exactly one '
                                                                 'element in $B$.'},
                                              {   'question': 'The range of the constant function '
                                                              '$f(x) = c$ for all $x \\in '
                                                              '\\mathbb{R}$ is:',
                                                  'options': [   '\\mathbb{R}',
                                                                 '\\{c\\}',
                                                                 '(0, c)',
                                                                 '[c, \\infty)'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'A constant function maps every '
                                                                 'domain element to a single '
                                                                 'constant value $c$, so its range '
                                                                 'is the singleton set $\\{c\\}$.'},
                                              {   'question': 'What is the range of $f(x) = '
                                                              '\\frac{x}{|x|}$ for $x \\neq 0$?',
                                                  'options': [   '[-1, 1]',
                                                                 '\\{-1, 1\\}',
                                                                 '\\mathbb{R}',
                                                                 '[0, 1]'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'For $x > 0$, $\\frac{x}{x} = 1$. '
                                                                 'For $x < 0$, $\\frac{x}{-x} = '
                                                                 '-1$. The function produces only '
                                                                 'the set of values $\\{-1, '
                                                                 '1\\}$.'}],
    'Chapter 3: Trigonometric Functions': [   {   'question': 'What is the degree measure '
                                                              'equivalent of $\\frac{2\\pi}{3}$ '
                                                              'radians?',
                                                  'options': ['60°', '120°', '135°', '150°'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'To convert radians to degrees, '
                                                                 'multiply by '
                                                                 '$\\frac{180^\\circ}{\\pi}$: '
                                                                 '$\\frac{2\\pi}{3} \\times '
                                                                 '\\frac{180^\\circ}{\\pi} = '
                                                                 '120^\\circ$.'},
                                              {   'question': 'What is the principal value of '
                                                              '$\\sin\\left(-\\frac{\\pi}{6}\\right)$?',
                                                  'options': [   '1/2',
                                                                 '-1/2',
                                                                 '\\sqrt{3}/2',
                                                                 '-\\sqrt{3}/2'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Since $\\sin(-x) = -\\sin(x)$, '
                                                                 '$\\sin\\left(-\\frac{\\pi}{6}\\right) '
                                                                 '= '
                                                                 '-\\sin\\left(\\frac{\\pi}{6}\\right) '
                                                                 '= -\\frac{1}{2}$.'},
                                              {   'question': 'Which of the following is the '
                                                              'correct identity for $\\cos(A + '
                                                              'B)$?',
                                                  'options': [   '\\cos A \\cos B + \\sin A \\sin '
                                                                 'B',
                                                                 '\\cos A \\cos B - \\sin A \\sin '
                                                                 'B',
                                                                 '\\sin A \\cos B + \\cos A \\sin '
                                                                 'B',
                                                                 '\\sin A \\cos B - \\cos A \\sin '
                                                                 'B'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'The standard cosine addition '
                                                                 'formula is $\\cos(A + B) = \\cos '
                                                                 'A \\cos B - \\sin A \\sin B$.'},
                                              {   'question': 'What is the period of the '
                                                              'trigonometric function $f(x) = '
                                                              '\\tan x$?',
                                                  'options': ['\\pi / 2', '\\pi', '2\\pi', '4\\pi'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'The fundamental period of the '
                                                                 'tangent function $\\tan x$ is '
                                                                 '$\\pi$ radians.'},
                                              {   'question': 'The value of $\\cos(15^\\circ)$ is '
                                                              'equal to:',
                                                  'options': [   '\\frac{\\sqrt{3} - '
                                                                 '1}{2\\sqrt{2}}',
                                                                 '\\frac{\\sqrt{3} + '
                                                                 '1}{2\\sqrt{2}}',
                                                                 '\\frac{1}{\\sqrt{2}}',
                                                                 '\\frac{\\sqrt{3}}{2}'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': '$\\cos(15^\\circ) = '
                                                                 '\\cos(45^\\circ - 30^\\circ) = '
                                                                 '\\cos 45^\\circ \\cos 30^\\circ '
                                                                 '+ \\sin 45^\\circ \\sin '
                                                                 '30^\\circ = '
                                                                 '\\frac{1}{\\sqrt{2}}\\frac{\\sqrt{3}}{2} '
                                                                 '+ '
                                                                 '\\frac{1}{\\sqrt{2}}\\frac{1}{2} '
                                                                 '= '
                                                                 '\\frac{\\sqrt{3}+1}{2\\sqrt{2}}$.'},
                                              {   'question': 'If $\\tan x = -\\frac{5}{12}$ and '
                                                              '$x$ lies in the second quadrant, '
                                                              'what is the value of $\\sin x$?',
                                                  'options': ['5/13', '-5/13', '12/13', '-12/13'],
                                                  'answer': 'a',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'In Quadrant II, sine is '
                                                                 'positive. Using identity $1 + '
                                                                 '\\cot^2 x = \\csc^2 x$, $\\csc x '
                                                                 '= \\sqrt{1 + (144/25)} = 13/5 '
                                                                 '\\implies \\sin x = 5/13$.'},
                                              {   'question': 'What is the value of $\\sin(2x)$ in '
                                                              'terms of $\\tan x$?',
                                                  'options': [   '\\frac{2\\tan x}{1 - \\tan^2 x}',
                                                                 '\\frac{2\\tan x}{1 + \\tan^2 x}',
                                                                 '\\frac{1 - \\tan^2 x}{1 + '
                                                                 '\\tan^2 x}',
                                                                 '\\frac{1 + \\tan^2 x}{2\\tan x}'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'The double angle formula for '
                                                                 'sine in terms of tangent is '
                                                                 '$\\sin(2x) = \\frac{2\\tan x}{1 '
                                                                 '+ \\tan^2 x}$.'},
                                              {   'question': 'The value of $\\cos(-750^\\circ)$ '
                                                              'is:',
                                                  'options': [   '1/2',
                                                                 '-1/2',
                                                                 '\\sqrt{3}/2',
                                                                 '-\\sqrt{3}/2'],
                                                  'answer': 'c',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': '$\\cos(-750^\\circ) = '
                                                                 '\\cos(750^\\circ) = \\cos(2 '
                                                                 '\\times 360^\\circ + 30^\\circ) '
                                                                 '= \\cos(30^\\circ) = '
                                                                 '\\frac{\\sqrt{3}}{2}$.'},
                                              {   'question': 'Find the radian measure of the '
                                                              'angle subtended at the center of a '
                                                              'circle of radius 10 cm by an arc of '
                                                              'length 15 cm.',
                                                  'options': [   '0.6 rad',
                                                                 '1.5 rad',
                                                                 '2.5 rad',
                                                                 '3.0 rad'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Formula: $\\theta = \\frac{l}{r} '
                                                                 '= \\frac{15}{10} = 1.5\\text{ '
                                                                 'radians}$.'},
                                              {   'question': 'What is the maximum value of the '
                                                              'function $f(x) = 3\\sin x + 4\\cos '
                                                              'x$?',
                                                  'options': ['5', '7', '1', '12'],
                                                  'answer': 'a',
                                                  'Difficulty': 'Difficult',
                                                  'Explanation': 'The maximum value of $a\\sin x + '
                                                                 'b\\cos x$ is $\\sqrt{a^2 + b^2} '
                                                                 '= \\sqrt{3^2 + 4^2} = \\sqrt{25} '
                                                                 '= 5$.'}],
    'Chapter 4: Complex Numbers and Quadratic Equations': [   {   'question': 'What is the value '
                                                                              'of $i^{19}$?',
                                                                  'options': ['1', '-1', 'i', '-i'],
                                                                  'answer': 'd',
                                                                  'Difficulty': 'Easy',
                                                                  'Explanation': '$i^{19} = i^{16 '
                                                                                 '+ 3} = (i^4)^4 '
                                                                                 '\\cdot i^3 = 1 '
                                                                                 '\\cdot (-i) = '
                                                                                 '-i$.'},
                                                              {   'question': 'The modulus of the '
                                                                              'complex number $z = '
                                                                              '3 - 4i$ is:',
                                                                  'options': ['5', '25', '7', '1'],
                                                                  'answer': 'a',
                                                                  'Difficulty': 'Easy',
                                                                  'Explanation': '$|z| = '
                                                                                 '\\sqrt{a^2 + '
                                                                                 'b^2} = '
                                                                                 '\\sqrt{3^2 + '
                                                                                 '(-4)^2} = '
                                                                                 '\\sqrt{9 + 16} = '
                                                                                 '5$.'},
                                                              {   'question': 'What is the '
                                                                              'multiplicative '
                                                                              'inverse of the '
                                                                              'complex number $z = '
                                                                              '1 + i$?',
                                                                  'options': [   '1 - i',
                                                                                 '\\frac{1}{2} - '
                                                                                 '\\frac{1}{2}i',
                                                                                 '\\frac{1}{2} + '
                                                                                 '\\frac{1}{2}i',
                                                                                 '-1 - i'],
                                                                  'answer': 'b',
                                                                  'Difficulty': 'Moderate',
                                                                  'Explanation': '$z^{-1} = '
                                                                                 '\\frac{\\bar{z}}{|z|^2} '
                                                                                 '= \\frac{1 - '
                                                                                 'i}{1^2 + 1^2} = '
                                                                                 '\\frac{1 - i}{2} '
                                                                                 '= \\frac{1}{2} - '
                                                                                 '\\frac{1}{2}i$.'},
                                                              {   'question': 'If $z = -1 + '
                                                                              'i\\sqrt{3}$, what '
                                                                              'is the argument '
                                                                              '$\\text{Arg}(z)$ of '
                                                                              'the complex number?',
                                                                  'options': [   '\\pi / 3',
                                                                                 '2\\pi / 3',
                                                                                 '4\\pi / 3',
                                                                                 '5\\pi / 6'],
                                                                  'answer': 'b',
                                                                  'Difficulty': 'Moderate',
                                                                  'Explanation': '$z$ lies in '
                                                                                 'Quadrant II. '
                                                                                 '$\\tan\\alpha = '
                                                                                 '|\\frac{\\sqrt{3}}{-1}| '
                                                                                 '= \\sqrt{3} '
                                                                                 '\\implies '
                                                                                 '\\alpha = '
                                                                                 '\\frac{\\pi}{3}$. '
                                                                                 'Argument = $\\pi '
                                                                                 '- \\alpha = '
                                                                                 '\\frac{2\\pi}{3}$.'},
                                                              {   'question': 'The roots of the '
                                                                              'quadratic equation '
                                                                              '$x^2 + x + 1 = 0$ '
                                                                              'are:',
                                                                  'options': [   '1, -1',
                                                                                 '\\frac{-1 \\pm '
                                                                                 'i\\sqrt{3}}{2}',
                                                                                 '\\frac{1 \\pm '
                                                                                 'i\\sqrt{3}}{2}',
                                                                                 '\\pm i'],
                                                                  'answer': 'b',
                                                                  'Difficulty': 'Moderate',
                                                                  'Explanation': 'Using quadratic '
                                                                                 'formula $x = '
                                                                                 '\\frac{-b \\pm '
                                                                                 '\\sqrt{b^2 - '
                                                                                 '4ac}}{2a} = '
                                                                                 '\\frac{-1 \\pm '
                                                                                 '\\sqrt{1 - '
                                                                                 '4}}{2} = '
                                                                                 '\\frac{-1 \\pm '
                                                                                 'i\\sqrt{3}}{2}$.'},
                                                              {   'question': 'The conjugate of '
                                                                              'the complex number '
                                                                              '$z = (2 + 3i)^2$ '
                                                                              'is:',
                                                                  'options': [   '-5 - 12i',
                                                                                 '-5 + 12i',
                                                                                 '5 - 12i',
                                                                                 '13 - 12i'],
                                                                  'answer': 'a',
                                                                  'Difficulty': 'Moderate',
                                                                  'Explanation': '$z = 4 + 12i + '
                                                                                 '9i^2 = -5 + '
                                                                                 '12i$. Therefore, '
                                                                                 'the conjugate '
                                                                                 '$\\bar{z} = -5 - '
                                                                                 '12i$.'},
                                                              {   'question': 'If $|z - i| = |z + '
                                                                              'i|$, then the locus '
                                                                              'of $z$ in the '
                                                                              'Argand plane is:',
                                                                  'options': [   'A circle',
                                                                                 'The Real axis '
                                                                                 '(X-axis)',
                                                                                 'The Imaginary '
                                                                                 'axis (Y-axis)',
                                                                                 'An ellipse'],
                                                                  'answer': 'b',
                                                                  'Difficulty': 'Difficult',
                                                                  'Explanation': '$|z - i| = |z + '
                                                                                 'i|$ means $z$ is '
                                                                                 'equidistant from '
                                                                                 '$(0, 1)$ and '
                                                                                 '$(0, -1)$, which '
                                                                                 'represents the '
                                                                                 'perpendicular '
                                                                                 'bisector of '
                                                                                 'these points: '
                                                                                 'the real axis '
                                                                                 '($y = 0$).'},
                                                              {   'question': 'What is the '
                                                                              'principal argument '
                                                                              'of a purely '
                                                                              'negative real '
                                                                              'number?',
                                                                  'options': [   '0',
                                                                                 '\\pi / 2',
                                                                                 '\\pi',
                                                                                 '-\\pi / 2'],
                                                                  'answer': 'c',
                                                                  'Difficulty': 'Easy',
                                                                  'Explanation': 'A negative real '
                                                                                 'number lies on '
                                                                                 'the negative '
                                                                                 'real axis in the '
                                                                                 'Argand plane, '
                                                                                 'which makes an '
                                                                                 'angle of $\\pi$ '
                                                                                 'radians with the '
                                                                                 'positive real '
                                                                                 'axis.'},
                                                              {   'question': 'The polar form of '
                                                                              '$z = 1 + i$ is:',
                                                                  'options': [   '\\sqrt{2}\\left(\\cos\\frac{\\pi}{4} '
                                                                                 '+ '
                                                                                 'i\\sin\\frac{\\pi}{4}\\right)',
                                                                                 '2\\left(\\cos\\frac{\\pi}{4} '
                                                                                 '+ '
                                                                                 'i\\sin\\frac{\\pi}{4}\\right)',
                                                                                 '\\sqrt{2}\\left(\\cos\\frac{\\pi}{3} '
                                                                                 '+ '
                                                                                 'i\\sin\\frac{\\pi}{3}\\right)',
                                                                                 '\\cos\\frac{\\pi}{4} '
                                                                                 '+ '
                                                                                 'i\\sin\\frac{\\pi}{4}'],
                                                                  'answer': 'a',
                                                                  'Difficulty': 'Moderate',
                                                                  'Explanation': 'Modulus $r = '
                                                                                 '\\sqrt{1^2 + '
                                                                                 '1^2} = '
                                                                                 '\\sqrt{2}$, '
                                                                                 'argument '
                                                                                 '$\\theta = '
                                                                                 '\\frac{\\pi}{4}$. '
                                                                                 'Thus $z = '
                                                                                 '\\sqrt{2}(\\cos\\frac{\\pi}{4} '
                                                                                 '+ '
                                                                                 'i\\sin\\frac{\\pi}{4})$.'},
                                                              {   'question': 'If $i^2 = -1$, then '
                                                                              '$1 + i^2 + i^4 + '
                                                                              'i^6 + \\dots + '
                                                                              'i^{2n}$ (where $n$ '
                                                                              'is an odd positive '
                                                                              'integer) equals:',
                                                                  'options': ['0', '1', '-1', 'i'],
                                                                  'answer': 'a',
                                                                  'Difficulty': 'Difficult',
                                                                  'Explanation': 'The terms '
                                                                                 'alternate as $1 '
                                                                                 '- 1 + 1 - 1 '
                                                                                 '\\dots$. Since '
                                                                                 'there are $n + '
                                                                                 '1$ terms and $n$ '
                                                                                 'is odd, $n+1$ is '
                                                                                 'even, so all '
                                                                                 'terms pair up '
                                                                                 'and cancel out '
                                                                                 'to $0$.'}],
    'Chapter 5: Linear Inequalities': [   {   'question': 'If $-3x + 6 < 0$, then which of the '
                                                          'following is true for $x \\in '
                                                          '\\mathbb{R}$?',
                                              'options': ['x < 2', 'x > 2', 'x < -2', 'x > -2'],
                                              'answer': 'b',
                                              'Difficulty': 'Easy',
                                              'Explanation': '$-3x < -6$. Dividing both sides by '
                                                             '$-3$ reverses the inequality sign, '
                                                             'giving $x > 2$.'},
                                          {   'question': 'The solution set of the inequality $|x| '
                                                          '< 5$ for $x \\in \\mathbb{R}$ is:',
                                              'options': [   '(-5, 5)',
                                                             '[-5, 5]',
                                                             '(-\\infty, -5) \\cup (5, \\infty)',
                                                             '(0, 5)'],
                                              'answer': 'a',
                                              'Difficulty': 'Easy',
                                              'Explanation': '$|x| < a$ unravels directly to $-a < '
                                                             'x < a$. Thus, $-5 < x < 5$, or $(-5, '
                                                             '5)$.'},
                                          {   'question': 'The solution set of the inequality $|x '
                                                          '- 2| \\ge 3$ is:',
                                              'options': [   '[-1, 5]',
                                                             '(-\\infty, -1] \\cup [5, \\infty)',
                                                             '(-1, 5)',
                                                             '[1, 5]'],
                                              'answer': 'b',
                                              'Difficulty': 'Moderate',
                                              'Explanation': '$|x - 2| \\ge 3 \\implies x - 2 \\le '
                                                             '-3$ or $x - 2 \\ge 3 \\implies x '
                                                             '\\le -1$ or $x \\ge 5$.'},
                                          {   'question': 'If $a > b$ and $c < 0$, then which of '
                                                          'the following relations is correct?',
                                              'options': [   'a/c > b/c',
                                                             'a/c < b/c',
                                                             'a + c < b + c',
                                                             'a - c < b - c'],
                                              'answer': 'b',
                                              'Difficulty': 'Easy',
                                              'Explanation': 'Dividing or multiplying both sides '
                                                             'of an inequality by a negative '
                                                             'number reverses the inequality '
                                                             'sign.'},
                                          {   'question': 'Solve for $x$: $\\frac{x}{4} < '
                                                          '\\frac{5x - 2}{3} - \\frac{7x - 3}{5}$.',
                                              'options': ['x < 4', 'x > 4', 'x < -4', 'x > -4'],
                                              'answer': 'b',
                                              'Difficulty': 'Difficult',
                                              'Explanation': 'Multiply terms by LCM 60: $15x < '
                                                             '20(5x - 2) - 12(7x - 3) \\implies '
                                                             '15x < 100x - 40 - 84x + 36 \\implies '
                                                             '15x < 16x - 4 \\implies -x < -4 '
                                                             '\\implies x > 4$.'},
                                          {   'question': 'The graphical representation of $y \\ge '
                                                          '0$ includes which region of the '
                                                          'Cartesian plane?',
                                              'options': [   'Left half-plane',
                                                             'Right half-plane',
                                                             'Upper half-plane including X-axis',
                                                             'Lower half-plane'],
                                              'answer': 'c',
                                              'Difficulty': 'Easy',
                                              'Explanation': '$y \\ge 0$ represents all points on '
                                                             'and above the horizontal X-axis.'},
                                          {   'question': 'Which integer value does NOT satisfy '
                                                          'the linear inequality $2(x - 1) < x + '
                                                          '5$?',
                                              'options': ['5', '6', '7', '0'],
                                              'answer': 'c',
                                              'Difficulty': 'Moderate',
                                              'Explanation': '$2x - 2 < x + 5 \\implies x < 7$. '
                                                             'Therefore, $7$ does not satisfy the '
                                                             'strict inequality.'},
                                          {   'question': 'The solution set of $\\frac{x - 1}{x + '
                                                          '2} > 0$ is:',
                                              'options': [   '(-2, 1)',
                                                             '(-\\infty, -2) \\cup (1, \\infty)',
                                                             '(1, \\infty)',
                                                             '(-\\infty, -2)'],
                                              'answer': 'b',
                                              'Difficulty': 'Difficult',
                                              'Explanation': 'Critical points are $-2$ and $1$. '
                                                             'The expression is positive when $x < '
                                                             '-2$ or $x > 1$.'},
                                          {   'question': 'A student needs an average score of at '
                                                          'least 80 marks across 4 tests. If '
                                                          'scores in the first 3 tests are 75, 82, '
                                                          'and 88, what is the minimum score '
                                                          'needed in the 4th test?',
                                              'options': ['70', '75', '80', '85'],
                                              'answer': 'b',
                                              'Difficulty': 'Moderate',
                                              'Explanation': '$\\frac{75 + 82 + 88 + x}{4} \\ge 80 '
                                                             '\\implies 245 + x \\ge 320 \\implies '
                                                             'x \\ge 75$.'},
                                          {   'question': 'If $x$ is a natural number ($x \\in '
                                                          '\\mathbb{N}$), what is the solution set '
                                                          'of $30x < 200$?',
                                              'options': [   '\\{1, 2, 3, 4, 5, 6\\}',
                                                             '\\{0, 1, 2, 3, 4, 5, 6\\}',
                                                             '( -\\infty, 20/3 )',
                                                             '\\{1, 2, 3, 4, 5\\}'],
                                              'answer': 'a',
                                              'Difficulty': 'Moderate',
                                              'Explanation': '$x < \\frac{200}{30} \\approx 6.67$. '
                                                             'Since $x$ must be a natural number '
                                                             '($1, 2, 3...$), the set is $\\{1, 2, '
                                                             '3, 4, 5, 6\\}$.'}],
    'Chapter 6: Permutations and Combinations': [   {   'question': 'What is the value of $0!$ '
                                                                    '(zero factorial)?',
                                                        'options': [   '0',
                                                                       '1',
                                                                       'Undefined',
                                                                       'Infinity'],
                                                        'answer': 'b',
                                                        'Difficulty': 'Easy',
                                                        'Explanation': 'By definition in '
                                                                       'mathematics, $0! = 1$.'},
                                                    {   'question': 'The value of ${}^{n}C_{n}$ is '
                                                                    'equal to:',
                                                        'options': ['0', '1', 'n', 'n!'],
                                                        'answer': 'b',
                                                        'Difficulty': 'Easy',
                                                        'Explanation': '${}^{n}C_{n} = '
                                                                       '\\frac{n!}{n!(n-n)!} = '
                                                                       '\\frac{n!}{n!0!} = 1$.'},
                                                    {   'question': 'If ${}^{n}C_{8} = '
                                                                    '{}^{n}C_{2}$, then what is '
                                                                    'the value of $n$?',
                                                        'options': ['6', '8', '10', '16'],
                                                        'answer': 'c',
                                                        'Difficulty': 'Moderate',
                                                        'Explanation': 'If ${}^{n}C_{x} = '
                                                                       '{}^{n}C_{y}$, then either '
                                                                       '$x = y$ or $x + y = n$. '
                                                                       'Here $n = 8 + 2 = 10$.'},
                                                    {   'question': 'How many 3-digit numbers can '
                                                                    'be formed using digits 1, 2, '
                                                                    '3, 4, 5 without repeating any '
                                                                    'digit?',
                                                        'options': ['60', '125', '20', '120'],
                                                        'answer': 'a',
                                                        'Difficulty': 'Easy',
                                                        'Explanation': 'Using permutations: '
                                                                       '${}^5P_3 = 5 \\times 4 '
                                                                       '\\times 3 = 60$.'},
                                                    {   'question': 'How many diagonals are there '
                                                                    'in a polygon with $n$ sides?',
                                                        'options': [   '\\frac{n(n-1)}{2}',
                                                                       '\\frac{n(n-3)}{2}',
                                                                       '\\frac{n(n-2)}{2}',
                                                                       'n(n-3)'],
                                                        'answer': 'b',
                                                        'Difficulty': 'Moderate',
                                                        'Explanation': 'Total line segments '
                                                                       'joining $n$ vertices is '
                                                                       '${}^nC_2$. Subtracting $n$ '
                                                                       'boundary sides gives '
                                                                       '$\\frac{n(n-1)}{2} - n = '
                                                                       '\\frac{n(n-3)}{2}$.'},
                                                    {   'question': 'What is the relation between '
                                                                    '${}^{n}P_{r}$ and '
                                                                    '${}^{n}C_{r}$?',
                                                        'options': [   '{}^{n}P_{r} = r! \\cdot '
                                                                       '{}^{n}C_{r}',
                                                                       '{}^{n}C_{r} = r! \\cdot '
                                                                       '{}^{n}P_{r}',
                                                                       '{}^{n}P_{r} = '
                                                                       '\\frac{{}^{n}C_{r}}{r!}',
                                                                       '{}^{n}P_{r} = {}^{n}C_{r}'],
                                                        'answer': 'a',
                                                        'Difficulty': 'Easy',
                                                        'Explanation': 'Permutation accounts for '
                                                                       'order, so ${}^{n}P_{r} = '
                                                                       'r! \\times {}^{n}C_{r}$.'},
                                                    {   'question': 'In how many ways can 5 people '
                                                                    'sit in a circle?',
                                                        'options': ['120', '24', '60', '25'],
                                                        'answer': 'b',
                                                        'Difficulty': 'Moderate',
                                                        'Explanation': 'Circular permutations of '
                                                                       '$n$ distinct items is $(n '
                                                                       '- 1)!$. For 5 people, $(5 '
                                                                       '- 1)! = 4! = 24$.'},
                                                    {   'question': 'How many words (with or '
                                                                    'without meaning) can be '
                                                                    'formed using all letters of '
                                                                    "the word 'MATHEMATICS'?",
                                                        'options': [   '11!',
                                                                       '\\frac{11!}{2! 2! 2!}',
                                                                       '\\frac{11!}{2! 2!}',
                                                                       '\\frac{11!}{4!}'],
                                                        'answer': 'b',
                                                        'Difficulty': 'Moderate',
                                                        'Explanation': "'MATHEMATICS' has 11 "
                                                                       'letters with repeating '
                                                                       'letters M(2), A(2), T(2). '
                                                                       'Number of arrangements = '
                                                                       '$\\frac{11!}{2! 2! 2!}$.'},
                                                    {   'question': 'What is the value of ${}^nC_r '
                                                                    '+ {}^nC_{r-1}$?',
                                                        'options': [   '{}^{n+1}C_r',
                                                                       '{}^{n+1}C_{r-1}',
                                                                       '{}^nC_{r+1}',
                                                                       '{}^{n-1}C_r'],
                                                        'answer': 'a',
                                                        'Difficulty': 'Moderate',
                                                        'Explanation': "Pascal's identity states "
                                                                       'that ${}^nC_r + '
                                                                       '{}^nC_{r-1} = '
                                                                       '{}^{n+1}C_r$.'},
                                                    {   'question': 'A committee of 3 persons is '
                                                                    'to be chosen from a group of '
                                                                    '5 men and 4 women. In how '
                                                                    'many ways can this be done if '
                                                                    'it must contain 2 men and 1 '
                                                                    'woman?',
                                                        'options': ['40', '20', '60', '30'],
                                                        'answer': 'a',
                                                        'Difficulty': 'Difficult',
                                                        'Explanation': 'Choose 2 men from 5 and 1 '
                                                                       'woman from 4: ${}^5C_2 '
                                                                       '\\times {}^4C_1 = 10 '
                                                                       '\\times 4 = 40$ ways.'}],
    'Chapter 7: Binomial Theorem': [   {   'question': 'What is the total number of terms in the '
                                                       'expansion of $(x + a)^n$ where $n$ is a '
                                                       'positive integer?',
                                           'options': ['n', 'n - 1', 'n + 1', '2^n'],
                                           'answer': 'c',
                                           'Difficulty': 'Easy',
                                           'Explanation': 'The expansion of $(x + a)^n$ contains '
                                                          'indices ranging from $k=0$ to $k=n$, '
                                                          'yielding $n + 1$ terms.'},
                                       {   'question': 'The general term $T_{r+1}$ in the binomial '
                                                       'expansion of $(a + b)^n$ is given by:',
                                           'options': [   '{}^nC_r a^{n-r} b^r',
                                                          '{}^nC_r a^r b^{n-r}',
                                                          '{}^nC_{r+1} a^{n-r} b^r',
                                                          '{}^nC_{r-1} a^{n-r} b^r'],
                                           'answer': 'a',
                                           'Difficulty': 'Easy',
                                           'Explanation': 'By definition, the $(r+1)$-th term is '
                                                          '$T_{r+1} = {}^nC_r a^{n-r} b^r$.'},
                                       {   'question': 'What is the sum of all binomial '
                                                       'coefficients in the expansion of $(1 + '
                                                       'x)^n$?',
                                           'options': ['n', '2^n', '2^{n-1}', '2^n - 1'],
                                           'answer': 'b',
                                           'Difficulty': 'Easy',
                                           'Explanation': 'Substituting $x = 1$ in $(1 + x)^n = '
                                                          '{}^nC_0 + {}^nC_1 x + \\dots + {}^nC_n '
                                                          'x^n$ gives sum of coefficients equal to '
                                                          '$2^n$.'},
                                       {   'question': 'If $n$ is an even positive integer, which '
                                                       'term is the middle term in the expansion '
                                                       'of $(x + a)^n$?',
                                           'options': [   '\\left(\\frac{n}{2}\\right)\\text{th '
                                                          'term}',
                                                          '\\left(\\frac{n}{2} + '
                                                          '1\\right)\\text{th term}',
                                                          '\\left(\\frac{n+1}{2}\\right)\\text{th '
                                                          'term}',
                                                          '\\left(\\frac{n+2}{2}\\right)\\text{th '
                                                          'and } '
                                                          '\\left(\\frac{n+4}{2}\\right)\\text{th '
                                                          'terms}'],
                                           'answer': 'b',
                                           'Difficulty': 'Moderate',
                                           'Explanation': 'When $n$ is even, there are $n+1$ (odd) '
                                                          'terms, so the single middle term is at '
                                                          'position $\\frac{n}{2} + 1$.'},
                                       {   'question': 'What is the coefficient of $x^3$ in the '
                                                       'expansion of $(1 + 2x)^5$?',
                                           'options': ['10', '40', '80', '160'],
                                           'answer': 'c',
                                           'Difficulty': 'Moderate',
                                           'Explanation': 'Term containing $x^3$ is $T_{3+1} = '
                                                          '{}^5C_3 (1)^{2} (2x)^3 = 10 \\times '
                                                          '8x^3 = 80x^3$. Coefficient is 80.'},
                                       {   'question': 'The coefficient independent of $x$ in the '
                                                       'expansion of $\\left(x + '
                                                       '\\frac{1}{x}\\right)^{6}$ is:',
                                           'options': ['15', '20', '6', '1'],
                                           'answer': 'b',
                                           'Difficulty': 'Difficult',
                                           'Explanation': '$T_{r+1} = {}^6C_r (x)^{6-r} (x^{-1})^r '
                                                          '= {}^6C_r x^{6-2r}$. For independent '
                                                          'term, $6 - 2r = 0 \\implies r = 3$. '
                                                          'Value = ${}^6C_3 = 20$.'},
                                       {   'question': 'What is the sum of odd binomial '
                                                       'coefficients ${}^nC_1 + {}^nC_3 + {}^nC_5 '
                                                       '+ \\dots$?',
                                           'options': ['2^n', '2^{n-1}', '2^{n+1}', '2^n - 1'],
                                           'answer': 'b',
                                           'Difficulty': 'Moderate',
                                           'Explanation': 'The sum of odd coefficients equals the '
                                                          'sum of even coefficients, both equal to '
                                                          '$2^{n-1}$.'},
                                       {   'question': 'In the expansion of $(a + b)^n$, the ratio '
                                                       'of $T_{r+1}$ to $T_r$ is:',
                                           'options': [   '\\frac{n - r + 1}{r} \\frac{b}{a}',
                                                          '\\frac{n - r}{r + 1} \\frac{b}{a}',
                                                          '\\frac{n - r + 1}{r} \\frac{a}{b}',
                                                          '\\frac{r}{n - r + 1} \\frac{b}{a}'],
                                           'answer': 'a',
                                           'Difficulty': 'Difficult',
                                           'Explanation': '$\\frac{T_{r+1}}{T_r} = \\frac{{}^nC_r '
                                                          'a^{n-r} b^r}{{}^nC_{r-1} a^{n-r+1} '
                                                          'b^{r-1}} = \\frac{n-r+1}{r} \\cdot '
                                                          '\\frac{b}{a}$.'},
                                       {   'question': 'What is the value of ${}^nC_0 - {}^nC_1 + '
                                                       '{}^nC_2 - {}^nC_3 + \\dots + (-1)^n '
                                                       '{}^nC_n$?',
                                           'options': ['0', '1', '2^n', '-1'],
                                           'answer': 'a',
                                           'Difficulty': 'Easy',
                                           'Explanation': 'Substitute $x = -1$ in $(1 + x)^n$ to '
                                                          'get $(1 - 1)^n = 0$.'},
                                       {   'question': 'What is the 4th term from the end in the '
                                                       'expansion of $(x - 2y)^{10}$?',
                                           'options': [   '7th term from beginning',
                                                          '8th term from beginning',
                                                          '4th term from beginning',
                                                          '6th term from beginning'],
                                           'answer': 'b',
                                           'Difficulty': 'Moderate',
                                           'Explanation': 'The $k$-th term from the end in an '
                                                          'expansion with $N$ total terms is $(N - '
                                                          'k + 1)$-th term from start. Total terms '
                                                          '= $11$. Position = $11 - 4 + 1 = 8$th '
                                                          'term.'}],
    'Chapter 8: Sequences and Series': [   {   'question': 'If the $n$-th term of an Arithmetic '
                                                           'Progression (A.P.) is $a_n = 3n + 5$, '
                                                           'what is its common difference?',
                                               'options': ['3', '5', '8', '2'],
                                               'answer': 'a',
                                               'Difficulty': 'Easy',
                                               'Explanation': 'The common difference $d = a_n - '
                                                              'a_{n-1} = (3n + 5) - (3(n-1) + 5) = '
                                                              '3$.'},
                                           {   'question': 'What is the sum of the first $n$ '
                                                           'natural numbers?',
                                               'options': [   'n(n + 1)',
                                                              '\\frac{n(n + 1)}{2}',
                                                              '\\frac{n(n - 1)}{2}',
                                                              'n^2'],
                                               'answer': 'b',
                                               'Difficulty': 'Easy',
                                               'Explanation': 'Standard formula for sum of first '
                                                              '$n$ natural numbers is $\\sum n = '
                                                              '\\frac{n(n + 1)}{2}$.'},
                                           {   'question': 'If $a, b, c$ are in Geometric '
                                                           'Progression (G.P.), then which '
                                                           'relation holds true?',
                                               'options': [   'b = \\frac{a + c}{2}',
                                                              'b^2 = ac',
                                                              '2b = a + c',
                                                              'b = ac'],
                                               'answer': 'b',
                                               'Difficulty': 'Easy',
                                               'Explanation': 'For terms in G.P., the common ratio '
                                                              'is $\\frac{b}{a} = \\frac{c}{b} '
                                                              '\\implies b^2 = ac$.'},
                                           {   'question': 'The geometric mean (G.M.) between two '
                                                           'positive numbers 4 and 16 is:',
                                               'options': ['10', '8', '64', '12'],
                                               'answer': 'b',
                                               'Difficulty': 'Easy',
                                               'Explanation': 'Geometric Mean $\\text{G.M.} = '
                                                              '\\sqrt{a \\cdot b} = \\sqrt{4 '
                                                              '\\times 16} = \\sqrt{64} = 8$.'},
                                           {   'question': 'Find the sum of the infinite G.P.: $1, '
                                                           '\\frac{1}{2}, \\frac{1}{4}, '
                                                           '\\frac{1}{8}, \\dots$',
                                               'options': ['2', '1.5', '3', '4'],
                                               'answer': 'a',
                                               'Difficulty': 'Moderate',
                                               'Explanation': 'Sum of infinite G.P. $S_\\infty = '
                                                              '\\frac{a}{1 - r}$. Here $a = 1, r = '
                                                              '1/2 \\implies S_\\infty = '
                                                              '\\frac{1}{1 - 1/2} = 2$.'},
                                           {   'question': 'Which term of the A.P. $2, 7, 12, 17, '
                                                           '\\dots$ is $47$?',
                                               'options': ['8th', '9th', '10th', '11th'],
                                               'answer': 'c',
                                               'Difficulty': 'Moderate',
                                               'Explanation': '$a_n = a + (n - 1)d \\implies 47 = '
                                                              '2 + (n - 1)5 \\implies 45 = 5(n - '
                                                              '1) \\implies n - 1 = 9 \\implies n '
                                                              '= 10$.'},
                                           {   'question': 'If Arithmetic Mean (A.M.) and '
                                                           'Geometric Mean (G.M.) of two positive '
                                                           'numbers are $A$ and $G$ respectively, '
                                                           'then:',
                                               'options': [   'A \\le G',
                                                              'A \\ge G',
                                                              'A = G^2',
                                                              'A \\cdot G = 1'],
                                               'answer': 'b',
                                               'Difficulty': 'Easy',
                                               'Explanation': 'For any two positive real numbers, '
                                                              'Arithmetic Mean is always greater '
                                                              'than or equal to Geometric Mean ($A '
                                                              '\\ge G$).'},
                                           {   'question': 'What is the 7th term of the G.P. $3, '
                                                           '6, 12, 24, \\dots$?',
                                               'options': ['192', '384', '96', '144'],
                                               'answer': 'a',
                                               'Difficulty': 'Moderate',
                                               'Explanation': '$a = 3, r = 2$. Term $a_7 = a r^{6} '
                                                              '= 3 \\cdot (2)^6 = 3 \\cdot 64 = '
                                                              '192$.'},
                                           {   'question': 'The sum of the series $1^2 + 2^2 + 3^2 '
                                                           '+ \\dots + n^2$ is:',
                                               'options': [   '\\left[\\frac{n(n+1)}{2}\\right]^2',
                                                              '\\frac{n(n+1)(2n+1)}{6}',
                                                              '\\frac{n(n+1)(n+2)}{6}',
                                                              '\\frac{n^2(n+1)}{4}'],
                                               'answer': 'b',
                                               'Difficulty': 'Easy',
                                               'Explanation': 'Standard formula for sum of squares '
                                                              'of first $n$ natural numbers is '
                                                              '$\\frac{n(n+1)(2n+1)}{6}$.'},
                                           {   'question': 'If 3rd term of a G.P. is 4, then '
                                                           'product of its first 5 terms is:',
                                               'options': ['4^3', '4^5', '4^4', '1024'],
                                               'answer': 'b',
                                               'Difficulty': 'Difficult',
                                               'Explanation': 'Terms are $a/r^2, a/r, a, ar, '
                                                              'ar^2$. Product = $a^5$. Given $a_3 '
                                                              '= a = 4$, product = $4^5 = 1024$.'}],
    'Chapter 9: Straight Lines': [   {   'question': 'What is the slope of a line passing through '
                                                     'points $(2, 3)$ and $(4, 7)$?',
                                         'options': ['2', '1/2', '4', '-2'],
                                         'answer': 'a',
                                         'Difficulty': 'Easy',
                                         'Explanation': 'Slope $m = \\frac{y_2 - y_1}{x_2 - x_1} = '
                                                        '\\frac{7 - 3}{4 - 2} = \\frac{4}{2} = '
                                                        '2$.'},
                                     {   'question': 'What is the slope of a line perpendicular to '
                                                     'the line $y = 3x + 5$?',
                                         'options': ['3', '-3', '1/3', '-1/3'],
                                         'answer': 'd',
                                         'Difficulty': 'Easy',
                                         'Explanation': 'Perpendicular lines have slopes $m_1 m_2 '
                                                        '= -1$. Given $m_1 = 3$, $m_2 = -1/3$.'},
                                     {   'question': 'The equation of a straight line in '
                                                     'slope-intercept form is:',
                                         'options': [   'y = mx + c',
                                                        '\\frac{x}{a} + \\frac{y}{b} = 1',
                                                        'x \\cos\\omega + y \\sin\\omega = p',
                                                        'Ax + By + C = 0'],
                                         'answer': 'a',
                                         'Difficulty': 'Easy',
                                         'Explanation': '$y = mx + c$ represents slope-intercept '
                                                        'form where $m$ is slope and $c$ is '
                                                        'y-intercept.'},
                                     {   'question': 'What is the distance of the point $(3, 4)$ '
                                                     'from the origin $(0,0)$?',
                                         'options': ['5', '7', '1', '25'],
                                         'answer': 'a',
                                         'Difficulty': 'Easy',
                                         'Explanation': 'Distance $d = \\sqrt{3^2 + 4^2} = '
                                                        '\\sqrt{9 + 16} = 5$.'},
                                     {   'question': 'The acute angle $\\theta$ between two lines '
                                                     'with slopes $m_1$ and $m_2$ is given by:',
                                         'options': [   '\\tan\\theta = \\left|\\frac{m_1 - m_2}{1 '
                                                        '+ m_1 m_2}\\right|',
                                                        '\\tan\\theta = \\left|\\frac{m_1 + m_2}{1 '
                                                        '- m_1 m_2}\\right|',
                                                        '\\cos\\theta = \\frac{m_1 m_2}{1 + m_1 '
                                                        'm_2}',
                                                        '\\tan\\theta = m_1 - m_2'],
                                         'answer': 'a',
                                         'Difficulty': 'Moderate',
                                         'Explanation': 'Standard trigonometric formula for angle '
                                                        'between two lines using their slopes.'},
                                     {   'question': 'What is the distance between parallel lines '
                                                     '$3x + 4y + 5 = 0$ and $3x + 4y - 15 = 0$?',
                                         'options': ['2 units', '4 units', '5 units', '20 units'],
                                         'answer': 'b',
                                         'Difficulty': 'Moderate',
                                         'Explanation': 'Distance $d = \\frac{|c_1 - '
                                                        'c_2|}{\\sqrt{A^2 + B^2}} = \\frac{|5 - '
                                                        '(-15)|}{\\sqrt{3^2 + 4^2}} = '
                                                        '\\frac{20}{5} = 4$ units.'},
                                     {   'question': 'The equation of a line passing through $(1, '
                                                     '2)$ and parallel to the line $2x + 3y - 5 = '
                                                     '0$ is:',
                                         'options': [   '2x + 3y - 8 = 0',
                                                        '2x + 3y + 8 = 0',
                                                        '3x - 2y + 1 = 0',
                                                        '2x - 3y + 4 = 0'],
                                         'answer': 'a',
                                         'Difficulty': 'Moderate',
                                         'Explanation': 'Parallel line has form $2x + 3y + k = 0$. '
                                                        'Substituting $(1, 2) \\implies 2(1) + '
                                                        '3(2) + k = 0 \\implies k = -8$.'},
                                     {   'question': 'What is the x-intercept of the line $2x - 3y '
                                                     '= 6$?',
                                         'options': ['2', '3', '-2', '-3'],
                                         'answer': 'b',
                                         'Difficulty': 'Easy',
                                         'Explanation': 'Set $y = 0 \\implies 2x = 6 \\implies x = '
                                                        '3$.'},
                                     {   'question': 'Perpendicular distance of point $(x_1, y_1)$ '
                                                     'from the line $Ax + By + C = 0$ is:',
                                         'options': [   '\\frac{|Ax_1 + By_1 + C|}{\\sqrt{A^2 + '
                                                        'B^2}}',
                                                        '\\frac{Ax_1 + By_1 + C}{A^2 + B^2}',
                                                        '\\frac{|Ax_1 + By_1|}{\\sqrt{A^2 + B^2}}',
                                                        '\\frac{|Ax_1 - By_1 + C|}{A + B}'],
                                         'answer': 'a',
                                         'Difficulty': 'Easy',
                                         'Explanation': 'Standard formula for perpendicular '
                                                        'distance from a point to a line.'},
                                     {   'question': 'If lines $2x + y - 3 = 0$, $5x + k y - 3 = '
                                                     '0$, and $3x - y - 2 = 0$ are concurrent, '
                                                     'what is the value of $k$?',
                                         'options': ['-2', '2', '3', '-3'],
                                         'answer': 'd',
                                         'Difficulty': 'Difficult',
                                         'Explanation': 'Solve first and third line: $2x + y = 3$ '
                                                        'and $3x - y = 2 \\implies 5x = 5 '
                                                        '\\implies x = 1, y = 1$. Substitute point '
                                                        '$(1,1)$ into $5(1) + k(1) - 3 = 0 '
                                                        '\\implies k = -2$.'}],
    'Chapter 10: Conic Sections': [   {   'question': 'What is the equation of a circle centered '
                                                      'at origin $(0,0)$ with radius $r$?',
                                          'options': [   'x^2 - y^2 = r^2',
                                                         'x^2 + y^2 = r^2',
                                                         'x + y = r',
                                                         'y^2 = 4rx'],
                                          'answer': 'b',
                                          'Difficulty': 'Easy',
                                          'Explanation': 'Standard equation of a circle with '
                                                         'center at origin is $x^2 + y^2 = r^2$.'},
                                      {   'question': 'The coordinates of the focus of the '
                                                      'parabola $y^2 = 8x$ are:',
                                          'options': ['(2, 0)', '(0, 2)', '(-2, 0)', '(4, 0)'],
                                          'answer': 'a',
                                          'Difficulty': 'Easy',
                                          'Explanation': 'Comparing with $y^2 = 4ax$, $4a = 8 '
                                                         '\\implies a = 2$. Focus is $(a, 0) = (2, '
                                                         '0)$.'},
                                      {   'question': 'What is the length of the latus rectum of '
                                                      'the parabola $x^2 = 12y$?',
                                          'options': ['3', '6', '12', '4'],
                                          'answer': 'c',
                                          'Difficulty': 'Easy',
                                          'Explanation': 'For parabola $x^2 = 4ay$, length of '
                                                         'latus rectum is $4a = 12$.'},
                                      {   'question': 'The eccentricity $e$ of an ellipse '
                                                      'satisfies which of the following '
                                                      'conditions?',
                                          'options': ['e = 0', '0 < e < 1', 'e = 1', 'e > 1'],
                                          'answer': 'b',
                                          'Difficulty': 'Easy',
                                          'Explanation': 'For an ellipse, eccentricity $e$ is '
                                                         'strictly between 0 and 1 ($0 < e < 1$).'},
                                      {   'question': 'What is the relationship between semi-major '
                                                      'axis $a$, semi-minor axis $b$, and focal '
                                                      'length $c$ for an ellipse?',
                                          'options': [   'a^2 = b^2 + c^2',
                                                         'c^2 = a^2 + b^2',
                                                         'b^2 = a^2 + c^2',
                                                         'a = b + c'],
                                          'answer': 'a',
                                          'Difficulty': 'Moderate',
                                          'Explanation': 'In an ellipse, major axis semi-length '
                                                         '$a$ is the hypotenuse relationship: $a^2 '
                                                         '= b^2 + c^2$.'},
                                      {   'question': 'The eccentricity $e$ of a hyperbola is '
                                                      'given by:',
                                          'options': [   'e = \\sqrt{1 - \\frac{b^2}{a^2}}',
                                                         'e = \\sqrt{1 + \\frac{b^2}{a^2}}',
                                                         'e = \\frac{a}{b}',
                                                         'e = \\sqrt{\\frac{a^2}{b^2} - 1}'],
                                          'answer': 'b',
                                          'Difficulty': 'Moderate',
                                          'Explanation': 'For hyperbola, $c^2 = a^2 + b^2 '
                                                         '\\implies e = \\frac{c}{a} = \\sqrt{1 + '
                                                         '\\frac{b^2}{a^2}}$.'},
                                      {   'question': 'What is the center and radius of the circle '
                                                      '$x^2 + y^2 - 4x + 6y - 12 = 0$?',
                                          'options': [   'Center (2, -3), Radius = 5',
                                                         'Center (-2, 3), Radius = 5',
                                                         'Center (2, -3), Radius = 25',
                                                         'Center (-4, 6), Radius = 12'],
                                          'answer': 'a',
                                          'Difficulty': 'Difficult',
                                          'Explanation': 'Center $(-g, -f) = (2, -3)$. Radius $r = '
                                                         '\\sqrt{g^2 + f^2 - c} = \\sqrt{(-2)^2 + '
                                                         '3^2 - (-12)} = \\sqrt{4 + 9 + 12} = '
                                                         '\\sqrt{25} = 5$.'},
                                      {   'question': 'The equation of directrix of parabola $y^2 '
                                                      '= -16x$ is:',
                                          'options': ['x = 4', 'x = -4', 'y = 4', 'y = -4'],
                                          'answer': 'a',
                                          'Difficulty': 'Moderate',
                                          'Explanation': '$4a = 16 \\implies a = 4$. For $y^2 = '
                                                         '-4ax$, directrix is vertical line $x = a '
                                                         '\\implies x = 4$.'},
                                      {   'question': 'What is the length of latus rectum of the '
                                                      'ellipse $\\frac{x^2}{25} + \\frac{y^2}{9} = '
                                                      '1$?',
                                          'options': ['18/5', '9/5', '5/18', '10/3'],
                                          'answer': 'a',
                                          'Difficulty': 'Moderate',
                                          'Explanation': '$a^2 = 25 \\implies a = 5$, and $b^2 = '
                                                         '9$. Length of latus rectum = '
                                                         '$\\frac{2b^2}{a} = \\frac{2(9)}{5} = '
                                                         '\\frac{18}{5}$.'},
                                      {   'question': 'Which conic section is represented by '
                                                      'equation $x^2 - y^2 = 16$?',
                                          'options': [   'Circle',
                                                         'Parabola',
                                                         'Ellipse',
                                                         'Rectangular Hyperbola'],
                                          'answer': 'd',
                                          'Difficulty': 'Easy',
                                          'Explanation': 'A hyperbola with equal semi-axes $a = b$ '
                                                         '($x^2 - y^2 = a^2$) is called a '
                                                         'rectangular hyperbola.'}],
    'Chapter 11: Introduction to Three Dimensional Geometry': [   {   'question': 'How many '
                                                                                  'octants are '
                                                                                  'formed by the '
                                                                                  'three mutually '
                                                                                  'perpendicular '
                                                                                  'coordinate '
                                                                                  'planes in 3D '
                                                                                  'space?',
                                                                      'options': [   '4',
                                                                                     '6',
                                                                                     '8',
                                                                                     '12'],
                                                                      'answer': 'c',
                                                                      'Difficulty': 'Easy',
                                                                      'Explanation': 'Three '
                                                                                     'coordinate '
                                                                                     'planes '
                                                                                     'divide 3D '
                                                                                     'space into 8 '
                                                                                     'regions '
                                                                                     'called '
                                                                                     'octants.'},
                                                                  {   'question': 'The distance of '
                                                                                  'point $P(x, y, '
                                                                                  'z)$ from the '
                                                                                  'origin $(0, 0, '
                                                                                  '0)$ is:',
                                                                      'options': [   'x + y + z',
                                                                                     '\\sqrt{x^2 + '
                                                                                     'y^2 + z^2}',
                                                                                     'x^2 + y^2 + '
                                                                                     'z^2',
                                                                                     '\\sqrt{x + y '
                                                                                     '+ z}'],
                                                                      'answer': 'b',
                                                                      'Difficulty': 'Easy',
                                                                      'Explanation': 'By 3D '
                                                                                     'distance '
                                                                                     'formula, '
                                                                                     'distance '
                                                                                     'from origin '
                                                                                     'is '
                                                                                     '$\\sqrt{x^2 '
                                                                                     '+ y^2 + '
                                                                                     'z^2}$.'},
                                                                  {   'question': 'In which octant '
                                                                                  'does the point '
                                                                                  '$(-3, 1, -2)$ '
                                                                                  'lie?',
                                                                      'options': [   'II',
                                                                                     'V',
                                                                                     'VI',
                                                                                     'VIII'],
                                                                      'answer': 'c',
                                                                      'Difficulty': 'Moderate',
                                                                      'Explanation': 'Sign pattern '
                                                                                     '$(- , +, -)$ '
                                                                                     'corresponds '
                                                                                     'to Octant '
                                                                                     'VI.'},
                                                                  {   'question': 'What are the '
                                                                                  'coordinates of '
                                                                                  'any point on '
                                                                                  'the Y-axis?',
                                                                      'options': [   '(x, 0, 0)',
                                                                                     '(0, y, 0)',
                                                                                     '(0, 0, z)',
                                                                                     '(x, y, 0)'],
                                                                      'answer': 'b',
                                                                      'Difficulty': 'Easy',
                                                                      'Explanation': 'On the '
                                                                                     'Y-axis, both '
                                                                                     'x-coordinate '
                                                                                     'and '
                                                                                     'z-coordinate '
                                                                                     'are equal to '
                                                                                     '0.'},
                                                                  {   'question': 'Find the '
                                                                                  'distance '
                                                                                  'between points '
                                                                                  '$A(1, -3, 4)$ '
                                                                                  'and $B(-4, 1, '
                                                                                  '2)$.',
                                                                      'options': [   '3',
                                                                                     'sqrt(45)',
                                                                                     'sqrt(33)',
                                                                                     'sqrt(57)'],
                                                                      'answer': 'b',
                                                                      'Difficulty': 'Moderate',
                                                                      'Explanation': '$d = '
                                                                                     '\\sqrt{(-4-1)^2 '
                                                                                     '+ (1 - '
                                                                                     '(-3))^2 + '
                                                                                     '(2-4)^2} = '
                                                                                     '\\sqrt{(-5)^2 '
                                                                                     '+ 4^2 + '
                                                                                     '(-2)^2} = '
                                                                                     '\\sqrt{25 + '
                                                                                     '16 + 4} = '
                                                                                     '\\sqrt{45} = '
                                                                                     '3\\sqrt{5}$.'},
                                                                  {   'question': 'What is the '
                                                                                  'equation of the '
                                                                                  'XY-plane?',
                                                                      'options': [   'x = 0',
                                                                                     'y = 0',
                                                                                     'z = 0',
                                                                                     'x + y = 0'],
                                                                      'answer': 'c',
                                                                      'Difficulty': 'Easy',
                                                                      'Explanation': 'At every '
                                                                                     'point on the '
                                                                                     'XY-plane, '
                                                                                     'the '
                                                                                     'z-coordinate '
                                                                                     'is zero ($z '
                                                                                     '= 0$).'},
                                                                  {   'question': 'If a line '
                                                                                  'segment joining '
                                                                                  '$A(2, 3, 5)$ '
                                                                                  'and $B(1, -2, '
                                                                                  '3)$ is divided '
                                                                                  'internally by '
                                                                                  'point $P$ in '
                                                                                  'ratio $1 : 2$, '
                                                                                  'find '
                                                                                  'coordinates of '
                                                                                  '$P$.',
                                                                      'options': [   '(5/3, 4/3, '
                                                                                     '13/3)',
                                                                                     '(4/3, 1/3, '
                                                                                     '11/3)',
                                                                                     '(5/3, -1/3, '
                                                                                     '11/3)',
                                                                                     '(1, 1, 4)'],
                                                                      'answer': 'a',
                                                                      'Difficulty': 'Difficult',
                                                                      'Explanation': 'Section '
                                                                                     'formula $x = '
                                                                                     '\\frac{m x_2 '
                                                                                     '+ n '
                                                                                     'x_1}{m+n} = '
                                                                                     '\\frac{1(1) '
                                                                                     '+ 2(2)}{3} = '
                                                                                     '\\frac{5}{3}$; '
                                                                                     '$y = '
                                                                                     '\\frac{1(-2) '
                                                                                     '+ 2(3)}{3} = '
                                                                                     '\\frac{4}{3}$; '
                                                                                     '$z = '
                                                                                     '\\frac{1(3) '
                                                                                     '+ 2(5)}{3} = '
                                                                                     '\\frac{13}{3}$.'},
                                                                  {   'question': 'The midpoint of '
                                                                                  'the line '
                                                                                  'segment joining '
                                                                                  'points $(2, 4, '
                                                                                  '10)$ and $(6, '
                                                                                  '8, -2)$ is:',
                                                                      'options': [   '(4, 6, 4)',
                                                                                     '(8, 12, 8)',
                                                                                     '(2, 2, 6)',
                                                                                     '(4, 6, 8)'],
                                                                      'answer': 'a',
                                                                      'Difficulty': 'Easy',
                                                                      'Explanation': 'Midpoint '
                                                                                     '$=\\left(\\frac{2+6}{2}, '
                                                                                     '\\frac{4+8}{2}, '
                                                                                     '\\frac{10-2}{2}\\right) '
                                                                                     '= (4, 6, '
                                                                                     '4)$.'},
                                                                  {   'question': 'What is the '
                                                                                  'image of the '
                                                                                  'point $(2, 3, '
                                                                                  '4)$ with '
                                                                                  'respect to the '
                                                                                  'XY-plane?',
                                                                      'options': [   '(-2, 3, 4)',
                                                                                     '(2, -3, 4)',
                                                                                     '(2, 3, -4)',
                                                                                     '(-2, -3, '
                                                                                     '-4)'],
                                                                      'answer': 'c',
                                                                      'Difficulty': 'Moderate',
                                                                      'Explanation': 'Reflection '
                                                                                     'in the '
                                                                                     'XY-plane '
                                                                                     'negates only '
                                                                                     'the '
                                                                                     'z-coordinate, '
                                                                                     'yielding '
                                                                                     '$(2, 3, '
                                                                                     '-4)$.'},
                                                                  {   'question': 'What is the '
                                                                                  'perpendicular '
                                                                                  'distance of '
                                                                                  'point $P(3, 4, '
                                                                                  '5)$ from the '
                                                                                  'X-axis?',
                                                                      'options': [   '3',
                                                                                     '\\sqrt{41}',
                                                                                     '5',
                                                                                     '\\sqrt{34}'],
                                                                      'answer': 'b',
                                                                      'Difficulty': 'Difficult',
                                                                      'Explanation': 'Perpendicular '
                                                                                     'distance '
                                                                                     'from X-axis '
                                                                                     'is '
                                                                                     '$\\sqrt{y^2 '
                                                                                     '+ z^2} = '
                                                                                     '\\sqrt{4^2 + '
                                                                                     '5^2} = '
                                                                                     '\\sqrt{16 + '
                                                                                     '25} = '
                                                                                     '\\sqrt{41}$.'}],
    'Chapter 12: Limits and Derivatives': [   {   'question': 'Evaluate $\\lim_{x \\to 0} '
                                                              '\\frac{\\sin x}{x}$.',
                                                  'options': ['0', '1', 'Undefined', '\\infty'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Standard trigonometric limit '
                                                                 'identity: $\\lim_{x \\to 0} '
                                                                 '\\frac{\\sin x}{x} = 1$.'},
                                              {   'question': 'What is the derivative of $f(x) = '
                                                              'x^n$ with respect to $x$?',
                                                  'options': [   'n x^n',
                                                                 'n x^{n-1}',
                                                                 'x^{n+1} / (n+1)',
                                                                 '(n-1) x^n'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'By the power rule of '
                                                                 'differentiation, '
                                                                 '$\\frac{d}{dx}(x^n) = n '
                                                                 'x^{n-1}$.'},
                                              {   'question': 'Evaluate $\\lim_{x \\to 2} '
                                                              '\\frac{x^2 - 4}{x - 2}$.',
                                                  'options': ['0', '2', '4', 'Undefined'],
                                                  'answer': 'c',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Factor numerator: '
                                                                 '$\\frac{(x-2)(x+2)}{x-2} = x + '
                                                                 '2$. Substituting $x = 2$ gives '
                                                                 '$2 + 2 = 4$.'},
                                              {   'question': 'What is the derivative of $\\tan x$ '
                                                              'with respect to $x$?',
                                                  'options': [   '\\sec x',
                                                                 '\\sec^2 x',
                                                                 '-\\csc^2 x',
                                                                 '\\sec x \\tan x'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Standard derivative rule: '
                                                                 '$\\frac{d}{dx}(\\tan x) = '
                                                                 '\\sec^2 x$.'},
                                              {   'question': 'Evaluate $\\lim_{x \\to 0} \\frac{1 '
                                                              '- \\cos x}{x}$.',
                                                  'options': ['0', '1', '1/2', 'Undefined'],
                                                  'answer': 'a',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': '$\\lim_{x \\to 0} \\frac{1 - '
                                                                 '\\cos x}{x} = \\lim_{x \\to 0} '
                                                                 '\\frac{2\\sin^2(x/2)}{x} = 0$.'},
                                              {   'question': 'Find derivative of $f(x) = \\sin x '
                                                              '\\cdot \\cos x$.',
                                                  'options': [   '\\cos(2x)',
                                                                 '\\sin(2x)',
                                                                 '-\\cos(2x)',
                                                                 '\\cos^2 x + \\sin^2 x'],
                                                  'answer': 'a',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': '$f(x) = \\frac{1}{2}\\sin(2x) '
                                                                 "\\implies f'(x) = "
                                                                 '\\frac{1}{2}(2\\cos(2x)) = '
                                                                 '\\cos(2x)$.'},
                                              {   'question': 'Evaluate $\\lim_{x \\to a} '
                                                              '\\frac{x^n - a^n}{x - a}$.',
                                                  'options': ['n a^n', 'n a^{n-1}', 'a^{n-1}', '0'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Moderate',
                                                  'Explanation': 'Standard limit formula: '
                                                                 '$\\lim_{x \\to a} \\frac{x^n - '
                                                                 'a^n}{x - a} = n a^{n-1}$.'},
                                              {   'question': 'What is derivative of $f(x) = '
                                                              '\\frac{x}{x + 1}$ at $x = 1$?',
                                                  'options': ['1/2', '1/4', '1', '0'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Difficult',
                                                  'Explanation': "By quotient rule: $f'(x) = "
                                                                 '\\frac{(x+1)(1) - x(1)}{(x+1)^2} '
                                                                 '= \\frac{1}{(x+1)^2}$. At $x=1$, '
                                                                 "$f'(1) = \\frac{1}{(1+1)^2} = "
                                                                 '\\frac{1}{4}$.'},
                                              {   'question': 'What is the derivative of a '
                                                              'constant function $c$?',
                                                  'options': ['1', 'c', '0', 'x'],
                                                  'answer': 'c',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'The rate of change of any '
                                                                 'constant value is zero.'},
                                              {   'question': 'Evaluate $\\lim_{x \\to 0} '
                                                              '\\frac{e^x - 1}{x}$.',
                                                  'options': ['0', '1', 'e', 'Undefined'],
                                                  'answer': 'b',
                                                  'Difficulty': 'Easy',
                                                  'Explanation': 'Standard exponential limit '
                                                                 'identity: $\\lim_{x \\to 0} '
                                                                 '\\frac{e^x - 1}{x} = 1$.'}],
    'Chapter 13: Statistics': [   {   'question': 'What is the mean deviation about the mean for '
                                                  'observations $3, 6, 6, 7, 8, 11, 15, 16$ (Mean '
                                                  '= 9)?',
                                      'options': ['3.25', '3.75', '4.0', '2.5'],
                                      'answer': 'b',
                                      'Difficulty': 'Moderate',
                                      'Explanation': 'Deviations $|x_i - 9|$ are $6, 3, 3, 2, 1, '
                                                     '2, 6, 7$. Sum $= 30$. Mean deviation $= 30/8 '
                                                     '= 3.75$.'},
                                  {   'question': 'The square root of variance is called:',
                                      'options': [   'Mean Deviation',
                                                     'Standard Deviation',
                                                     'Range',
                                                     'Coefficient of Variation'],
                                      'answer': 'b',
                                      'Difficulty': 'Easy',
                                      'Explanation': 'By definition, Standard Deviation $\\sigma = '
                                                     '\\sqrt{\\text{Variance}}$.'},
                                  {   'question': 'What is the variance of first $n$ natural '
                                                  'numbers?',
                                      'options': [   '\\frac{n^2 - 1}{12}',
                                                     '\\frac{n^2 + 1}{12}',
                                                     '\\frac{n^2 - 1}{6}',
                                                     '\\frac{n(n+1)}{12}'],
                                      'answer': 'a',
                                      'Difficulty': 'Difficult',
                                      'Explanation': 'Standard statistical result: Variance of '
                                                     'first $n$ natural numbers is $\\sigma^2 = '
                                                     '\\frac{n^2 - 1}{12}$.'},
                                  {   'question': 'If each observation in a data set is multiplied '
                                                  'by 3, what happens to the standard deviation?',
                                      'options': [   'Remains unchanged',
                                                     'Multiplied by 3',
                                                     'Multiplied by 9',
                                                     'Increased by 3'],
                                      'answer': 'b',
                                      'Difficulty': 'Moderate',
                                      'Explanation': 'Multiplying observations by constant $k$ '
                                                     'multiplies standard deviation by $|k|$. Here '
                                                     '$k=3$.'},
                                  {   'question': 'If each observation in a data set is increased '
                                                  'by 5, what happens to the variance?',
                                      'options': [   'Increases by 5',
                                                     'Increases by 25',
                                                     'Remains unchanged',
                                                     'Multiplied by 5'],
                                      'answer': 'c',
                                      'Difficulty': 'Moderate',
                                      'Explanation': 'Variance is independent of change of origin '
                                                     '(adding/subtracting a constant).'},
                                  {   'question': 'The coefficient of variation (C.V.) is defined '
                                                  'as:',
                                      'options': [   '\\frac{\\sigma}{\\bar{x}} \\times 100',
                                                     '\\frac{\\bar{x}}{\\sigma} \\times 100',
                                                     '\\frac{\\sigma^2}{\\bar{x}} \\times 100',
                                                     '\\sigma \\cdot \\bar{x} \\times 100'],
                                      'answer': 'a',
                                      'Difficulty': 'Easy',
                                      'Explanation': 'Coefficient of variation $\\text{C.V.} = '
                                                     '\\frac{\\text{Standard '
                                                     'Deviation}}{\\text{Mean}} \\times 100$.'},
                                  {   'question': 'Between two data series with equal means, the '
                                                  'series with greater standard deviation is:',
                                      'options': [   'More consistent',
                                                     'Less variable',
                                                     'More variable / Less consistent',
                                                     'More accurate'],
                                      'answer': 'c',
                                      'Difficulty': 'Easy',
                                      'Explanation': 'Higher standard deviation indicates greater '
                                                     'spread/variability, meaning less '
                                                     'consistency.'},
                                  {   'question': 'What is the Range of the dataset $\\{12, 25, 7, '
                                                  '33, 41, 18\\}$?',
                                      'options': ['34', '41', '26', '33'],
                                      'answer': 'a',
                                      'Difficulty': 'Easy',
                                      'Explanation': '$\\text{Range} = \\text{Maximum value} - '
                                                     '\\text{Minimum value} = 41 - 7 = 34$.'},
                                  {   'question': 'If variance of a distribution is 16, what is '
                                                  'its standard deviation?',
                                      'options': ['256', '8', '4', '16'],
                                      'answer': 'c',
                                      'Difficulty': 'Easy',
                                      'Explanation': '$\\sigma = \\sqrt{\\text{Variance}} = '
                                                     '\\sqrt{16} = 4$.'},
                                  {   'question': 'What is the algebraic sum of deviations of '
                                                  'observations from their mean?',
                                      'options': [   'Always positive',
                                                     'Always zero',
                                                     'Equal to standard deviation',
                                                     'Equal to variance'],
                                      'answer': 'b',
                                      'Difficulty': 'Easy',
                                      'Explanation': 'A fundamental property of arithmetic mean: '
                                                     '$\\sum (x_i - \\bar{x}) = 0$.'}],
    'Chapter 14: Probability': [   {   'question': 'An experiment has sample space $S = \\{1, 2, '
                                                   '3, 4, 5, 6\\}$. What is the probability of '
                                                   'getting an even prime number in a single roll '
                                                   'of a fair die?',
                                       'options': ['1/6', '1/3', '1/2', '2/3'],
                                       'answer': 'a',
                                       'Difficulty': 'Easy',
                                       'Explanation': 'The only even prime number is $2$. '
                                                      'Favorable outcome = $\\{2\\}$ (1 outcome). '
                                                      'Probability = $1/6$.'},
                                   {   'question': 'If $P(A) = 0.6$, $P(B) = 0.3$, and $P(A \\cap '
                                                   'B) = 0.2$, find $P(A \\cup B)$.',
                                       'options': ['0.7', '0.9', '0.5', '0.8'],
                                       'answer': 'a',
                                       'Difficulty': 'Easy',
                                       'Explanation': '$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) '
                                                      '= 0.6 + 0.3 - 0.2 = 0.7$.'},
                                   {   'question': 'If $A$ and $B$ are mutually exclusive events, '
                                                   'then $P(A \\cap B)$ is equal to:',
                                       'options': ['1', '0', 'P(A)P(B)', 'P(A) + P(B)'],
                                       'answer': 'b',
                                       'Difficulty': 'Easy',
                                       'Explanation': 'Mutually exclusive events cannot happen '
                                                      'together, so $A \\cap B = \\emptyset '
                                                      '\\implies P(A \\cap B) = 0$.'},
                                   {   'question': 'What is the probability of getting at least '
                                                   'one head when two fair coins are tossed '
                                                   'simultaneously?',
                                       'options': ['1/4', '1/2', '3/4', '1'],
                                       'answer': 'c',
                                       'Difficulty': 'Moderate',
                                       'Explanation': 'Sample space $S = \\{HH, HT, TH, TT\\}$. '
                                                      'Favorable outcomes = $\\{HH, HT, TH\\}$ (3 '
                                                      'cases). Probability = $3/4$.'},
                                   {   'question': "If $E'$ is the complement of event $E$, then "
                                                   "$P(E) + P(E')$ is equal to:",
                                       'options': ['0', '0.5', '1', '2'],
                                       'answer': 'c',
                                       'Difficulty': 'Easy',
                                       'Explanation': 'The sum of probabilities of an event and '
                                                      'its complementary event is always equal to '
                                                      '$1$.'},
                                   {   'question': 'Two dice are thrown simultaneously. What is '
                                                   'the probability of getting a total sum of 10?',
                                       'options': ['1/12', '1/6', '1/9', '5/36'],
                                       'answer': 'a',
                                       'Difficulty': 'Moderate',
                                       'Explanation': 'Favorable outcomes for sum 10: $\\{(4,6), '
                                                      '(5,5), (6,4)\\}$ (3 cases out of 36). '
                                                      'Probability = $3/36 = 1/12$.'},
                                   {   'question': 'A card is drawn from a well-shuffled deck of '
                                                   '52 playing cards. What is the probability of '
                                                   'drawing a red face card?',
                                       'options': ['3/26', '3/13', '1/26', '1/13'],
                                       'answer': 'a',
                                       'Difficulty': 'Moderate',
                                       'Explanation': 'There are 6 red face cards (3 Hearts + 3 '
                                                      'Diamonds). Probability = $6/52 = 3/26$.'},
                                   {   'question': 'If $A$ and $B$ are two exhaustive events of a '
                                                   'sample space $S$, then:',
                                       'options': [   'P(A \\cup B) = 1',
                                                      'P(A \\cap B) = 0',
                                                      'P(A) + P(B) = 1',
                                                      'P(A) = P(B)'],
                                       'answer': 'a',
                                       'Difficulty': 'Moderate',
                                       'Explanation': 'Exhaustive events cover the entire sample '
                                                      'space, meaning $A \\cup B = S \\implies P(A '
                                                      '\\cup B) = 1$.'},
                                   {   'question': 'What is the probability that a non-leap year '
                                                   'selected at random contains 53 Sundays?',
                                       'options': ['1/7', '2/7', '3/7', '53/365'],
                                       'answer': 'a',
                                       'Difficulty': 'Difficult',
                                       'Explanation': 'A non-leap year has 365 days = 52 weeks + 1 '
                                                      'extra day. The 1 extra day can be any day '
                                                      'of the week (7 options). Probability of '
                                                      'Sunday = $1/7$.'},
                                   {   'question': "If $P(A) = 2/5$ and $P(B') = 1/3$, and $A, B$ "
                                                   'are mutually exclusive, find $P(A \\cup B)$.',
                                       'options': ['11/15', '1/15', '4/15', '2/15'],
                                       'answer': 'a',
                                       'Difficulty': 'Difficult',
                                       'Explanation': '$P(B) = 1 - 1/3 = 2/3$. For mutually '
                                                      'exclusive events, $P(A \\cup B) = P(A) + '
                                                      'P(B) = 2/5 + 2/3 = \\frac{6 + 10}{15} = '
                                                      '16/15$.'}]}