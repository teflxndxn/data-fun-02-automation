# data-fun-02-automation  
# Blessing's Project Setup (DataFun-02)

## Project Overview

This project demonstrates automation with Python using core programming concepts from Chapters 3 and 4 of the Python textbook. It reinforces key skills such as:

- Repetition (loops)
- Branching (conditional logic)
- Functions and modular code design
- Dictionaries and list comprehensions
- Professional workflow using Git and virtual environments

It also builds on work completed in Module 1 by importing a `utils` module and continuing to follow the repeatable workflow outlined in the `pro-analytics-01` guide.

---

## Features & Functions

### `repeat_message(message, times)`
Prints a message multiple times using a `for` loop.

### `get_long_state_names(states)`
Returns U.S. state names longer than 10 characters using a list comprehension.

### `describe_population(pop)`
Categorizes a given population using conditional logic:
- "Huge" for over 30 million  
- "Large" for over 10 million  
- "Smaller" otherwise

### `get_most_populous_state(states_with_population)`
Accepts a dictionary of states with population values and returns the state with the highest population.

---

## Example Output

```text
Welcome to Blessing Analytics!

Blessing Aganaga - Data Analyst in Training

1: Data is powerful!
2: Data is powerful!
3: Data is powerful!

Long state names: ['Pennsylvania', 'North Carolina']

California population description: Huge population!

Most Populous State: California with a population of 39.14 million
```

---

## Project Structure

```
data-fun-02-automation/
│
├── .venv/                   # Virtual environment
├── utils_blessing.py        # Imported utility module from Module 1
├── blessing_project_setup.py # Main Python script for this module
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Files and folders to ignore in Git
```

---

##  How to Run

1. Clone the project or open your existing folder.
2. Activate your virtual environment:  
   `source .venv/bin/activate` (Mac/Linux) or `.venv\Scripts\activate` (Windows)
3. Run the script:  
   `python blessing_project_setup.py`

---

## Professional Workflow Used

- Git version control
- GitHub repository
- Virtual environment management
- Modular programming with reusable functions
- Python best practices: `main()` function and conditional execution

---

 ## How to Push to GitHub

1. Initialize a local Git repo if not already done:  
   `git init`

2. Add files to staging:  
   `git add .`

3. Commit your changes:  
   `git commit -m "Initial commit"`

4. Add your remote GitHub repo:  
   `git remote add origin 

5. Push your code:  
   `git push -u origin main` (or `master`, depending on your default branch)

