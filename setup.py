from setuptools import find_packages, setup
from typing import List

def get_requirements(file_name:str)->List[str]:
        """
            This function creates a list of libraries out of the requirements.txt file
        """
        libraries = []
        minus_e_dot = "-e ."
        with open(file_name) as file:
            lines = file.readlines()
            for line in lines:
                libraries.append(line.replace("\n", ""))
        if minus_e_dot in libraries:
             libraries.remove(minus_e_dot)
        return libraries

setup (
    name = 'END_TO_END', 
    version = '0.0.1',
    author = 'Jeet',
    author_email = 'jeetkhamar2022@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)