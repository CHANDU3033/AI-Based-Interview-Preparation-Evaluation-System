import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)

"""
Curated Question Bank - 300 Official Structured Questions across 5 Major Roles & 3 Difficulty Levels
(Beginner, Intermediate, Advanced - 20 questions each per role)
"""

JOB_ROLES = [
    {
        "role_name": "Python Developer",
        "description": "Build applications, web APIs, and automation scripts using Python, Django, FastAPI, and data structures."
    },
    {
        "role_name": "Java Developer",
        "description": "Develop enterprise applications, microservices, and high-performance backend systems using Java, Spring Boot, and JVM."
    },
    {
        "role_name": "Software Developer",
        "description": "Build software systems using modern C++, JavaScript, Web APIs, and core algorithms."
    },
    {
        "role_name": "Data Analyst & AI Engineer",
        "description": "Analyze data, perform statistical modeling, and build ML models using Python, SQL, Pandas, and ML algorithms."
    },
    {
        "role_name": "SQL & Database Engineer",
        "description": "Design, optimize, and manage relational database schemas, complex queries, transactions, and indexing."
    }
]

QUESTION_BANK = [
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is Python?",
        "expected_answer": "Clear technical explanation of python? covering key principles and practical usage.",
        "expected_concepts": [
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are the main features of Python?",
        "expected_answer": "Clear technical explanation of what are the main features of python? covering key principles and practical usage.",
        "expected_concepts": [
            "main",
            "features",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are Python's built-in data types?",
        "expected_answer": "Clear technical explanation of what are python's built-in data types? covering key principles and practical usage.",
        "expected_concepts": [
            "Python's",
            "built-in",
            "data",
            "types"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the difference between a list and a tuple?",
        "expected_answer": "Clear technical explanation of the difference between a list and a tuple? covering key principles and practical usage.",
        "expected_concepts": [
            "list",
            "tuple"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a dictionary in Python?",
        "expected_answer": "Clear technical explanation of a dictionary in python? covering key principles and practical usage.",
        "expected_concepts": [
            "dictionary",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a set?",
        "expected_answer": "Clear technical explanation of a set? covering key principles and practical usage.",
        "expected_concepts": [
            "set"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a variable in Python?",
        "expected_answer": "Clear technical explanation of a variable in python? covering key principles and practical usage.",
        "expected_concepts": [
            "variable",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is type casting?",
        "expected_answer": "Clear technical explanation of type casting? covering key principles and practical usage.",
        "expected_concepts": [
            "type",
            "casting"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the difference between input() and print()?",
        "expected_answer": "Clear technical explanation of the difference between input() and print()? covering key principles and practical usage.",
        "expected_concepts": [
            "input",
            "print"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are conditional statements?",
        "expected_answer": "Clear technical explanation of what are conditional statements? covering key principles and practical usage.",
        "expected_concepts": [
            "conditional",
            "statements"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are loops in Python?",
        "expected_answer": "Clear technical explanation of what are loops in python? covering key principles and practical usage.",
        "expected_concepts": [
            "loops",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "Difference between for and while loops?",
        "expected_answer": "Clear technical explanation of difference between for and while loops? covering key principles and practical usage.",
        "expected_concepts": [
            "while",
            "loops"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a function?",
        "expected_answer": "Clear technical explanation of a function? covering key principles and practical usage.",
        "expected_concepts": [
            "function"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are function parameters and arguments?",
        "expected_answer": "Clear technical explanation of what are function parameters and arguments? covering key principles and practical usage.",
        "expected_concepts": [
            "function",
            "parameters",
            "arguments"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the difference between return and print()?",
        "expected_answer": "Clear technical explanation of the difference between return and print()? covering key principles and practical usage.",
        "expected_concepts": [
            "return",
            "print"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a string in Python?",
        "expected_answer": "Clear technical explanation of a string in python? covering key principles and practical usage.",
        "expected_concepts": [
            "string",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "How do you reverse a string?",
        "expected_answer": "Clear technical explanation of how do you reverse a string? covering key principles and practical usage.",
        "expected_concepts": [
            "reverse",
            "string"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is list slicing?",
        "expected_answer": "Clear technical explanation of list slicing? covering key principles and practical usage.",
        "expected_concepts": [
            "list",
            "slicing"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is exception handling?",
        "expected_answer": "Clear technical explanation of exception handling? covering key principles and practical usage.",
        "expected_concepts": [
            "exception",
            "handling"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the purpose of import in Python?",
        "expected_answer": "Clear technical explanation of the purpose of import in python? covering key principles and practical usage.",
        "expected_concepts": [
            "purpose",
            "import",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain mutable and immutable objects.",
        "expected_answer": "Clear technical explanation of mutable and immutable objects. covering key principles and practical usage.",
        "expected_concepts": [
            "mutable",
            "immutable",
            "objects"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between == and is.",
        "expected_answer": "Clear technical explanation of difference between == and is. covering key principles and practical usage.",
        "expected_concepts": []
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain shallow copy and deep copy.",
        "expected_answer": "Clear technical explanation of shallow copy and deep copy. covering key principles and practical usage.",
        "expected_concepts": [
            "shallow",
            "copy",
            "deep",
            "copy"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are *args and **kwargs?",
        "expected_answer": "Clear technical explanation of what are *args and **kwargs? covering key principles and practical usage.",
        "expected_concepts": [
            "*args",
            "**kwargs"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is list comprehension?",
        "expected_answer": "Clear technical explanation of list comprehension? covering key principles and practical usage.",
        "expected_concepts": [
            "list",
            "comprehension"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain lambda functions.",
        "expected_answer": "Clear technical explanation of lambda functions. covering key principles and practical usage.",
        "expected_concepts": [
            "lambda",
            "functions"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain map(), filter(), and reduce().",
        "expected_answer": "Clear technical explanation of map(), filter(), and reduce(). covering key principles and practical usage.",
        "expected_concepts": [
            "map",
            "filter",
            "reduce"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are iterators and generators?",
        "expected_answer": "Clear technical explanation of what are iterators and generators? covering key principles and practical usage.",
        "expected_concepts": [
            "iterators",
            "generators"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is the purpose of yield?",
        "expected_answer": "Clear technical explanation of the purpose of yield? covering key principles and practical usage.",
        "expected_concepts": [
            "purpose",
            "yield"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain try, except, else, and finally.",
        "expected_answer": "Clear technical explanation of try, except, else, and finally. covering key principles and practical usage.",
        "expected_concepts": [
            "try",
            "except",
            "else",
            "finally"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are modules and packages?",
        "expected_answer": "Clear technical explanation of what are modules and packages? covering key principles and practical usage.",
        "expected_concepts": [
            "modules",
            "packages"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain OOP concepts in Python.",
        "expected_answer": "Clear technical explanation of oop concepts in python. covering key principles and practical usage.",
        "expected_concepts": [
            "concepts",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is inheritance?",
        "expected_answer": "Clear technical explanation of inheritance? covering key principles and practical usage.",
        "expected_concepts": [
            "inheritance"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is polymorphism?",
        "expected_answer": "Clear technical explanation of polymorphism? covering key principles and practical usage.",
        "expected_concepts": [
            "polymorphism"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is encapsulation?",
        "expected_answer": "Clear technical explanation of encapsulation? covering key principles and practical usage.",
        "expected_concepts": [
            "encapsulation"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is abstraction?",
        "expected_answer": "Clear technical explanation of abstraction? covering key principles and practical usage.",
        "expected_concepts": [
            "abstraction"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are decorators?",
        "expected_answer": "Clear technical explanation of what are decorators? covering key principles and practical usage.",
        "expected_concepts": [
            "decorators"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between class and instance variables.",
        "expected_answer": "Clear technical explanation of difference between class and instance variables. covering key principles and practical usage.",
        "expected_concepts": [
            "class",
            "instance",
            "variables"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain @staticmethod and @classmethod.",
        "expected_answer": "Clear technical explanation of @staticmethod and @classmethod. covering key principles and practical usage.",
        "expected_concepts": [
            "@staticmethod",
            "@classmethod"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How can you optimize Python code?",
        "expected_answer": "Clear technical explanation of how can you optimize python code? covering key principles and practical usage.",
        "expected_concepts": [
            "optimize",
            "Python",
            "code"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Python's memory management.",
        "expected_answer": "Clear technical explanation of python's memory management. covering key principles and practical usage.",
        "expected_concepts": [
            "Python's",
            "memory",
            "management"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is garbage collection in Python?",
        "expected_answer": "Clear technical explanation of garbage collection in python? covering key principles and practical usage.",
        "expected_concepts": [
            "garbage",
            "collection",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Python's Global Interpreter Lock (GIL).",
        "expected_answer": "Clear technical explanation of python's global interpreter lock (gil). covering key principles and practical usage.",
        "expected_concepts": [
            "Python's",
            "Global",
            "Interpreter",
            "Lock"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How does Python handle multithreading?",
        "expected_answer": "Clear technical explanation of how does python handle multithreading? covering key principles and practical usage.",
        "expected_concepts": [
            "Python",
            "handle",
            "multithreading"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Difference between multiprocessing and multithreading.",
        "expected_answer": "Clear technical explanation of difference between multiprocessing and multithreading. covering key principles and practical usage.",
        "expected_concepts": [
            "multiprocessing",
            "multithreading"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain asynchronous programming using async and await.",
        "expected_answer": "Clear technical explanation of asynchronous programming using async and await. covering key principles and practical usage.",
        "expected_concepts": [
            "asynchronous",
            "programming",
            "async",
            "await"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How do decorators work internally?",
        "expected_answer": "Clear technical explanation of how do decorators work internally? covering key principles and practical usage.",
        "expected_concepts": [
            "decorators",
            "work",
            "internally"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are context managers?",
        "expected_answer": "Clear technical explanation of what are context managers? covering key principles and practical usage.",
        "expected_concepts": [
            "context",
            "managers"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain the with statement.",
        "expected_answer": "Clear technical explanation of the with statement. covering key principles and practical usage.",
        "expected_concepts": [
            "statement"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are metaclasses?",
        "expected_answer": "Clear technical explanation of what are metaclasses? covering key principles and practical usage.",
        "expected_concepts": [
            "metaclasses"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain method resolution order (MRO).",
        "expected_answer": "Clear technical explanation of method resolution order (mro). covering key principles and practical usage.",
        "expected_concepts": [
            "method",
            "resolution",
            "order",
            "MRO"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are magic/dunder methods?",
        "expected_answer": "Clear technical explanation of what are magic/dunder methods? covering key principles and practical usage.",
        "expected_concepts": [
            "magic/dunder",
            "methods"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain __init__, __str__, and __repr__.",
        "expected_answer": "Clear technical explanation of __init__, __str__, and __repr__. covering key principles and practical usage.",
        "expected_concepts": [
            "__init__",
            "__str__",
            "__repr__"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How does Python dictionary hashing work?",
        "expected_answer": "Clear technical explanation of how does python dictionary hashing work? covering key principles and practical usage.",
        "expected_concepts": [
            "Python",
            "dictionary",
            "hashing",
            "work"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you optimize memory usage in Python?",
        "expected_answer": "Clear technical explanation of how would you optimize memory usage in python? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "optimize",
            "memory",
            "usage"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you debug a memory leak?",
        "expected_answer": "Clear technical explanation of how would you debug a memory leak? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "debug",
            "memory",
            "leak"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you design a scalable Python application?",
        "expected_answer": "Clear technical explanation of how would you design a scalable python application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "design",
            "scalable",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is dependency management in Python?",
        "expected_answer": "Clear technical explanation of dependency management in python? covering key principles and practical usage.",
        "expected_concepts": [
            "dependency",
            "management",
            "Python"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you improve the performance of a large Python application?",
        "expected_answer": "Clear technical explanation of how would you improve the performance of a large python application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "improve",
            "performance",
            "large"
        ]
    },
    {
        "role": "Python Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain how you would structure a production-level Python project.",
        "expected_answer": "Clear technical explanation of how you would structure a production-level python project. covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "structure",
            "production-level",
            "Python"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is Java?",
        "expected_answer": "Clear technical explanation of java? covering key principles and practical usage.",
        "expected_concepts": [
            "Java"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are the features of Java?",
        "expected_answer": "Clear technical explanation of what are the features of java? covering key principles and practical usage.",
        "expected_concepts": [
            "features",
            "Java"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "Why is Java platform independent?",
        "expected_answer": "Clear technical explanation of why is java platform independent? covering key principles and practical usage.",
        "expected_concepts": [
            "Java",
            "platform",
            "independent"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is JVM?",
        "expected_answer": "Clear technical explanation of jvm? covering key principles and practical usage.",
        "expected_concepts": [
            "JVM"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is JDK?",
        "expected_answer": "Clear technical explanation of jdk? covering key principles and practical usage.",
        "expected_concepts": [
            "JDK"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is JRE?",
        "expected_answer": "Clear technical explanation of jre? covering key principles and practical usage.",
        "expected_concepts": [
            "JRE"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a class?",
        "expected_answer": "Clear technical explanation of a class? covering key principles and practical usage.",
        "expected_concepts": [
            "class"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is an object?",
        "expected_answer": "Clear technical explanation of an object? covering key principles and practical usage.",
        "expected_concepts": [
            "object"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a constructor?",
        "expected_answer": "Clear technical explanation of a constructor? covering key principles and practical usage.",
        "expected_concepts": [
            "constructor"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is inheritance?",
        "expected_answer": "Clear technical explanation of inheritance? covering key principles and practical usage.",
        "expected_concepts": [
            "inheritance"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is polymorphism?",
        "expected_answer": "Clear technical explanation of polymorphism? covering key principles and practical usage.",
        "expected_concepts": [
            "polymorphism"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is encapsulation?",
        "expected_answer": "Clear technical explanation of encapsulation? covering key principles and practical usage.",
        "expected_concepts": [
            "encapsulation"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is abstraction?",
        "expected_answer": "Clear technical explanation of abstraction? covering key principles and practical usage.",
        "expected_concepts": [
            "abstraction"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is method overloading?",
        "expected_answer": "Clear technical explanation of method overloading? covering key principles and practical usage.",
        "expected_concepts": [
            "method",
            "overloading"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is method overriding?",
        "expected_answer": "Clear technical explanation of method overriding? covering key principles and practical usage.",
        "expected_concepts": [
            "method",
            "overriding"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the this keyword?",
        "expected_answer": "Clear technical explanation of the this keyword? covering key principles and practical usage.",
        "expected_concepts": [
            "this",
            "keyword"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the super keyword?",
        "expected_answer": "Clear technical explanation of the super keyword? covering key principles and practical usage.",
        "expected_concepts": [
            "super",
            "keyword"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is an interface?",
        "expected_answer": "Clear technical explanation of an interface? covering key principles and practical usage.",
        "expected_concepts": [
            "interface"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is an abstract class?",
        "expected_answer": "Clear technical explanation of an abstract class? covering key principles and practical usage.",
        "expected_concepts": [
            "abstract",
            "class"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is exception handling?",
        "expected_answer": "Clear technical explanation of exception handling? covering key principles and practical usage.",
        "expected_concepts": [
            "exception",
            "handling"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between == and .equals().",
        "expected_answer": "Clear technical explanation of difference between == and .equals(). covering key principles and practical usage.",
        "expected_concepts": [
            "equals"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain checked and unchecked exceptions.",
        "expected_answer": "Clear technical explanation of checked and unchecked exceptions. covering key principles and practical usage.",
        "expected_concepts": [
            "checked",
            "unchecked",
            "exceptions"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain final, finally, and finalize().",
        "expected_answer": "Clear technical explanation of final, finally, and finalize(). covering key principles and practical usage.",
        "expected_concepts": [
            "final",
            "finally",
            "finalize"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain ArrayList and LinkedList.",
        "expected_answer": "Clear technical explanation of arraylist and linkedlist. covering key principles and practical usage.",
        "expected_concepts": [
            "ArrayList",
            "LinkedList"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between HashMap and HashSet.",
        "expected_answer": "Clear technical explanation of difference between hashmap and hashset. covering key principles and practical usage.",
        "expected_concepts": [
            "HashMap",
            "HashSet"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How does HashMap work?",
        "expected_answer": "Clear technical explanation of how does hashmap work? covering key principles and practical usage.",
        "expected_concepts": [
            "HashMap",
            "work"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is multithreading?",
        "expected_answer": "Clear technical explanation of multithreading? covering key principles and practical usage.",
        "expected_concepts": [
            "multithreading"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a thread?",
        "expected_answer": "Clear technical explanation of a thread? covering key principles and practical usage.",
        "expected_concepts": [
            "thread"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is synchronization?",
        "expected_answer": "Clear technical explanation of synchronization? covering key principles and practical usage.",
        "expected_concepts": [
            "synchronization"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is garbage collection?",
        "expected_answer": "Clear technical explanation of garbage collection? covering key principles and practical usage.",
        "expected_concepts": [
            "garbage",
            "collection"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are Java Collections?",
        "expected_answer": "Clear technical explanation of what are java collections? covering key principles and practical usage.",
        "expected_concepts": [
            "Java",
            "Collections"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is an Iterator?",
        "expected_answer": "Clear technical explanation of an iterator? covering key principles and practical usage.",
        "expected_concepts": [
            "Iterator"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are Generics?",
        "expected_answer": "Clear technical explanation of what are generics? covering key principles and practical usage.",
        "expected_concepts": [
            "Generics"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is the difference between String, StringBuilder, and StringBuffer?",
        "expected_answer": "Clear technical explanation of the difference between string, stringbuilder, and stringbuffer? covering key principles and practical usage.",
        "expected_concepts": [
            "String",
            "StringBuilder",
            "StringBuffer"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is an immutable object?",
        "expected_answer": "Clear technical explanation of an immutable object? covering key principles and practical usage.",
        "expected_concepts": [
            "immutable",
            "object"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is an enum?",
        "expected_answer": "Clear technical explanation of an enum? covering key principles and practical usage.",
        "expected_concepts": [
            "enum"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are lambda expressions?",
        "expected_answer": "Clear technical explanation of what are lambda expressions? covering key principles and practical usage.",
        "expected_concepts": [
            "lambda",
            "expressions"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are functional interfaces?",
        "expected_answer": "Clear technical explanation of what are functional interfaces? covering key principles and practical usage.",
        "expected_concepts": [
            "functional",
            "interfaces"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are Java Streams?",
        "expected_answer": "Clear technical explanation of what are java streams? covering key principles and practical usage.",
        "expected_concepts": [
            "Java",
            "Streams"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is the difference between Comparable and Comparator?",
        "expected_answer": "Clear technical explanation of the difference between comparable and comparator? covering key principles and practical usage.",
        "expected_concepts": [
            "Comparable",
            "Comparator"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain JVM architecture.",
        "expected_answer": "Clear technical explanation of jvm architecture. covering key principles and practical usage.",
        "expected_concepts": [
            "architecture"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Java memory management.",
        "expected_answer": "Clear technical explanation of java memory management. covering key principles and practical usage.",
        "expected_concepts": [
            "Java",
            "memory",
            "management"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Heap and Stack memory.",
        "expected_answer": "Clear technical explanation of heap and stack memory. covering key principles and practical usage.",
        "expected_concepts": [
            "Heap",
            "Stack",
            "memory"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain garbage collector algorithms.",
        "expected_answer": "Clear technical explanation of garbage collector algorithms. covering key principles and practical usage.",
        "expected_concepts": [
            "garbage",
            "collector",
            "algorithms"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Java concurrency.",
        "expected_answer": "Clear technical explanation of java concurrency. covering key principles and practical usage.",
        "expected_concepts": [
            "Java",
            "concurrency"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is ExecutorService?",
        "expected_answer": "Clear technical explanation of executorservice? covering key principles and practical usage.",
        "expected_concepts": [
            "ExecutorService"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is a thread pool?",
        "expected_answer": "Clear technical explanation of a thread pool? covering key principles and practical usage.",
        "expected_concepts": [
            "thread",
            "pool"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is deadlock?",
        "expected_answer": "Clear technical explanation of deadlock? covering key principles and practical usage.",
        "expected_concepts": [
            "deadlock"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How can deadlocks be prevented?",
        "expected_answer": "Clear technical explanation of how can deadlocks be prevented? covering key principles and practical usage.",
        "expected_concepts": [
            "deadlocks",
            "prevented"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are race conditions?",
        "expected_answer": "Clear technical explanation of what are race conditions? covering key principles and practical usage.",
        "expected_concepts": [
            "race",
            "conditions"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain volatile variables.",
        "expected_answer": "Clear technical explanation of volatile variables. covering key principles and practical usage.",
        "expected_concepts": [
            "volatile",
            "variables"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain synchronized blocks and methods.",
        "expected_answer": "Clear technical explanation of synchronized blocks and methods. covering key principles and practical usage.",
        "expected_concepts": [
            "synchronized",
            "blocks",
            "methods"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are atomic classes?",
        "expected_answer": "Clear technical explanation of what are atomic classes? covering key principles and practical usage.",
        "expected_concepts": [
            "atomic",
            "classes"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain CompletableFuture.",
        "expected_answer": "Clear technical explanation of completablefuture. covering key principles and practical usage.",
        "expected_concepts": [
            "CompletableFuture"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Java Stream optimization.",
        "expected_answer": "Clear technical explanation of java stream optimization. covering key principles and practical usage.",
        "expected_concepts": [
            "Java",
            "Stream",
            "optimization"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are design patterns in Java?",
        "expected_answer": "Clear technical explanation of what are design patterns in java? covering key principles and practical usage.",
        "expected_concepts": [
            "design",
            "patterns",
            "Java"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Singleton, Factory, and Observer patterns.",
        "expected_answer": "Clear technical explanation of singleton, factory, and observer patterns. covering key principles and practical usage.",
        "expected_concepts": [
            "Singleton",
            "Factory",
            "Observer",
            "patterns"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is dependency injection?",
        "expected_answer": "Clear technical explanation of dependency injection? covering key principles and practical usage.",
        "expected_concepts": [
            "dependency",
            "injection"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you design a scalable Java application?",
        "expected_answer": "Clear technical explanation of how would you design a scalable java application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "design",
            "scalable",
            "Java"
        ]
    },
    {
        "role": "Java Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you improve the performance of a Java application?",
        "expected_answer": "Clear technical explanation of how would you improve the performance of a java application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "improve",
            "performance",
            "Java"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is software?",
        "expected_answer": "Clear technical explanation of software? covering key principles and practical usage.",
        "expected_concepts": [
            "software"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is software development?",
        "expected_answer": "Clear technical explanation of software development? covering key principles and practical usage.",
        "expected_concepts": [
            "software",
            "development"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is SDLC?",
        "expected_answer": "Clear technical explanation of sdlc? covering key principles and practical usage.",
        "expected_concepts": [
            "SDLC"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "Explain the stages of SDLC.",
        "expected_answer": "Clear technical explanation of the stages of sdlc. covering key principles and practical usage.",
        "expected_concepts": [
            "stages",
            "SDLC"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is the Waterfall model?",
        "expected_answer": "Clear technical explanation of the waterfall model? covering key principles and practical usage.",
        "expected_concepts": [
            "Waterfall",
            "model"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is Agile?",
        "expected_answer": "Clear technical explanation of agile? covering key principles and practical usage.",
        "expected_concepts": [
            "Agile"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is Scrum?",
        "expected_answer": "Clear technical explanation of scrum? covering key principles and practical usage.",
        "expected_concepts": [
            "Scrum"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a requirement?",
        "expected_answer": "Clear technical explanation of a requirement? covering key principles and practical usage.",
        "expected_concepts": [
            "requirement"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is functional requirement?",
        "expected_answer": "Clear technical explanation of functional requirement? covering key principles and practical usage.",
        "expected_concepts": [
            "functional",
            "requirement"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is non-functional requirement?",
        "expected_answer": "Clear technical explanation of non-functional requirement? covering key principles and practical usage.",
        "expected_concepts": [
            "non-functional",
            "requirement"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is debugging?",
        "expected_answer": "Clear technical explanation of debugging? covering key principles and practical usage.",
        "expected_concepts": [
            "debugging"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is software testing?",
        "expected_answer": "Clear technical explanation of software testing? covering key principles and practical usage.",
        "expected_concepts": [
            "software",
            "testing"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is unit testing?",
        "expected_answer": "Clear technical explanation of unit testing? covering key principles and practical usage.",
        "expected_concepts": [
            "unit",
            "testing"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is integration testing?",
        "expected_answer": "Clear technical explanation of integration testing? covering key principles and practical usage.",
        "expected_concepts": [
            "integration",
            "testing"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is Git?",
        "expected_answer": "Clear technical explanation of git? covering key principles and practical usage.",
        "expected_concepts": [
            "Git"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is GitHub?",
        "expected_answer": "Clear technical explanation of github? covering key principles and practical usage.",
        "expected_concepts": [
            "GitHub"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a Git repository?",
        "expected_answer": "Clear technical explanation of a git repository? covering key principles and practical usage.",
        "expected_concepts": [
            "repository"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a Git branch?",
        "expected_answer": "Clear technical explanation of a git branch? covering key principles and practical usage.",
        "expected_concepts": [
            "branch"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is an API?",
        "expected_answer": "Clear technical explanation of an api? covering key principles and practical usage.",
        "expected_concepts": [
            "API"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a database?",
        "expected_answer": "Clear technical explanation of a database? covering key principles and practical usage.",
        "expected_concepts": [
            "database"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain Agile methodology.",
        "expected_answer": "Clear technical explanation of agile methodology. covering key principles and practical usage.",
        "expected_concepts": [
            "Agile",
            "methodology"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are Scrum roles?",
        "expected_answer": "Clear technical explanation of what are scrum roles? covering key principles and practical usage.",
        "expected_concepts": [
            "Scrum",
            "roles"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a user story?",
        "expected_answer": "Clear technical explanation of a user story? covering key principles and practical usage.",
        "expected_concepts": [
            "user",
            "story"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is an API?",
        "expected_answer": "Clear technical explanation of an api? covering key principles and practical usage.",
        "expected_concepts": [
            "API"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is REST API?",
        "expected_answer": "Clear technical explanation of rest api? covering key principles and practical usage.",
        "expected_concepts": [
            "REST",
            "API"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between REST and SOAP.",
        "expected_answer": "Clear technical explanation of difference between rest and soap. covering key principles and practical usage.",
        "expected_concepts": [
            "REST",
            "SOAP"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain GET, POST, PUT, PATCH, and DELETE.",
        "expected_answer": "Clear technical explanation of get, post, put, patch, and delete. covering key principles and practical usage.",
        "expected_concepts": [
            "GET",
            "POST",
            "PUT",
            "PATCH"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain common HTTP status codes.",
        "expected_answer": "Clear technical explanation of common http status codes. covering key principles and practical usage.",
        "expected_concepts": [
            "common",
            "HTTP",
            "status",
            "codes"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is authentication?",
        "expected_answer": "Clear technical explanation of authentication? covering key principles and practical usage.",
        "expected_concepts": [
            "authentication"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is authorization?",
        "expected_answer": "Clear technical explanation of authorization? covering key principles and practical usage.",
        "expected_concepts": [
            "authorization"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain OOP principles.",
        "expected_answer": "Clear technical explanation of oop principles. covering key principles and practical usage.",
        "expected_concepts": [
            "principles"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are SOLID principles?",
        "expected_answer": "Clear technical explanation of what are solid principles? covering key principles and practical usage.",
        "expected_concepts": [
            "SOLID",
            "principles"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between high-level and low-level design.",
        "expected_answer": "Clear technical explanation of difference between high-level and low-level design. covering key principles and practical usage.",
        "expected_concepts": [
            "high-level",
            "low-level",
            "design"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between Git merge and rebase.",
        "expected_answer": "Clear technical explanation of difference between git merge and rebase. covering key principles and practical usage.",
        "expected_concepts": [
            "merge",
            "rebase"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a pull request?",
        "expected_answer": "Clear technical explanation of a pull request? covering key principles and practical usage.",
        "expected_concepts": [
            "pull",
            "request"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is CI/CD?",
        "expected_answer": "Clear technical explanation of ci/cd? covering key principles and practical usage.",
        "expected_concepts": [
            "CI/CD"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between unit and integration testing.",
        "expected_answer": "Clear technical explanation of difference between unit and integration testing. covering key principles and practical usage.",
        "expected_concepts": [
            "unit",
            "integration",
            "testing"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is database normalization?",
        "expected_answer": "Clear technical explanation of database normalization? covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "normalization"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is exception handling?",
        "expected_answer": "Clear technical explanation of exception handling? covering key principles and practical usage.",
        "expected_concepts": [
            "exception",
            "handling"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How would you debug a production issue?",
        "expected_answer": "Clear technical explanation of how would you debug a production issue? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "debug",
            "production",
            "issue"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you design a scalable application?",
        "expected_answer": "Clear technical explanation of how would you design a scalable application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "design",
            "scalable",
            "application"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is system design?",
        "expected_answer": "Clear technical explanation of system design? covering key principles and practical usage.",
        "expected_concepts": [
            "system",
            "design"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is a microservices architecture?",
        "expected_answer": "Clear technical explanation of a microservices architecture? covering key principles and practical usage.",
        "expected_concepts": [
            "microservices",
            "architecture"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Monolithic vs microservices architecture?",
        "expected_answer": "Clear technical explanation of monolithic vs microservices architecture? covering key principles and practical usage.",
        "expected_concepts": [
            "Monolithic",
            "microservices",
            "architecture"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is service-oriented architecture?",
        "expected_answer": "Clear technical explanation of service-oriented architecture? covering key principles and practical usage.",
        "expected_concepts": [
            "service-oriented",
            "architecture"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is load balancing?",
        "expected_answer": "Clear technical explanation of load balancing? covering key principles and practical usage.",
        "expected_concepts": [
            "load",
            "balancing"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is caching?",
        "expected_answer": "Clear technical explanation of caching? covering key principles and practical usage.",
        "expected_concepts": [
            "caching"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is database sharding?",
        "expected_answer": "Clear technical explanation of database sharding? covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "sharding"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is replication?",
        "expected_answer": "Clear technical explanation of replication? covering key principles and practical usage.",
        "expected_concepts": [
            "replication"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is message queuing?",
        "expected_answer": "Clear technical explanation of message queuing? covering key principles and practical usage.",
        "expected_concepts": [
            "message",
            "queuing"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Kafka/RabbitMQ concepts.",
        "expected_answer": "Clear technical explanation of kafka/rabbitmq concepts. covering key principles and practical usage.",
        "expected_concepts": [
            "Kafka/RabbitMQ",
            "concepts"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is an API gateway?",
        "expected_answer": "Clear technical explanation of an api gateway? covering key principles and practical usage.",
        "expected_concepts": [
            "gateway"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is rate limiting?",
        "expected_answer": "Clear technical explanation of rate limiting? covering key principles and practical usage.",
        "expected_concepts": [
            "rate",
            "limiting"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is fault tolerance?",
        "expected_answer": "Clear technical explanation of fault tolerance? covering key principles and practical usage.",
        "expected_concepts": [
            "fault",
            "tolerance"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is horizontal vs vertical scaling?",
        "expected_answer": "Clear technical explanation of horizontal vs vertical scaling? covering key principles and practical usage.",
        "expected_concepts": [
            "horizontal",
            "vertical",
            "scaling"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is eventual consistency?",
        "expected_answer": "Clear technical explanation of eventual consistency? covering key principles and practical usage.",
        "expected_concepts": [
            "eventual",
            "consistency"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are design patterns?",
        "expected_answer": "Clear technical explanation of what are design patterns? covering key principles and practical usage.",
        "expected_concepts": [
            "design",
            "patterns"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How do you secure a REST API?",
        "expected_answer": "Clear technical explanation of how do you secure a rest api? covering key principles and practical usage.",
        "expected_concepts": [
            "secure",
            "REST",
            "API"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you troubleshoot a slow application?",
        "expected_answer": "Clear technical explanation of how would you troubleshoot a slow application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "troubleshoot",
            "slow",
            "application"
        ]
    },
    {
        "role": "Software Developer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Design a basic e-commerce / banking / interview platform architecture.",
        "expected_answer": "Clear technical explanation of design a basic e-commerce / banking / interview platform architecture. covering key principles and practical usage.",
        "expected_concepts": [
            "Design",
            "basic",
            "e-commerce",
            "banking"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is data analysis?",
        "expected_answer": "Clear technical explanation of data analysis? covering key principles and practical usage.",
        "expected_concepts": [
            "data",
            "analysis"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is artificial intelligence?",
        "expected_answer": "Clear technical explanation of artificial intelligence? covering key principles and practical usage.",
        "expected_concepts": [
            "artificial",
            "intelligence"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is machine learning?",
        "expected_answer": "Clear technical explanation of machine learning? covering key principles and practical usage.",
        "expected_concepts": [
            "machine",
            "learning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is deep learning?",
        "expected_answer": "Clear technical explanation of deep learning? covering key principles and practical usage.",
        "expected_concepts": [
            "deep",
            "learning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "Difference between AI, ML, and DL.",
        "expected_answer": "Clear technical explanation of difference between ai, ml, and dl. covering key principles and practical usage.",
        "expected_concepts": []
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a dataset?",
        "expected_answer": "Clear technical explanation of a dataset? covering key principles and practical usage.",
        "expected_concepts": [
            "dataset"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is structured data?",
        "expected_answer": "Clear technical explanation of structured data? covering key principles and practical usage.",
        "expected_concepts": [
            "structured",
            "data"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is unstructured data?",
        "expected_answer": "Clear technical explanation of unstructured data? covering key principles and practical usage.",
        "expected_concepts": [
            "unstructured",
            "data"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is data preprocessing?",
        "expected_answer": "Clear technical explanation of data preprocessing? covering key principles and practical usage.",
        "expected_concepts": [
            "data",
            "preprocessing"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is missing data?",
        "expected_answer": "Clear technical explanation of missing data? covering key principles and practical usage.",
        "expected_concepts": [
            "missing",
            "data"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is an outlier?",
        "expected_answer": "Clear technical explanation of an outlier? covering key principles and practical usage.",
        "expected_concepts": [
            "outlier"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is mean?",
        "expected_answer": "Clear technical explanation of mean? covering key principles and practical usage.",
        "expected_concepts": [
            "mean"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is median?",
        "expected_answer": "Clear technical explanation of median? covering key principles and practical usage.",
        "expected_concepts": [
            "median"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is mode?",
        "expected_answer": "Clear technical explanation of mode? covering key principles and practical usage.",
        "expected_concepts": [
            "mode"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is variance?",
        "expected_answer": "Clear technical explanation of variance? covering key principles and practical usage.",
        "expected_concepts": [
            "variance"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is standard deviation?",
        "expected_answer": "Clear technical explanation of standard deviation? covering key principles and practical usage.",
        "expected_concepts": [
            "standard",
            "deviation"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is correlation?",
        "expected_answer": "Clear technical explanation of correlation? covering key principles and practical usage.",
        "expected_concepts": [
            "correlation"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is EDA?",
        "expected_answer": "Clear technical explanation of eda? covering key principles and practical usage.",
        "expected_concepts": [
            "EDA"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is supervised learning?",
        "expected_answer": "Clear technical explanation of supervised learning? covering key principles and practical usage.",
        "expected_concepts": [
            "supervised",
            "learning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is unsupervised learning?",
        "expected_answer": "Clear technical explanation of unsupervised learning? covering key principles and practical usage.",
        "expected_concepts": [
            "unsupervised",
            "learning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How do you handle missing values?",
        "expected_answer": "Clear technical explanation of how do you handle missing values? covering key principles and practical usage.",
        "expected_concepts": [
            "handle",
            "missing",
            "values"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How do you handle outliers?",
        "expected_answer": "Clear technical explanation of how do you handle outliers? covering key principles and practical usage.",
        "expected_concepts": [
            "handle",
            "outliers"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Normalization vs standardization.",
        "expected_answer": "Clear technical explanation of normalization vs standardization. covering key principles and practical usage.",
        "expected_concepts": [
            "Normalization",
            "standardization"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain feature engineering.",
        "expected_answer": "Clear technical explanation of feature engineering. covering key principles and practical usage.",
        "expected_concepts": [
            "feature",
            "engineering"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain feature selection.",
        "expected_answer": "Clear technical explanation of feature selection. covering key principles and practical usage.",
        "expected_concepts": [
            "feature",
            "selection"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Classification vs regression.",
        "expected_answer": "Clear technical explanation of classification vs regression. covering key principles and practical usage.",
        "expected_concepts": [
            "Classification",
            "regression"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain train, validation, and test data.",
        "expected_answer": "Clear technical explanation of train, validation, and test data. covering key principles and practical usage.",
        "expected_concepts": [
            "train",
            "validation",
            "test",
            "data"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is overfitting?",
        "expected_answer": "Clear technical explanation of overfitting? covering key principles and practical usage.",
        "expected_concepts": [
            "overfitting"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is underfitting?",
        "expected_answer": "Clear technical explanation of underfitting? covering key principles and practical usage.",
        "expected_concepts": [
            "underfitting"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain bias-variance tradeoff.",
        "expected_answer": "Clear technical explanation of bias-variance tradeoff. covering key principles and practical usage.",
        "expected_concepts": [
            "bias-variance",
            "tradeoff"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is cross-validation?",
        "expected_answer": "Clear technical explanation of cross-validation? covering key principles and practical usage.",
        "expected_concepts": [
            "cross-validation"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain confusion matrix.",
        "expected_answer": "Clear technical explanation of confusion matrix. covering key principles and practical usage.",
        "expected_concepts": [
            "confusion",
            "matrix"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain accuracy, precision, recall, and F1-score.",
        "expected_answer": "Clear technical explanation of accuracy, precision, recall, and f1-score. covering key principles and practical usage.",
        "expected_concepts": [
            "accuracy",
            "precision",
            "recall",
            "F1-score"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is class imbalance?",
        "expected_answer": "Clear technical explanation of class imbalance? covering key principles and practical usage.",
        "expected_concepts": [
            "class",
            "imbalance"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How do you handle imbalanced datasets?",
        "expected_answer": "Clear technical explanation of how do you handle imbalanced datasets? covering key principles and practical usage.",
        "expected_concepts": [
            "handle",
            "imbalanced",
            "datasets"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a decision tree?",
        "expected_answer": "Clear technical explanation of a decision tree? covering key principles and practical usage.",
        "expected_concepts": [
            "decision",
            "tree"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is random forest?",
        "expected_answer": "Clear technical explanation of random forest? covering key principles and practical usage.",
        "expected_concepts": [
            "random",
            "forest"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is linear regression?",
        "expected_answer": "Clear technical explanation of linear regression? covering key principles and practical usage.",
        "expected_concepts": [
            "linear",
            "regression"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is logistic regression?",
        "expected_answer": "Clear technical explanation of logistic regression? covering key principles and practical usage.",
        "expected_concepts": [
            "logistic",
            "regression"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How do you select an ML algorithm?",
        "expected_answer": "Clear technical explanation of how do you select an ml algorithm? covering key principles and practical usage.",
        "expected_concepts": [
            "select",
            "algorithm"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain ensemble learning.",
        "expected_answer": "Clear technical explanation of ensemble learning. covering key principles and practical usage.",
        "expected_concepts": [
            "ensemble",
            "learning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Bagging vs boosting.",
        "expected_answer": "Clear technical explanation of bagging vs boosting. covering key principles and practical usage.",
        "expected_concepts": [
            "Bagging",
            "boosting"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Random Forest internally.",
        "expected_answer": "Clear technical explanation of random forest internally. covering key principles and practical usage.",
        "expected_concepts": [
            "Random",
            "Forest",
            "internally"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain Gradient Boosting.",
        "expected_answer": "Clear technical explanation of gradient boosting. covering key principles and practical usage.",
        "expected_concepts": [
            "Gradient",
            "Boosting"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is XGBoost?",
        "expected_answer": "Clear technical explanation of xgboost? covering key principles and practical usage.",
        "expected_concepts": [
            "XGBoost"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is hyperparameter tuning?",
        "expected_answer": "Clear technical explanation of hyperparameter tuning? covering key principles and practical usage.",
        "expected_concepts": [
            "hyperparameter",
            "tuning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Grid Search vs Random Search.",
        "expected_answer": "Clear technical explanation of grid search vs random search. covering key principles and practical usage.",
        "expected_concepts": [
            "Grid",
            "Search",
            "Random",
            "Search"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is dimensionality reduction?",
        "expected_answer": "Clear technical explanation of dimensionality reduction? covering key principles and practical usage.",
        "expected_concepts": [
            "dimensionality",
            "reduction"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain PCA.",
        "expected_answer": "Clear technical explanation of pca. covering key principles and practical usage.",
        "expected_concepts": [
            "PCA"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is feature importance?",
        "expected_answer": "Clear technical explanation of feature importance? covering key principles and practical usage.",
        "expected_concepts": [
            "feature",
            "importance"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is model interpretability?",
        "expected_answer": "Clear technical explanation of model interpretability? covering key principles and practical usage.",
        "expected_concepts": [
            "model",
            "interpretability"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is data leakage?",
        "expected_answer": "Clear technical explanation of data leakage? covering key principles and practical usage.",
        "expected_concepts": [
            "data",
            "leakage"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How can data leakage be prevented?",
        "expected_answer": "Clear technical explanation of how can data leakage be prevented? covering key principles and practical usage.",
        "expected_concepts": [
            "data",
            "leakage",
            "prevented"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain ROC-AUC.",
        "expected_answer": "Clear technical explanation of roc-auc. covering key principles and practical usage.",
        "expected_concepts": [
            "ROC-AUC"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "When is F1-score better than accuracy?",
        "expected_answer": "Clear technical explanation of when is f1-score better than accuracy? covering key principles and practical usage.",
        "expected_concepts": [
            "When",
            "F1-score",
            "better",
            "than"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain neural network architecture.",
        "expected_answer": "Clear technical explanation of neural network architecture. covering key principles and practical usage.",
        "expected_concepts": [
            "neural",
            "network",
            "architecture"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain backpropagation.",
        "expected_answer": "Clear technical explanation of backpropagation. covering key principles and practical usage.",
        "expected_concepts": [
            "backpropagation"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is transfer learning?",
        "expected_answer": "Clear technical explanation of transfer learning? covering key principles and practical usage.",
        "expected_concepts": [
            "transfer",
            "learning"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you deploy an ML model?",
        "expected_answer": "Clear technical explanation of how would you deploy an ml model? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "deploy",
            "model"
        ]
    },
    {
        "role": "Data Analyst & AI Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you design an end-to-end AI system from data collection \u2192 preprocessing \u2192 training \u2192 evaluation \u2192 deployment \u2192 monitoring?",
        "expected_answer": "Clear technical explanation of how would you design an end-to-end ai system from data collection \u2192 preprocessing \u2192 training \u2192 evaluation \u2192 deployment \u2192 monitoring? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "design",
            "end-to-end",
            "system"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is SQL?",
        "expected_answer": "Clear technical explanation of sql? covering key principles and practical usage.",
        "expected_concepts": [
            "SQL"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is DBMS?",
        "expected_answer": "Clear technical explanation of dbms? covering key principles and practical usage.",
        "expected_concepts": [
            "DBMS"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is RDBMS?",
        "expected_answer": "Clear technical explanation of rdbms? covering key principles and practical usage.",
        "expected_concepts": [
            "RDBMS"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a table?",
        "expected_answer": "Clear technical explanation of a table? covering key principles and practical usage.",
        "expected_concepts": [
            "table"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a row?",
        "expected_answer": "Clear technical explanation of a row? covering key principles and practical usage.",
        "expected_concepts": [
            "row"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a column?",
        "expected_answer": "Clear technical explanation of a column? covering key principles and practical usage.",
        "expected_concepts": [
            "column"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a primary key?",
        "expected_answer": "Clear technical explanation of a primary key? covering key principles and practical usage.",
        "expected_concepts": [
            "primary",
            "key"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a foreign key?",
        "expected_answer": "Clear technical explanation of a foreign key? covering key principles and practical usage.",
        "expected_concepts": [
            "foreign",
            "key"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a unique key?",
        "expected_answer": "Clear technical explanation of a unique key? covering key principles and practical usage.",
        "expected_concepts": [
            "unique",
            "key"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is SELECT?",
        "expected_answer": "Clear technical explanation of select? covering key principles and practical usage.",
        "expected_concepts": [
            "SELECT"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is WHERE?",
        "expected_answer": "Clear technical explanation of where? covering key principles and practical usage.",
        "expected_concepts": [
            "WHERE"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is ORDER BY?",
        "expected_answer": "Clear technical explanation of order by? covering key principles and practical usage.",
        "expected_concepts": [
            "ORDER"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is GROUP BY?",
        "expected_answer": "Clear technical explanation of group by? covering key principles and practical usage.",
        "expected_concepts": [
            "GROUP"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is HAVING?",
        "expected_answer": "Clear technical explanation of having? covering key principles and practical usage.",
        "expected_concepts": [
            "HAVING"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What are aggregate functions?",
        "expected_answer": "Clear technical explanation of what are aggregate functions? covering key principles and practical usage.",
        "expected_concepts": [
            "aggregate",
            "functions"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a JOIN?",
        "expected_answer": "Clear technical explanation of a join? covering key principles and practical usage.",
        "expected_concepts": [
            "JOIN"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is an INNER JOIN?",
        "expected_answer": "Clear technical explanation of an inner join? covering key principles and practical usage.",
        "expected_concepts": [
            "INNER",
            "JOIN"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a LEFT JOIN?",
        "expected_answer": "Clear technical explanation of a left join? covering key principles and practical usage.",
        "expected_concepts": [
            "LEFT",
            "JOIN"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is a subquery?",
        "expected_answer": "Clear technical explanation of a subquery? covering key principles and practical usage.",
        "expected_concepts": [
            "subquery"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Beginner",
        "question_text": "What is database normalization?",
        "expected_answer": "Clear technical explanation of database normalization? covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "normalization"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain all types of SQL JOINs.",
        "expected_answer": "Clear technical explanation of all types of sql joins. covering key principles and practical usage.",
        "expected_concepts": [
            "types",
            "JOINs"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "WHERE vs HAVING.",
        "expected_answer": "Clear technical explanation of where vs having. covering key principles and practical usage.",
        "expected_concepts": [
            "WHERE",
            "HAVING"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "GROUP BY vs ORDER BY.",
        "expected_answer": "Clear technical explanation of group by vs order by. covering key principles and practical usage.",
        "expected_concepts": [
            "GROUP",
            "ORDER"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a correlated subquery?",
        "expected_answer": "Clear technical explanation of a correlated subquery? covering key principles and practical usage.",
        "expected_concepts": [
            "correlated",
            "subquery"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a CTE?",
        "expected_answer": "Clear technical explanation of a cte? covering key principles and practical usage.",
        "expected_concepts": [
            "CTE"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are window functions?",
        "expected_answer": "Clear technical explanation of what are window functions? covering key principles and practical usage.",
        "expected_concepts": [
            "window",
            "functions"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain ROW_NUMBER().",
        "expected_answer": "Clear technical explanation of row_number(). covering key principles and practical usage.",
        "expected_concepts": [
            "ROW_NUMBER"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Difference between RANK() and DENSE_RANK().",
        "expected_answer": "Clear technical explanation of difference between rank() and dense_rank(). covering key principles and practical usage.",
        "expected_concepts": [
            "RANK",
            "DENSE_RANK"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is an index?",
        "expected_answer": "Clear technical explanation of an index? covering key principles and practical usage.",
        "expected_concepts": [
            "index"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How does an index improve performance?",
        "expected_answer": "Clear technical explanation of how does an index improve performance? covering key principles and practical usage.",
        "expected_concepts": [
            "index",
            "improve",
            "performance"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is normalization?",
        "expected_answer": "Clear technical explanation of normalization? covering key principles and practical usage.",
        "expected_concepts": [
            "normalization"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain 1NF, 2NF, and 3NF.",
        "expected_answer": "Clear technical explanation of 1nf, 2nf, and 3nf. covering key principles and practical usage.",
        "expected_concepts": [
            "1NF",
            "2NF",
            "3NF"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is denormalization?",
        "expected_answer": "Clear technical explanation of denormalization? covering key principles and practical usage.",
        "expected_concepts": [
            "denormalization"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What are transactions?",
        "expected_answer": "Clear technical explanation of what are transactions? covering key principles and practical usage.",
        "expected_concepts": [
            "transactions"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "Explain ACID properties.",
        "expected_answer": "Clear technical explanation of acid properties. covering key principles and practical usage.",
        "expected_concepts": [
            "ACID",
            "properties"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a view?",
        "expected_answer": "Clear technical explanation of a view? covering key principles and practical usage.",
        "expected_concepts": [
            "view"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a stored procedure?",
        "expected_answer": "Clear technical explanation of a stored procedure? covering key principles and practical usage.",
        "expected_concepts": [
            "stored",
            "procedure"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a trigger?",
        "expected_answer": "Clear technical explanation of a trigger? covering key principles and practical usage.",
        "expected_concepts": [
            "trigger"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "What is a self join?",
        "expected_answer": "Clear technical explanation of a self join? covering key principles and practical usage.",
        "expected_concepts": [
            "self",
            "join"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Intermediate",
        "question_text": "How would you optimize a slow SQL query?",
        "expected_answer": "Clear technical explanation of how would you optimize a slow sql query? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "optimize",
            "slow",
            "query"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain database indexing internally.",
        "expected_answer": "Clear technical explanation of database indexing internally. covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "indexing",
            "internally"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Clustered vs non-clustered indexes.",
        "expected_answer": "Clear technical explanation of clustered vs non-clustered indexes. covering key principles and practical usage.",
        "expected_concepts": [
            "Clustered",
            "non-clustered",
            "indexes"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is a composite index?",
        "expected_answer": "Clear technical explanation of a composite index? covering key principles and practical usage.",
        "expected_concepts": [
            "composite",
            "index"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is query execution planning?",
        "expected_answer": "Clear technical explanation of query execution planning? covering key principles and practical usage.",
        "expected_concepts": [
            "query",
            "execution",
            "planning"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is an execution plan?",
        "expected_answer": "Clear technical explanation of an execution plan? covering key principles and practical usage.",
        "expected_concepts": [
            "execution",
            "plan"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How do you identify a slow SQL query?",
        "expected_answer": "Clear technical explanation of how do you identify a slow sql query? covering key principles and practical usage.",
        "expected_concepts": [
            "identify",
            "slow",
            "query"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is database partitioning?",
        "expected_answer": "Clear technical explanation of database partitioning? covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "partitioning"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is database sharding?",
        "expected_answer": "Clear technical explanation of database sharding? covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "sharding"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain replication.",
        "expected_answer": "Clear technical explanation of replication. covering key principles and practical usage.",
        "expected_concepts": [
            "replication"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is master-slave/primary-replica architecture?",
        "expected_answer": "Clear technical explanation of master-slave/primary-replica architecture? covering key principles and practical usage.",
        "expected_concepts": [
            "master-slave/primary-replica",
            "architecture"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is a deadlock in databases?",
        "expected_answer": "Clear technical explanation of a deadlock in databases? covering key principles and practical usage.",
        "expected_concepts": [
            "deadlock",
            "databases"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How can database deadlocks be prevented?",
        "expected_answer": "Clear technical explanation of how can database deadlocks be prevented? covering key principles and practical usage.",
        "expected_concepts": [
            "database",
            "deadlocks",
            "prevented"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Explain transaction isolation levels.",
        "expected_answer": "Clear technical explanation of transaction isolation levels. covering key principles and practical usage.",
        "expected_concepts": [
            "transaction",
            "isolation",
            "levels"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are dirty reads?",
        "expected_answer": "Clear technical explanation of what are dirty reads? covering key principles and practical usage.",
        "expected_concepts": [
            "dirty",
            "reads"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What are phantom reads?",
        "expected_answer": "Clear technical explanation of what are phantom reads? covering key principles and practical usage.",
        "expected_concepts": [
            "phantom",
            "reads"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "What is optimistic vs pessimistic locking?",
        "expected_answer": "Clear technical explanation of optimistic vs pessimistic locking? covering key principles and practical usage.",
        "expected_concepts": [
            "optimistic",
            "pessimistic",
            "locking"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you design a database for a large-scale application?",
        "expected_answer": "Clear technical explanation of how would you design a database for a large-scale application? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "design",
            "database",
            "large-scale"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you optimize a database containing millions of records?",
        "expected_answer": "Clear technical explanation of how would you optimize a database containing millions of records? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "optimize",
            "database",
            "containing"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "How would you handle database backup and recovery?",
        "expected_answer": "Clear technical explanation of how would you handle database backup and recovery? covering key principles and practical usage.",
        "expected_concepts": [
            "would",
            "handle",
            "database",
            "backup"
        ]
    },
    {
        "role": "SQL & Database Engineer",
        "category": "Technical",
        "difficulty": "Advanced",
        "question_text": "Design the database architecture for an e-commerce / banking / job portal system.",
        "expected_answer": "Clear technical explanation of design the database architecture for an e-commerce / banking / job portal system. covering key principles and practical usage.",
        "expected_concepts": [
            "Design",
            "database",
            "architecture",
            "e-commerce"
        ]
    }
]
