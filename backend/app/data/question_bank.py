import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Question Bank — 150+ curated interview questions
Covers 5 roles × 3 categories × 3 difficulty levels
"""

JOB_ROLES = [
    {"role_name": "Python Developer", "description": "Build applications, scripts, and systems using Python."},
    {"role_name": "Data Analyst", "description": "Analyze data to drive business decisions using SQL, Python, and BI tools."},
    {"role_name": "AI/ML Engineer", "description": "Design and deploy machine learning models and AI systems."},
    {"role_name": "SQL Developer", "description": "Design, query, and optimize relational databases."},
    {"role_name": "Software Developer", "description": "Build software systems using various programming languages and frameworks."},
]

QUESTION_BANK = [

    # ─────────────────────────────────────────────────────────────
    # PYTHON DEVELOPER
    # ─────────────────────────────────────────────────────────────

    # Technical — Beginner
    {"role": "Python Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between a list and a tuple in Python?",
     "expected_answer": "A list is mutable (can be changed after creation) and uses square brackets []. A tuple is immutable (cannot be changed) and uses parentheses (). Tuples are faster and used for fixed data.",
     "expected_concepts": ["mutable", "immutable", "list", "tuple", "square brackets", "parentheses"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What are Python decorators and how do you use them?",
     "expected_answer": "A decorator is a function that wraps another function to extend its behavior without modifying its source code. Applied with @decorator_name syntax above a function definition.",
     "expected_concepts": ["decorator", "function", "@syntax", "wrapper", "extend behavior"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "Explain the difference between '==' and 'is' operators in Python.",
     "expected_answer": "'==' checks value equality (are the values the same?). 'is' checks identity (are they the same object in memory?). Example: [1,2] == [1,2] is True but [1,2] is [1,2] is False.",
     "expected_concepts": ["equality", "identity", "memory", "value", "object"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What are Python's built-in data types?",
     "expected_answer": "Python's main built-in types are: int, float, str, bool, list, tuple, dict, set, frozenset, NoneType, bytes.",
     "expected_concepts": ["int", "float", "str", "list", "tuple", "dict", "set"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the use of 'self' in Python classes?",
     "expected_answer": "self refers to the instance of the class. It is the first parameter of instance methods and allows access to instance attributes and other methods within the class.",
     "expected_concepts": ["self", "instance", "class", "attribute", "method"]},

    # Technical — Intermediate
    {"role": "Python Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain list comprehension with an example.",
     "expected_answer": "List comprehension provides a concise way to create lists. Example: squares = [x**2 for x in range(10)]. Can include conditions: evens = [x for x in range(20) if x % 2 == 0].",
     "expected_concepts": ["list comprehension", "concise", "condition", "iterable", "expression"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is the difference between *args and **kwargs?",
     "expected_answer": "*args allows a function to accept any number of positional arguments as a tuple. **kwargs allows any number of keyword arguments as a dictionary. def func(*args, **kwargs): passes them through.",
     "expected_concepts": ["*args", "**kwargs", "positional", "keyword", "tuple", "dictionary"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain Python's context managers and the 'with' statement.",
     "expected_answer": "Context managers manage resources automatically using __enter__ and __exit__ methods. The 'with' statement ensures cleanup happens even if an exception occurs. Used commonly for file handling: with open('file') as f.",
     "expected_concepts": ["context manager", "with statement", "__enter__", "__exit__", "resource management"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What are lambda functions in Python?",
     "expected_answer": "Lambda functions are anonymous, single-expression functions defined with the lambda keyword. Syntax: lambda arguments: expression. Example: square = lambda x: x**2. Used for short, throwaway functions.",
     "expected_concepts": ["lambda", "anonymous", "single expression", "inline", "functional"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "How does Python handle exceptions? Explain try-except-finally.",
     "expected_answer": "try block contains code that might raise an exception. except catches specific exceptions. else runs if no exception occurred. finally always runs regardless of exceptions (used for cleanup).",
     "expected_concepts": ["try", "except", "finally", "exception", "error handling", "cleanup"]},

    # Technical — Advanced
    {"role": "Python Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain Python's GIL (Global Interpreter Lock) and its implications.",
     "expected_answer": "The GIL is a mutex that allows only one thread to execute Python bytecode at a time. This prevents true parallelism for CPU-bound tasks. Use multiprocessing for CPU-bound parallelism; threading still useful for I/O-bound tasks.",
     "expected_concepts": ["GIL", "mutex", "thread", "bytecode", "multiprocessing", "CPU-bound", "I/O-bound"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What are Python generators and how do they differ from regular functions?",
     "expected_answer": "Generators use the yield keyword to produce values lazily, one at a time. They maintain state between calls, saving memory. A generator function returns a generator object. Example: def count(): yield 1; yield 2.",
     "expected_concepts": ["generator", "yield", "lazy evaluation", "memory efficient", "state", "iterator"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain metaclasses in Python.",
     "expected_answer": "A metaclass is the class of a class — it defines how a class behaves. type is the default metaclass. Custom metaclasses can modify class creation by inheriting from type and overriding __new__ or __init__.",
     "expected_concepts": ["metaclass", "type", "class creation", "__new__", "__init__", "class factory"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is the difference between deep copy and shallow copy in Python?",
     "expected_answer": "Shallow copy (copy.copy) creates a new object but references the same nested objects. Deep copy (copy.deepcopy) recursively copies all nested objects. Important for mutable nested structures.",
     "expected_concepts": ["shallow copy", "deep copy", "copy module", "nested objects", "reference", "recursive"]},

    {"role": "Python Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "How does Python's memory management work?",
     "expected_answer": "Python uses reference counting (Py_INCREF/DECREF) as primary GC and a cyclic garbage collector for circular references. Memory is managed in arenas/pools. del decrements reference count. When count hits 0, memory is freed.",
     "expected_concepts": ["reference counting", "garbage collection", "circular reference", "memory", "arena", "pool"]},

    # HR
    {"role": "Python Developer", "category": "HR", "difficulty": "Beginner",
     "question_text": "Tell me about yourself and your Python experience.",
     "expected_answer": "Structured introduction: educational background, Python experience, key projects built with Python, and career goals as a Python developer.",
     "expected_concepts": ["background", "experience", "projects", "goals", "Python"]},

    {"role": "Python Developer", "category": "HR", "difficulty": "Beginner",
     "question_text": "What are your strengths as a Python developer?",
     "expected_answer": "Mention specific strengths with examples: problem-solving ability, debugging skills, knowledge of Python libraries, clean code practices, and demonstrated projects.",
     "expected_concepts": ["strengths", "specific examples", "libraries", "clean code", "projects"]},

    {"role": "Python Developer", "category": "HR", "difficulty": "Intermediate",
     "question_text": "Describe a challenging Python project you worked on.",
     "expected_answer": "Use STAR method: Situation (context), Task (objective), Action (what you coded), Result (outcome). Focus on technical challenges and how you solved them.",
     "expected_concepts": ["STAR method", "challenge", "solution", "result", "technical"]},

    {"role": "Python Developer", "category": "HR", "difficulty": "Intermediate",
     "question_text": "How do you stay updated with Python developments?",
     "expected_answer": "Mention: reading PEPs, following Python.org, GitHub trending, real Python blog, YouTube channels, practicing on LeetCode/HackerRank, contributing to open source.",
     "expected_concepts": ["PEPs", "community", "practice", "open source", "learning"]},

    {"role": "Python Developer", "category": "HR", "difficulty": "Beginner",
     "question_text": "Where do you see yourself in 5 years as a Python developer?",
     "expected_answer": "Show career ambition: senior developer, team lead, specializing in AI/data engineering, contributing to open source, or architecting large-scale Python systems.",
     "expected_concepts": ["growth", "senior", "specialization", "ambition", "realistic"]},

    # Project
    {"role": "Python Developer", "category": "Project", "difficulty": "Intermediate",
     "question_text": "Explain a Python project you built. What was its purpose and how did you design it?",
     "expected_answer": "Describe project purpose, tech stack used (frameworks, libraries), architecture design, key challenges faced, and results achieved.",
     "expected_concepts": ["purpose", "tech stack", "architecture", "challenges", "results"]},

    {"role": "Python Developer", "category": "Project", "difficulty": "Intermediate",
     "question_text": "What Python libraries or frameworks did you use in your projects and why?",
     "expected_answer": "Discuss specific libraries (e.g., FastAPI for APIs, pandas for data, SQLAlchemy for DB, requests for HTTP) and justify each choice based on project requirements.",
     "expected_concepts": ["libraries", "frameworks", "justification", "requirements", "FastAPI", "pandas"]},

    # ─────────────────────────────────────────────────────────────
    # DATA ANALYST
    # ─────────────────────────────────────────────────────────────

    # Technical — Beginner
    {"role": "Data Analyst", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between INNER JOIN and LEFT JOIN in SQL?",
     "expected_answer": "INNER JOIN returns only rows where there is a match in both tables. LEFT JOIN returns all rows from the left table and matching rows from the right; non-matching rows show NULL.",
     "expected_concepts": ["INNER JOIN", "LEFT JOIN", "NULL", "match", "tables", "all rows"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is a primary key and why is it important?",
     "expected_answer": "A primary key is a column that uniquely identifies each row in a table. It cannot be NULL or duplicate. Every table should have one to ensure data integrity and enable relationships.",
     "expected_concepts": ["primary key", "unique", "NULL", "row", "data integrity"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between COUNT(*) and COUNT(column_name)?",
     "expected_answer": "COUNT(*) counts all rows including NULLs. COUNT(column_name) counts only non-NULL values in that specific column. Use COUNT(*) for total rows, COUNT(col) when NULLs should be excluded.",
     "expected_concepts": ["COUNT", "NULL", "rows", "non-null", "aggregate"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is data cleaning and why is it important?",
     "expected_answer": "Data cleaning involves identifying and fixing errors, duplicates, missing values, and inconsistencies in data. It's crucial because analysis on dirty data leads to incorrect conclusions and bad decisions.",
     "expected_concepts": ["missing values", "duplicates", "errors", "inconsistency", "accuracy", "decisions"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Beginner",
     "question_text": "Explain what a NULL value is in SQL.",
     "expected_answer": "NULL represents missing or unknown data. It is not zero or empty string. SQL handles NULL specially: NULL = NULL is FALSE. Use IS NULL or IS NOT NULL to check for nulls.",
     "expected_concepts": ["NULL", "missing", "unknown", "IS NULL", "IS NOT NULL", "not zero"]},

    # Technical — Intermediate
    {"role": "Data Analyst", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain the difference between GROUP BY and HAVING in SQL.",
     "expected_answer": "GROUP BY groups rows by specified columns for aggregation. HAVING filters those groups after aggregation (like WHERE but for groups). Example: GROUP BY dept HAVING COUNT(*) > 5 filters departments with more than 5 employees.",
     "expected_concepts": ["GROUP BY", "HAVING", "aggregate", "filter", "WHERE", "groups"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "How would you handle missing values in a dataset?",
     "expected_answer": "Options: 1) Remove rows with missing values (if few). 2) Impute with mean/median/mode. 3) Forward/backward fill for time series. 4) Use ML-based imputation. Choice depends on the amount of missing data and impact on analysis.",
     "expected_concepts": ["missing values", "imputation", "mean", "median", "drop", "time series"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?",
     "expected_answer": "ROW_NUMBER() assigns unique sequential numbers. RANK() assigns same rank for ties but skips numbers (1,1,3). DENSE_RANK() assigns same rank for ties but doesn't skip (1,1,2). All use OVER clause.",
     "expected_concepts": ["ROW_NUMBER", "RANK", "DENSE_RANK", "ties", "OVER", "window function"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain the concept of data normalization.",
     "expected_answer": "Normalization organizes database tables to reduce redundancy and improve data integrity. 1NF: atomic values. 2NF: no partial dependencies. 3NF: no transitive dependencies. Reduces update anomalies.",
     "expected_concepts": ["normalization", "redundancy", "1NF", "2NF", "3NF", "anomalies", "integrity"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is a subquery? When would you use it?",
     "expected_answer": "A subquery is a query nested inside another query. Use it to filter based on aggregated values, compute values dynamically, or use results of one query in another. Can appear in SELECT, FROM, or WHERE clauses.",
     "expected_concepts": ["subquery", "nested", "filter", "aggregate", "SELECT", "WHERE", "FROM"]},

    # Technical — Advanced
    {"role": "Data Analyst", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is a window function in SQL? Give a real-world example.",
     "expected_answer": "Window functions perform calculations across rows related to the current row without collapsing them. They use OVER() with PARTITION BY and ORDER BY. Example: running total of sales: SUM(sales) OVER (PARTITION BY region ORDER BY date).",
     "expected_concepts": ["window function", "OVER", "PARTITION BY", "ORDER BY", "running total", "rank"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain the difference between OLAP and OLTP systems.",
     "expected_answer": "OLTP (Online Transaction Processing) handles real-time transactions, normalized, optimized for INSERT/UPDATE/DELETE. OLAP (Online Analytical Processing) handles complex queries on large historical data, denormalized, optimized for READ performance (data warehouses).",
     "expected_concepts": ["OLTP", "OLAP", "transactions", "analytical", "normalized", "data warehouse"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is a CTE (Common Table Expression) and when should you use it?",
     "expected_answer": "A CTE is a named temporary result set defined with WITH keyword. It improves readability for complex queries, enables recursion, and can be referenced multiple times in the same query. Example: WITH ranked AS (SELECT ...) SELECT * FROM ranked WHERE rank=1.",
     "expected_concepts": ["CTE", "WITH", "temporary", "recursive", "readability", "subquery"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Advanced",
     "question_text": "How would you optimize a slow SQL query?",
     "expected_answer": "Steps: 1) Use EXPLAIN to analyze execution plan. 2) Add indexes on filtered/joined columns. 3) Avoid SELECT *, use specific columns. 4) Avoid functions on indexed columns. 5) Rewrite subqueries as JOINs. 6) Partition large tables.",
     "expected_concepts": ["EXPLAIN", "index", "execution plan", "optimization", "JOIN", "SELECT *", "partition"]},

    {"role": "Data Analyst", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain the concept of outlier detection and how to handle outliers.",
     "expected_answer": "Outliers are data points significantly different from others. Detection: IQR method (outside 1.5×IQR), Z-score (>3 std devs), box plots, scatter plots. Handle: remove if errors, keep if valid extreme values, transform (log), cap/floor.",
     "expected_concepts": ["outlier", "IQR", "Z-score", "box plot", "detection", "handling", "transform"]},

    # HR
    {"role": "Data Analyst", "category": "HR", "difficulty": "Beginner",
     "question_text": "Why do you want to become a Data Analyst?",
     "expected_answer": "Genuine interest in data and pattern recognition, examples of analyzing data in projects/college, excitement about using SQL/Python/Power BI, understanding of how data drives decisions.",
     "expected_concepts": ["interest", "data", "patterns", "tools", "business value", "decisions"]},

    {"role": "Data Analyst", "category": "HR", "difficulty": "Beginner",
     "question_text": "What tools and technologies are you comfortable with for data analysis?",
     "expected_answer": "Mention: SQL for querying, Python (pandas, numpy, matplotlib) for analysis, Power BI/Tableau for visualization, Excel for spreadsheet analysis. Give examples of using each.",
     "expected_concepts": ["SQL", "Python", "pandas", "Power BI", "Excel", "visualization", "tools"]},

    {"role": "Data Analyst", "category": "HR", "difficulty": "Intermediate",
     "question_text": "Describe a time when your data analysis led to a meaningful insight.",
     "expected_answer": "Use STAR method: describe the data analyzed, the analysis performed, the insight found, and the decision or action it led to. Be specific about the tools and methods used.",
     "expected_concepts": ["insight", "analysis", "decision", "impact", "STAR", "tools"]},

    {"role": "Data Analyst", "category": "HR", "difficulty": "Intermediate",
     "question_text": "How do you ensure accuracy in your analysis?",
     "expected_answer": "Data validation, cross-checking with multiple sources, peer review, unit testing queries, documenting assumptions, comparing results with expected business logic, version controlling notebooks.",
     "expected_concepts": ["validation", "accuracy", "peer review", "testing", "assumptions", "documentation"]},

    {"role": "Data Analyst", "category": "HR", "difficulty": "Beginner",
     "question_text": "How do you communicate complex data findings to non-technical stakeholders?",
     "expected_answer": "Use clear visualizations, avoid jargon, focus on business impact not methodology, use storytelling with data, prepare executive summaries, use dashboards with KPIs.",
     "expected_concepts": ["visualization", "non-technical", "storytelling", "KPIs", "dashboard", "business impact"]},

    # Project
    {"role": "Data Analyst", "category": "Project", "difficulty": "Intermediate",
     "question_text": "Describe a data analysis project you completed. What was the business problem?",
     "expected_answer": "Describe business problem, data sources used, analysis approach (EDA, statistical analysis), tools used, visualizations created, and insights/recommendations delivered.",
     "expected_concepts": ["business problem", "data sources", "EDA", "tools", "insights", "recommendations"]},

    {"role": "Data Analyst", "category": "Project", "difficulty": "Intermediate",
     "question_text": "Have you created any dashboards? What KPIs did you track?",
     "expected_answer": "Describe dashboard tool (Power BI, Tableau, etc.), KPIs tracked (revenue, conversion rate, etc.), audience, refresh frequency, and any insights that came from monitoring.",
     "expected_concepts": ["dashboard", "KPIs", "Power BI", "Tableau", "metrics", "monitoring"]},

    # ─────────────────────────────────────────────────────────────
    # AI/ML ENGINEER
    # ─────────────────────────────────────────────────────────────

    # Technical — Beginner
    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between supervised and unsupervised learning?",
     "expected_answer": "Supervised learning uses labeled training data to learn input-output mappings (classification, regression). Unsupervised learning finds patterns without labels (clustering, dimensionality reduction). Semi-supervised uses both.",
     "expected_concepts": ["supervised", "unsupervised", "labeled", "classification", "clustering", "regression"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between classification and regression?",
     "expected_answer": "Classification predicts a discrete category/class (e.g., spam/not spam, cat/dog). Regression predicts a continuous numerical value (e.g., house price, temperature). Different metrics: classification uses accuracy/F1, regression uses RMSE/MAE.",
     "expected_concepts": ["classification", "regression", "discrete", "continuous", "accuracy", "RMSE"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is a train-test split and why is it important?",
     "expected_answer": "Splitting data into training (e.g., 80%) and testing (20%) sets to evaluate model performance on unseen data. Prevents overfitting evaluation. Common splits: 70/30, 80/20, 60/20/20 (with validation).",
     "expected_concepts": ["train", "test", "split", "overfitting", "unseen data", "evaluation", "validation"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is a confusion matrix?",
     "expected_answer": "A confusion matrix shows True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN). Used to evaluate classification models. Derives metrics: accuracy, precision, recall, F1-score.",
     "expected_concepts": ["confusion matrix", "true positive", "false positive", "precision", "recall", "F1"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is feature engineering and why is it important?",
     "expected_answer": "Feature engineering is creating new features or transforming existing ones to improve model performance. Includes: encoding categoricals, scaling, polynomial features, interaction terms. Better features often matter more than better algorithms.",
     "expected_concepts": ["feature engineering", "encoding", "scaling", "transformation", "model performance"]},

    # Technical — Intermediate
    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain overfitting and how to prevent it.",
     "expected_answer": "Overfitting is when a model learns training data too well including noise, and generalizes poorly to new data. Prevention: regularization (L1/L2), dropout, cross-validation, pruning, more data, simpler model, early stopping.",
     "expected_concepts": ["overfitting", "regularization", "dropout", "cross-validation", "generalization", "L1", "L2"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is cross-validation? Explain k-fold cross-validation.",
     "expected_answer": "Cross-validation evaluates model performance on multiple data splits. K-fold: divide data into k equal parts; train on k-1 folds, test on 1 fold; repeat k times; average performance. More reliable than single train-test split.",
     "expected_concepts": ["cross-validation", "k-fold", "folds", "train", "test", "average", "reliable"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain the difference between precision and recall.",
     "expected_answer": "Precision = TP/(TP+FP): of all positive predictions, how many were actually positive? Recall = TP/(TP+FN): of all actual positives, how many did we catch? Trade-off: high precision = fewer false positives, high recall = fewer false negatives.",
     "expected_concepts": ["precision", "recall", "true positive", "false positive", "false negative", "trade-off"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is gradient descent and how does it work?",
     "expected_answer": "Gradient descent is an optimization algorithm that minimizes a loss function by iteratively moving in the direction of steepest descent (negative gradient). Learning rate controls step size. Variants: batch, stochastic (SGD), mini-batch.",
     "expected_concepts": ["gradient descent", "loss function", "learning rate", "optimization", "SGD", "iteration"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is the bias-variance tradeoff?",
     "expected_answer": "Bias: error from wrong assumptions (underfitting). Variance: error from sensitivity to training data fluctuations (overfitting). High bias + low variance = underfitting. Low bias + high variance = overfitting. Goal: balance both.",
     "expected_concepts": ["bias", "variance", "underfitting", "overfitting", "tradeoff", "balance"]},

    # Technical — Advanced
    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain the backpropagation algorithm in neural networks.",
     "expected_answer": "Backpropagation computes gradients of the loss function w.r.t. each weight using chain rule, propagating errors backward from output to input. These gradients are used by gradient descent to update weights to minimize loss.",
     "expected_concepts": ["backpropagation", "gradient", "chain rule", "loss function", "weights", "neural network"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is attention mechanism in transformers?",
     "expected_answer": "Attention allows a model to focus on relevant parts of the input when making predictions. Self-attention computes Q, K, V matrices; attention score = softmax(QK^T/sqrt(d_k))V. Enables transformers to handle long-range dependencies.",
     "expected_concepts": ["attention", "transformer", "Q K V", "self-attention", "softmax", "dependency"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What are the different types of regularization techniques?",
     "expected_answer": "L1 (Lasso): adds |weights| to loss, promotes sparsity (zero weights). L2 (Ridge): adds weights² to loss, shrinks weights. Elastic Net: combines L1+L2. Dropout: randomly zeros neurons during training. Data augmentation reduces overfitting.",
     "expected_concepts": ["L1", "L2", "Lasso", "Ridge", "dropout", "regularization", "sparsity"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain the difference between bagging and boosting.",
     "expected_answer": "Bagging: train multiple models in parallel on bootstrap samples, aggregate predictions (Random Forest). Reduces variance. Boosting: train models sequentially, each correcting previous errors (XGBoost, AdaBoost). Reduces bias. Boosting often more accurate but prone to overfitting.",
     "expected_concepts": ["bagging", "boosting", "Random Forest", "XGBoost", "parallel", "sequential", "variance", "bias"]},

    {"role": "AI/ML Engineer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is transfer learning? When would you use it?",
     "expected_answer": "Transfer learning uses a pre-trained model (trained on large dataset) as the starting point for a new task. Fine-tune on smaller domain-specific dataset. Use when: limited data, similar domain, high compute cost. Examples: BERT for NLP, ResNet for images.",
     "expected_concepts": ["transfer learning", "pre-trained", "fine-tuning", "limited data", "BERT", "ResNet"]},

    # HR
    {"role": "AI/ML Engineer", "category": "HR", "difficulty": "Beginner",
     "question_text": "What interests you about AI and Machine Learning?",
     "expected_answer": "Genuine excitement about AI's impact, specific areas of interest (NLP, computer vision, etc.), personal projects or learning journey, and how you see AI shaping the future.",
     "expected_concepts": ["interest", "AI", "impact", "projects", "learning", "future"]},

    {"role": "AI/ML Engineer", "category": "HR", "difficulty": "Intermediate",
     "question_text": "Describe a machine learning project you built from scratch.",
     "expected_answer": "Cover: problem definition, data collection, EDA, feature engineering, model selection, training, evaluation, deployment. Be specific about metrics achieved and lessons learned.",
     "expected_concepts": ["problem definition", "data", "EDA", "model", "training", "evaluation", "deployment"]},

    {"role": "AI/ML Engineer", "category": "HR", "difficulty": "Beginner",
     "question_text": "How do you approach a new ML problem?",
     "expected_answer": "Structured approach: understand business problem → collect and explore data (EDA) → preprocess → choose appropriate model → train and tune → evaluate with proper metrics → deploy and monitor.",
     "expected_concepts": ["structured", "EDA", "preprocessing", "model selection", "evaluation", "deployment", "monitoring"]},

    # Project
    {"role": "AI/ML Engineer", "category": "Project", "difficulty": "Intermediate",
     "question_text": "Describe an ML project you worked on. What algorithm did you use and why?",
     "expected_answer": "Describe project goal, dataset, why specific algorithm chosen (performance, interpretability, data size), how you evaluated it, and what results you achieved.",
     "expected_concepts": ["algorithm", "choice", "evaluation", "metrics", "dataset", "results"]},

    {"role": "AI/ML Engineer", "category": "Project", "difficulty": "Advanced",
     "question_text": "Have you deployed any ML model? What challenges did you face?",
     "expected_answer": "Discuss deployment approach (Flask/FastAPI/cloud), challenges: model drift, latency, scaling, versioning, monitoring, data pipeline. Solutions used to address these challenges.",
     "expected_concepts": ["deployment", "model drift", "latency", "scaling", "monitoring", "pipeline"]},

    # ─────────────────────────────────────────────────────────────
    # SQL DEVELOPER
    # ─────────────────────────────────────────────────────────────

    # Technical — Beginner
    {"role": "SQL Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is normalization? Explain 1NF, 2NF, and 3NF.",
     "expected_answer": "Normalization organizes data to reduce redundancy. 1NF: atomic values, no repeating groups. 2NF: 1NF + no partial dependencies on composite primary key. 3NF: 2NF + no transitive dependencies.",
     "expected_concepts": ["normalization", "1NF", "2NF", "3NF", "redundancy", "dependencies", "atomic"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is an index in SQL and when should you use it?",
     "expected_answer": "An index speeds up data retrieval by creating a separate lookup structure. Use on: frequently queried columns, JOIN columns, WHERE clause columns. Avoid over-indexing as it slows INSERT/UPDATE/DELETE.",
     "expected_concepts": ["index", "performance", "retrieval", "columns", "tradeoff", "INSERT", "UPDATE"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between DELETE, TRUNCATE, and DROP?",
     "expected_answer": "DELETE: removes specific rows, logged, can be rolled back, WHERE clause available. TRUNCATE: removes all rows, faster, minimal logging, can't be rolled back in some DBs, resets identity. DROP: removes entire table structure and data.",
     "expected_concepts": ["DELETE", "TRUNCATE", "DROP", "rollback", "rows", "table", "WHERE"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What are stored procedures and what are their advantages?",
     "expected_answer": "Stored procedures are precompiled SQL code stored in the database. Advantages: performance (precompiled), security (abstraction), reusability, reduce network traffic, centralized logic.",
     "expected_concepts": ["stored procedure", "precompiled", "performance", "security", "reusability", "network"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is a foreign key and how does it enforce referential integrity?",
     "expected_answer": "A foreign key is a column that references the primary key of another table. It enforces referential integrity by preventing records from being created in child table without matching parent record, and preventing deletion of parent records that have children.",
     "expected_concepts": ["foreign key", "primary key", "referential integrity", "parent", "child", "constraint"]},

    # Technical — Intermediate
    {"role": "SQL Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain different types of JOINs in SQL.",
     "expected_answer": "INNER JOIN: matching rows in both. LEFT JOIN: all left rows + matching right. RIGHT JOIN: all right rows + matching left. FULL OUTER JOIN: all rows from both. CROSS JOIN: Cartesian product. SELF JOIN: table joined with itself.",
     "expected_concepts": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN", "CROSS JOIN", "Cartesian"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is a view in SQL and when should you use it?",
     "expected_answer": "A view is a virtual table based on a SELECT query. Uses: simplify complex queries, provide security (expose only needed columns), abstract underlying schema changes. Doesn't store data (except materialized views).",
     "expected_concepts": ["view", "virtual table", "SELECT", "security", "simplify", "materialized view"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is a transaction in SQL? Explain ACID properties.",
     "expected_answer": "A transaction is a sequence of operations treated as a unit. ACID: Atomicity (all or nothing), Consistency (valid state before/after), Isolation (transactions don't interfere), Durability (committed changes persist).",
     "expected_concepts": ["transaction", "ACID", "atomicity", "consistency", "isolation", "durability", "COMMIT", "ROLLBACK"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is the difference between UNION and UNION ALL?",
     "expected_answer": "UNION combines results of two queries and removes duplicates. UNION ALL combines results keeping all rows including duplicates. UNION is slower due to deduplication. Use UNION ALL when duplicates are acceptable or impossible.",
     "expected_concepts": ["UNION", "UNION ALL", "duplicates", "combine", "performance"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What are triggers in SQL?",
     "expected_answer": "Triggers are stored procedures that automatically execute in response to INSERT, UPDATE, or DELETE events on a table. Types: BEFORE/AFTER triggers. Use for: audit logging, enforcing business rules, cascading updates.",
     "expected_concepts": ["trigger", "automatic", "INSERT", "UPDATE", "DELETE", "BEFORE", "AFTER", "audit"]},

    # Technical — Advanced
    {"role": "SQL Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is database partitioning and what are its types?",
     "expected_answer": "Partitioning divides large tables into smaller parts for performance. Types: Range (by date/value), List (by category), Hash (by hash function), Composite (multiple methods). Improves query performance on large tables by limiting scanned partitions.",
     "expected_concepts": ["partitioning", "range", "list", "hash", "performance", "large table"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "How would you design a database schema for an e-commerce system?",
     "expected_answer": "Tables: Users, Products, Categories, Orders, OrderItems, Payments, Reviews. Relationships: User has many Orders; Order has many OrderItems; OrderItem references Product. Apply normalization, add indexes on frequently queried columns.",
     "expected_concepts": ["schema design", "normalization", "relationships", "indexes", "entities", "foreign keys"]},

    {"role": "SQL Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain query execution plan and how to use it for optimization.",
     "expected_answer": "Execution plan shows how the database will execute a query: table scans, index seeks, joins, sorts. Use EXPLAIN (MySQL/PostgreSQL) or EXPLAIN PLAN (Oracle). Look for table scans on large tables, add indexes, rewrite problematic joins.",
     "expected_concepts": ["execution plan", "EXPLAIN", "table scan", "index seek", "optimization", "JOIN"]},

    # HR
    {"role": "SQL Developer", "category": "HR", "difficulty": "Beginner",
     "question_text": "Tell me about your SQL experience and the databases you've worked with.",
     "expected_answer": "Describe SQL experience, specific databases (MySQL, PostgreSQL, SQL Server, Oracle), types of queries written, performance tuning done, and any projects involving database design.",
     "expected_concepts": ["experience", "databases", "queries", "performance", "design", "projects"]},

    {"role": "SQL Developer", "category": "HR", "difficulty": "Intermediate",
     "question_text": "Describe a challenging SQL query or database design problem you solved.",
     "expected_answer": "Use STAR: describe the data problem, approach taken, SQL techniques used (CTEs, window functions, indexes), and the result/performance improvement achieved.",
     "expected_concepts": ["STAR", "challenge", "solution", "technique", "performance", "result"]},

    # Project
    {"role": "SQL Developer", "category": "Project", "difficulty": "Intermediate",
     "question_text": "Describe a database you designed. What design decisions did you make?",
     "expected_answer": "Cover: ER diagram design, normalization decisions, indexing strategy, choice of data types, handling of relationships, and any performance considerations.",
     "expected_concepts": ["ER diagram", "normalization", "indexing", "data types", "relationships", "performance"]},

    # ─────────────────────────────────────────────────────────────
    # SOFTWARE DEVELOPER
    # ─────────────────────────────────────────────────────────────

    # Technical — Beginner
    {"role": "Software Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between a stack and a queue?",
     "expected_answer": "Stack follows LIFO (Last In First Out) — like a stack of plates. Operations: push, pop. Queue follows FIFO (First In First Out) — like a queue/line. Operations: enqueue, dequeue. Stack used for function calls, undo; Queue for scheduling, BFS.",
     "expected_concepts": ["stack", "queue", "LIFO", "FIFO", "push", "pop", "enqueue", "dequeue"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is Object-Oriented Programming? Explain its four pillars.",
     "expected_answer": "OOP organizes code into objects with data and behavior. Four pillars: Encapsulation (hiding internal state), Inheritance (inheriting properties from parent), Polymorphism (same interface, different behavior), Abstraction (hiding complexity, showing only essentials).",
     "expected_concepts": ["OOP", "encapsulation", "inheritance", "polymorphism", "abstraction", "object", "class"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between an array and a linked list?",
     "expected_answer": "Array: fixed size, contiguous memory, O(1) random access, O(n) insert/delete. Linked list: dynamic size, non-contiguous memory, O(n) access, O(1) insert/delete at known position. Arrays better for reads, linked lists for frequent inserts/deletes.",
     "expected_concepts": ["array", "linked list", "memory", "access", "O(1)", "O(n)", "dynamic"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is the difference between HTTP and HTTPS?",
     "expected_answer": "HTTP (HyperText Transfer Protocol) transfers data in plain text — insecure. HTTPS adds SSL/TLS encryption, providing security, data integrity, and authentication. HTTPS uses port 443, HTTP uses port 80. HTTPS required for sensitive data.",
     "expected_concepts": ["HTTP", "HTTPS", "SSL", "TLS", "encryption", "security", "port"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Beginner",
     "question_text": "What is version control and why is Git important?",
     "expected_answer": "Version control tracks changes to code over time. Git is a distributed VCS. Important for: collaboration (branching/merging), history tracking, rollback capability, code review (PRs), CI/CD integration. Standard in professional software development.",
     "expected_concepts": ["version control", "Git", "branching", "merging", "collaboration", "history", "rollback"]},

    # Technical — Intermediate
    {"role": "Software Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is a REST API? Explain its key principles.",
     "expected_answer": "REST (Representational State Transfer) is an architectural style for web APIs. Principles: Stateless (no client state on server), Client-Server, Uniform Interface (resources identified by URLs), Layered System, Cacheable. Uses HTTP methods: GET, POST, PUT, DELETE.",
     "expected_concepts": ["REST", "stateless", "HTTP methods", "GET", "POST", "PUT", "DELETE", "resource", "URL"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "Explain the concept of time complexity and Big O notation.",
     "expected_answer": "Time complexity measures how runtime grows with input size. Big O notation: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n²) quadratic, O(2^n) exponential. Lower is better for large inputs.",
     "expected_concepts": ["time complexity", "Big O", "O(1)", "O(n)", "O(n²)", "runtime", "input size"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What are design patterns? Name and explain 3 common ones.",
     "expected_answer": "Design patterns are reusable solutions to common problems. Singleton (one instance), Factory (create objects without specifying class), Observer (notify subscribers of state changes). Categorized as Creational, Structural, Behavioral.",
     "expected_concepts": ["design pattern", "Singleton", "Factory", "Observer", "Creational", "Structural", "Behavioral"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is the difference between synchronous and asynchronous programming?",
     "expected_answer": "Synchronous: operations execute sequentially, blocking until each completes. Asynchronous: operations can run concurrently without blocking, using callbacks/promises/async-await. Async is better for I/O-bound operations to improve throughput.",
     "expected_concepts": ["synchronous", "asynchronous", "blocking", "callback", "promise", "async", "await", "concurrent"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Intermediate",
     "question_text": "What is Docker and why is it useful?",
     "expected_answer": "Docker is a containerization platform that packages applications with dependencies into portable containers. Benefits: consistent environment across dev/prod, isolation, scalability, faster deployment. Uses Dockerfile to define container image.",
     "expected_concepts": ["Docker", "container", "containerization", "isolation", "portable", "Dockerfile", "image"]},

    # Technical — Advanced
    {"role": "Software Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is microservices architecture? Compare with monolithic.",
     "expected_answer": "Microservices: application broken into small, independent services each with own DB. Benefits: independent deployment, scalability, technology flexibility. Drawbacks: distributed system complexity, network overhead. Monolithic: simpler for small apps, single deployable unit.",
     "expected_concepts": ["microservices", "monolithic", "independent", "deployment", "scalability", "distributed", "service"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "What is CI/CD and how does it improve software development?",
     "expected_answer": "CI (Continuous Integration): automatically build and test code on each commit. CD (Continuous Delivery/Deployment): automatically deploy to staging/production after tests pass. Reduces manual errors, enables faster releases, improves code quality.",
     "expected_concepts": ["CI/CD", "continuous integration", "continuous deployment", "automation", "testing", "pipeline"]},

    {"role": "Software Developer", "category": "Technical", "difficulty": "Advanced",
     "question_text": "Explain SOLID principles in software design.",
     "expected_answer": "S: Single Responsibility (one reason to change). O: Open/Closed (open for extension, closed for modification). L: Liskov Substitution (subtypes substitutable for base types). I: Interface Segregation (specific interfaces). D: Dependency Inversion (depend on abstractions).",
     "expected_concepts": ["SOLID", "Single Responsibility", "Open/Closed", "Liskov", "Interface Segregation", "Dependency Inversion"]},

    # HR
    {"role": "Software Developer", "category": "HR", "difficulty": "Beginner",
     "question_text": "Tell me about your software development experience and tech stack.",
     "expected_answer": "Cover: languages known (Python, Java, JS, etc.), frameworks used, types of applications built (web, mobile, APIs), team experience, and most significant project.",
     "expected_concepts": ["languages", "frameworks", "projects", "team", "experience", "stack"]},

    {"role": "Software Developer", "category": "HR", "difficulty": "Intermediate",
     "question_text": "How do you handle bugs or technical debt in a project?",
     "expected_answer": "Systematic approach: reproduce bug → isolate cause → fix with tests → document. Technical debt: prioritize with product team, refactor incrementally, maintain code quality standards, use code reviews.",
     "expected_concepts": ["debugging", "reproduce", "fix", "testing", "technical debt", "refactoring", "code review"]},

    {"role": "Software Developer", "category": "HR", "difficulty": "Beginner",
     "question_text": "How do you approach learning a new programming language or framework?",
     "expected_answer": "Structured approach: official docs and tutorials, build a small project, read source code, join community (Discord, forums), practice daily, build progressively complex projects.",
     "expected_concepts": ["documentation", "practice", "projects", "community", "structured learning"]},

    # Project
    {"role": "Software Developer", "category": "Project", "difficulty": "Intermediate",
     "question_text": "Walk me through a software project you're most proud of.",
     "expected_answer": "Describe: project purpose, your role, technologies used, architecture decisions made, challenges overcome, and the impact or results of the project.",
     "expected_concepts": ["purpose", "role", "technologies", "architecture", "challenges", "impact"]},

    {"role": "Software Developer", "category": "Project", "difficulty": "Intermediate",
     "question_text": "How did you ensure code quality in your projects?",
     "expected_answer": "Code reviews, unit testing, integration testing, linting/formatters, type checking, documentation, following coding standards, CI/CD pipeline with automated tests.",
     "expected_concepts": ["code review", "unit testing", "linting", "documentation", "standards", "CI/CD", "quality"]},
]
