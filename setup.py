from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [requirement.replance("\n", "") for requirement in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements

setup(
    name="hypozen",
    version="0.1.0",
    description="A library for automated hypothesis testing with parametric and non-parametric methods.",
    author="ariqlubis",
    author_email="ariqf.lubis@gmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
)
