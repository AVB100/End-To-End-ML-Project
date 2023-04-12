# Importing required modules
from setuptools import find_packages, setup
from typing import List


# Define a function to get requirements from a file
def get_requirements(file_name: str) -> List[str]:
    # Initialize an empty list to store the requirements
    libraries = []
    # Define a string to check for in the requirements
    minus_e_dot = "-e ."
    # Open the file specified by file_name argument
    with open(file_name) as file:
        # Read all the lines from the file
        lines = file.readlines()
        # Iterate over each line
        for line in lines:
            # Remove trailing newline and append to libraries list
            libraries.append(line.replace("\n", ""))
    # Check if "-e ." is present in libraries list
    if minus_e_dot in libraries:
        # Remove "-e ." from libraries list
        libraries.remove(minus_e_dot)
    # Return the parsed requirements as a list of strings
    return libraries


# Set up the package details
setup(
    # Package name
    name='End to End Student Score Prediction',
    # Package version
    version='0.0.1',
    # Author name
    author='Jeet',
    # Author email
    author_email='jeetkhamar2022@gmail.com',
    # Find and include all packages in the package
    packages=find_packages(),
    # Use parsed requirements as dependencies
    install_requires=get_requirements('requirements.txt')
)