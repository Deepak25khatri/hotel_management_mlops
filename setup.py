from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "hotel_management",
    version = "1.0",
    author = "Deepak",
    packages = find_packages(),
    install_requires = requirements,
    
)