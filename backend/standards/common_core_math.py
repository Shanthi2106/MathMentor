"""
USA Common Core State Standards for Mathematics, Grades 1-12.
Used to align tutor responses and to drive grade/topic selection in the UI.
Reference: https://www.corestandards.org/Math/
"""

COMMON_CORE_MATH_BY_GRADE = {
    1: {
        "grade": 1,
        "domains": [
            {
                "id": "OA",
                "name": "Operations & Algebraic Thinking",
                "topics": [
                    "Represent and solve problems involving addition and subtraction",
                    "Understand and apply properties of operations",
                    "Add and subtract within 20",
                    "Work with addition and subtraction equations",
                ],
            },
            {
                "id": "NBT",
                "name": "Number & Operations in Base Ten",
                "topics": [
                    "Extend the counting sequence to 120",
                    "Understand place value (tens and ones)",
                    "Use place value to add and subtract",
                ],
            },
            {
                "id": "MD",
                "name": "Measurement & Data",
                "topics": [
                    "Measure lengths indirectly and by iterating length units",
                    "Tell and write time (hours and half-hours)",
                    "Represent and interpret data",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Reason about shapes and their attributes",
                    "Compose two-dimensional or three-dimensional shapes",
                ],
            },
        ],
    },
    2: {
        "grade": 2,
        "domains": [
            {
                "id": "OA",
                "name": "Operations & Algebraic Thinking",
                "topics": [
                    "Represent and solve problems (addition and subtraction)",
                    "Add and subtract within 20 (fluency)",
                    "Work with equal groups (foundations for multiplication)",
                ],
            },
            {
                "id": "NBT",
                "name": "Number & Operations in Base Ten",
                "topics": [
                    "Understand place value (hundreds, tens, ones)",
                    "Use place value understanding to add and subtract",
                    "Use mental strategies",
                ],
            },
            {
                "id": "MD",
                "name": "Measurement & Data",
                "topics": [
                    "Measure and estimate lengths",
                    "Relate addition and subtraction to length",
                    "Work with time and money",
                    "Represent and interpret data",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Reason about shapes and their attributes",
                    "Partition rectangles and circles into equal shares",
                ],
            },
        ],
    },
    3: {
        "grade": 3,
        "domains": [
            {
                "id": "OA",
                "name": "Operations & Algebraic Thinking",
                "topics": [
                    "Represent and solve multiplication and division problems",
                    "Understand properties of multiplication",
                    "Multiply and divide within 100",
                    "Solve two-step word problems",
                    "Identify arithmetic patterns",
                ],
            },
            {
                "id": "NBT",
                "name": "Number & Operations in Base Ten",
                "topics": [
                    "Use place value to round and fluently add/subtract within 1000",
                    "Multiply one-digit by multiples of 10",
                ],
            },
            {
                "id": "NF",
                "name": "Number & Operations—Fractions",
                "topics": [
                    "Develop understanding of fractions as numbers",
                    "Unit fractions and fractions on a number line",
                ],
            },
            {
                "id": "MD",
                "name": "Measurement & Data",
                "topics": [
                    "Solve problems involving measurement and estimation",
                    "Represent and interpret data",
                    "Geometric measurement: area and perimeter",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Reason with shapes and their attributes",
                    "Partition shapes into parts with equal areas",
                ],
            },
        ],
    },
    4: {
        "grade": 4,
        "domains": [
            {
                "id": "OA",
                "name": "Operations & Algebraic Thinking",
                "topics": [
                    "Use the four operations with whole numbers",
                    "Factors and multiples",
                    "Generate and analyze patterns",
                ],
            },
            {
                "id": "NBT",
                "name": "Number & Operations in Base Ten",
                "topics": [
                    "Generalize place value to multi-digit whole numbers",
                    "Fluently add and subtract multi-digit numbers",
                    "Multiply and divide (multi-digit by one-digit)",
                ],
            },
            {
                "id": "NF",
                "name": "Number & Operations—Fractions",
                "topics": [
                    "Equivalent fractions and comparing fractions",
                    "Build fractions from unit fractions",
                    "Decimal notation for fractions",
                    "Compare decimals to hundredths",
                ],
            },
            {
                "id": "MD",
                "name": "Measurement & Data",
                "topics": [
                    "Solve problems involving measurement and conversion",
                    "Represent and interpret data",
                    "Geometric measurement: area and perimeter",
                    "Angles and angle measure",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Draw and identify lines, angles, and shapes",
                    "Classify shapes by lines and angles",
                ],
            },
        ],
    },
    5: {
        "grade": 5,
        "domains": [
            {
                "id": "OA",
                "name": "Operations & Algebraic Thinking",
                "topics": [
                    "Write and interpret numerical expressions",
                    "Analyze patterns and relationships",
                ],
            },
            {
                "id": "NBT",
                "name": "Number & Operations in Base Ten",
                "topics": [
                    "Understand the place value system (decimals)",
                    "Perform operations with multi-digit whole numbers and decimals",
                ],
            },
            {
                "id": "NF",
                "name": "Number & Operations—Fractions",
                "topics": [
                    "Use equivalent fractions and add/subtract fractions",
                    "Apply understanding of multiplication to multiply fractions",
                    "Divide fractions and solve real-world problems",
                ],
            },
            {
                "id": "MD",
                "name": "Measurement & Data",
                "topics": [
                    "Convert measurement units",
                    "Represent and interpret data",
                    "Geometric measurement: volume",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Graph points on the coordinate plane",
                    "Classify two-dimensional figures into categories",
                ],
            },
        ],
    },
    6: {
        "grade": 6,
        "domains": [
            {
                "id": "RP",
                "name": "Ratios & Proportional Relationships",
                "topics": [
                    "Understand ratio concepts and use ratio language",
                    "Understand unit rate and solve problems",
                ],
            },
            {
                "id": "NS",
                "name": "The Number System",
                "topics": [
                    "Divide fractions by fractions",
                    "Fluently add, subtract, multiply, divide multi-digit decimals",
                    "Find common factors and multiples",
                    "Apply number theory to positive rational numbers",
                ],
            },
            {
                "id": "EE",
                "name": "Expressions & Equations",
                "topics": [
                    "Write and evaluate expressions with variables",
                    "Reason about and solve one-variable equations and inequalities",
                    "Represent and analyze quantitative relationships",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Solve real-world area, surface area, and volume problems",
                ],
            },
            {
                "id": "SP",
                "name": "Statistics & Probability",
                "topics": [
                    "Develop understanding of statistical variability",
                    "Summarize and describe distributions",
                ],
            },
        ],
    },
    7: {
        "grade": 7,
        "domains": [
            {
                "id": "RP",
                "name": "Ratios & Proportional Relationships",
                "topics": [
                    "Compute unit rates with complex fractions",
                    "Recognize and represent proportional relationships",
                ],
            },
            {
                "id": "NS",
                "name": "The Number System",
                "topics": [
                    "Add, subtract, multiply, divide rational numbers",
                    "Apply properties of operations",
                ],
            },
            {
                "id": "EE",
                "name": "Expressions & Equations",
                "topics": [
                    "Use properties to add, subtract, factor, expand expressions",
                    "Solve multi-step equations and inequalities",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Draw, construct, describe geometric figures",
                    "Solve problems involving scale drawings and 2D/3D figures",
                    "Circles: area and circumference",
                ],
            },
            {
                "id": "SP",
                "name": "Statistics & Probability",
                "topics": [
                    "Use random sampling and draw inferences",
                    "Investigate chance processes and develop probability models",
                ],
            },
        ],
    },
    8: {
        "grade": 8,
        "domains": [
            {
                "id": "NS",
                "name": "The Number System",
                "topics": [
                    "Know that there are numbers that are not rational (irrational)",
                    "Approximate irrational numbers and use them in expressions",
                ],
            },
            {
                "id": "EE",
                "name": "Expressions & Equations",
                "topics": [
                    "Work with radicals and integer exponents",
                    "Understand proportional relationships and lines",
                    "Analyze and solve linear equations and pairs of linear equations",
                ],
            },
            {
                "id": "F",
                "name": "Functions",
                "topics": [
                    "Define, evaluate, and compare functions",
                    "Use functions to model relationships between quantities",
                ],
            },
            {
                "id": "G",
                "name": "Geometry",
                "topics": [
                    "Understand congruence and similarity",
                    "Understand and apply the Pythagorean theorem",
                    "Solve real-world volume problems (cones, cylinders, spheres)",
                ],
            },
            {
                "id": "SP",
                "name": "Statistics & Probability",
                "topics": [
                    "Investigate patterns of association in bivariate data",
                ],
            },
        ],
    },
    9: {
        "grade": 9,
        "domains": [
            {
                "id": "N-RN",
                "name": "Number & Quantity – Real Number System",
                "topics": [
                    "Extend properties of exponents to rational exponents",
                    "Use properties of rational and irrational numbers",
                ],
            },
            {
                "id": "A-SSE",
                "name": "Algebra – Seeing Structure in Expressions",
                "topics": [
                    "Interpret expressions and parts of expressions",
                    "Write expressions in equivalent forms",
                ],
            },
            {
                "id": "A-APR",
                "name": "Algebra – Arithmetic with Polynomials",
                "topics": [
                    "Perform arithmetic on polynomials",
                ],
            },
            {
                "id": "A-CED",
                "name": "Algebra – Creating Equations",
                "topics": [
                    "Create equations and inequalities in one variable",
                ],
            },
            {
                "id": "A-REI",
                "name": "Algebra – Reasoning with Equations & Inequalities",
                "topics": [
                    "Solve linear equations and inequalities",
                    "Solve systems of linear equations",
                ],
            },
            {
                "id": "F-IF",
                "name": "Functions – Interpreting Functions",
                "topics": [
                    "Understand function notation and key features of graphs",
                ],
            },
            {
                "id": "G-CO",
                "name": "Geometry – Congruence",
                "topics": [
                    "Experiment with rigid motions and congruence",
                ],
            },
        ],
    },
    10: {
        "grade": 10,
        "domains": [
            {
                "id": "A-SSE",
                "name": "Algebra – Seeing Structure in Expressions",
                "topics": [
                    "Interpret and write expressions (quadratics)",
                ],
            },
            {
                "id": "A-APR",
                "name": "Algebra – Arithmetic with Polynomials",
                "topics": [
                    "Understand the relationship between zeros and factors of polynomials",
                ],
            },
            {
                "id": "A-CED",
                "name": "Algebra – Creating Equations",
                "topics": [
                    "Create equations in two or more variables",
                ],
            },
            {
                "id": "A-REI",
                "name": "Algebra – Reasoning with Equations & Inequalities",
                "topics": [
                    "Solve quadratic equations and systems (including nonlinear)",
                ],
            },
            {
                "id": "F-IF",
                "name": "Functions – Interpreting Functions",
                "topics": [
                    "Interpret functions that arise in applications (linear, quadratic, exponential)",
                ],
            },
            {
                "id": "F-BF",
                "name": "Functions – Building Functions",
                "topics": [
                    "Build new functions from existing functions",
                ],
            },
            {
                "id": "G-CO",
                "name": "Geometry – Congruence",
                "topics": [
                    "Prove geometric theorems (lines, angles, triangles, parallelograms)",
                ],
            },
            {
                "id": "G-SRT",
                "name": "Geometry – Similarity, Right Triangles, Trigonometry",
                "topics": [
                    "Understand similarity and trigonometric ratios",
                ],
            },
        ],
    },
    11: {
        "grade": 11,
        "domains": [
            {
                "id": "N-Q",
                "name": "Number & Quantity – Quantities",
                "topics": [
                    "Use units to guide problem solving",
                ],
            },
            {
                "id": "A-SSE",
                "name": "Algebra – Seeing Structure in Expressions",
                "topics": [
                    "Write equivalent expressions (exponential and logarithmic)",
                ],
            },
            {
                "id": "F-IF",
                "name": "Functions – Interpreting Functions",
                "topics": [
                    "Interpret key features of graphs (including periodic)",
                ],
            },
            {
                "id": "F-BF",
                "name": "Functions – Building Functions",
                "topics": [
                    "Build functions (including exponential and trigonometric)",
                ],
            },
            {
                "id": "F-LE",
                "name": "Functions – Linear, Quadratic, & Exponential Models",
                "topics": [
                    "Construct and compare linear, quadratic, exponential models",
                ],
            },
            {
                "id": "F-TF",
                "name": "Functions – Trigonometric Functions",
                "topics": [
                    "Extend the domain of trigonometric functions using the unit circle",
                    "Model periodic phenomena with trigonometric functions",
                ],
            },
            {
                "id": "G-SRT",
                "name": "Geometry – Similarity, Right Triangles, Trigonometry",
                "topics": [
                    "Apply trigonometry to general triangles (Law of Sines, Law of Cosines)",
                ],
            },
            {
                "id": "G-C",
                "name": "Geometry – Circles",
                "topics": [
                    "Understand and apply theorems about circles",
                ],
            },
            {
                "id": "G-GPE",
                "name": "Geometry – Expressing Geometric Properties with Equations",
                "topics": [
                    "Translate between geometric description and equation (conic sections)",
                ],
            },
        ],
    },
    12: {
        "grade": 12,
        "domains": [
            {
                "id": "N-CN",
                "name": "Number & Quantity – Complex Numbers",
                "topics": [
                    "Perform arithmetic with complex numbers",
                ],
            },
            {
                "id": "F-TF",
                "name": "Functions – Trigonometric Functions",
                "topics": [
                    "Prove and use trigonometric identities",
                ],
            },
            {
                "id": "G-GMD",
                "name": "Geometry – Geometric Measurement & Dimension",
                "topics": [
                    "Explain volume formulas and use them",
                ],
            },
            {
                "id": "G-MG",
                "name": "Geometry – Modeling with Geometry",
                "topics": [
                    "Apply geometric concepts in modeling situations",
                ],
            },
            {
                "id": "S-ID",
                "name": "Statistics & Probability – Interpreting Categorical & Quantitative Data",
                "topics": [
                    "Summarize, represent, and interpret data",
                ],
            },
            {
                "id": "S-IC",
                "name": "Statistics & Probability – Making Inferences & Justifying Conclusions",
                "topics": [
                    "Understand and evaluate random processes",
                    "Make inferences and justify conclusions",
                ],
            },
            {
                "id": "S-CP",
                "name": "Statistics & Probability – Conditional Probability & Rules",
                "topics": [
                    "Understand independence and conditional probability",
                    "Use the rules of probability to compute probabilities",
                ],
            },
        ],
    },
}

# Mathematical practices (same for all grades, from Common Core)
STANDARDS_FOR_MATHEMATICAL_PRACTICE = [
    "Make sense of problems and persevere in solving them.",
    "Reason abstractly and quantitatively.",
    "Construct viable arguments and critique the reasoning of others.",
    "Model with mathematics.",
    "Use appropriate tools strategically.",
    "Attend to precision.",
    "Look for and make use of structure.",
    "Look for and express regularity in repeated reasoning.",
]
