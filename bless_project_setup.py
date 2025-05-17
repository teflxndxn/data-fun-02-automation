# File: bless_project_setup.py

"""
Purpose: Project 2 - Practice Python Fundamentals  
Author: Blessing Aganaga
"""

# ----------------------------------
# Import your custom module
# ----------------------------------
import utils_bless

import os

# ----------------------------------
# Additional Functions for Project 2
# ----------------------------------

def repeat_message(message: str, times: int) -> None:
    """Repeat a message a number of times."""
    for i in range(times):
        print(f"{i+1}: {message}")

def get_long_state_names(states: list) -> list:
    """Return state names longer than 10 characters."""
    return [state for state in states if len(state) > 10]

def describe_population(pop: int) -> str:
    """Describe population size."""
    if pop > 20_000_000:
        return "Huge population!"
    elif pop > 10_000_000:
        return "Large population."
    else:
        return "Smaller population."

def get_most_populous_state(states_with_population: dict) -> tuple:
    """Return the state with the highest population."""
    most_populous = ("", 0)  # (state, population)
    for state, population in states_with_population.items():
        if population > most_populous[1]:
            most_populous = (state, population)
    return most_populous

# Place this function outside main()
def create_project_directories(base_path, dir_names):
    for name in dir_names:
        dir_path = os.path.join(base_path, name)
        os.makedirs(dir_path, exist_ok=True)
        # Optional: create a README inside each folder for clarity
        with open(os.path.join(dir_path, "README.md"), "w") as f:
            f.write(f"# {name}\nThis folder is for {name}")

# ----------------------------------
# Main Function
# ----------------------------------

def main():

    print("\nWelcome to Blessing Analytics!\n")
    print(utils_bless.get_byline())

    # Call repeat message
    repeat_message("Data is powerful!", 3)

    # Population dictionary in millions
    states_with_population = {
        "California": 39.14,
        "Texas": 30.03,
        "Florida": 22.24,
        "New York": 19.84,
        "Pennsylvania": 12.96,
        "Illinois": 12.58,
        "Ohio": 11.78,
        "Georgia": 11.03,
        "North Carolina": 10.82,
        "Michigan": 10.03
    }

    # Long state names
    long_states = get_long_state_names(states_with_population.keys())
    print("\nLong state names:", long_states)

    # Describe California's population
    description = describe_population(39_140_000)
    print("\nCalifornia population description:", description)

    # Most populous state
    state, pop = get_most_populous_state(states_with_population)
    print(f"\nMost Populous State: {state} with a population of {pop} million")
    
    # List of directories you want to create
    directories = [
        "data", "scripts", "notebooks", "images", "reports",
        "models", "tests", "docs", "exports", "logs", "temp"
    ]

    # Call directory creation function inside 'MyProject/'
    create_project_directories('MyProject', directories)

# ----------------------------------
# Conditional Script Execution
# ----------------------------------

if __name__ == "__main__":
    main()
