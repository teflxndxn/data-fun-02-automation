# data-fun-02-automation
# Blessing's Project Setup (DataFun-02)

## Project Overview

This project demonstrates automation with Python using core programming concepts from Chapters 3 and 4 of the Python textbook. It reinforces key skills such as:

- Repetition (loops)
- Branching (conditional logic)
- Functions and modular code design
- Dictionaries and list comprehensions
- Professional workflow using Git and virtual environments

It also builds on work completed in Module 1 by importing a `utils` module and following the repeatable workflow outlined in the `pro-analytics-01` guide.

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

## **Folder Creation Automation**

Using the provided Python script, many project folders such as `data`, `scripts`, `notebooks`, `reports`, and others were automatically generated, including README files for each. The script executed successfully, creating a well-structured project directory, verified by the screenshot of the folder structure in VS Code.

---

##  **Output**

```text
Welcome to Blessing Analytics!

Blessing Aganaga - Data Analyst in Training

1: Data is powerful!
2: Data is powerful!
3: Data is powerful!

Long state names: ['Pennsylvania', 'North Carolina']

California population description: Huge population!

Most Populous State: California with a population of 39.14 million

### Project structure

data-fun-02-automation/
│
├── .venv/                   # Virtual environment
├── utils_blessing.py        # Imported utility module from Module 1
├── blessing_project_setup.py # Main Python script for this module
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Files and folders to ignore in Git

Your README is quite comprehensive, but I recommend a few improvements for clarity, formatting, and professionalism. Here’s a polished, organized, and complete version you can copy and paste directly into your README.md. It emphasizes your work, clarifies instructions, and improves readability:
markdown
Copy
# data-fun-02-automation
# Blessing's Project Setup (DataFun-02)

## Project Overview

This project demonstrates automation with Python using core programming concepts from Chapters 3 and 4 of the Python textbook. It reinforces key skills such as:

- Repetition (loops)
- Branching (conditional logic)
- Functions and modular code design
- Dictionaries and list comprehensions
- Professional workflow using Git and virtual environments

It also builds on work completed in Module 1 by importing a `utils` module and following the repeatable workflow outlined in the `pro-analytics-01` guide.

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

## **Folder Creation Automation**

Using the provided Python script, many project folders such as `data`, `scripts`, `notebooks`, `reports`, and others were automatically generated, including README files for each. The script executed successfully, creating a well-structured project directory, verified by the screenshot of the folder structure in VS Code.

---

##  **Output**

```text
Welcome to Blessing Analytics!

Blessing Aganaga - Data Analyst in Training

1: Data is powerful!
2: Data is powerful!
3: Data is powerful!

Long state names: ['Pennsylvania', 'North Carolina']

California population description: Huge population!

Most Populous State: California with a population of 39.14 million
Project Structure

text
Copy
data-fun-02-automation/
│
├── .venv/                   # Virtual environment
├── utils_blessing.py        # Imported utility module from Module 1
├── blessing_project_setup.py # Main Python script for this module
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Files and folders to ignore in Git
How to Run

Clone the project or open your existing folder.
Activate your virtual environment:
source .venv/bin/activate (Mac/Linux)
.venv\Scripts\activate (Windows)

run the scrip:
python bless_project_setup.py

###Version Control & Workflow

Cloned and updated from GitHub.
Resolved merge conflicts and ensured code is clean.
The project adheres to best practices with modular functions and clear structure.
Regular commits and pushes to maintain version control.

##How to Push Changes to GitHub
Ensure your local repo is up to date: git pull
Stage your changes:git add .
Commit with a descriptive message:git commit -m "Added folder creation automation and updated README"
Push to GitHub:git push origin main
