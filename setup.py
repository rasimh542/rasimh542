# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rasim_project",
    version="0.1.0",
    author="Your Name",
    author_email="your-email@example.com",
    description="A short description of the package",
    long_description=long_description,
    long_description_content_type="text/markdown",  # or "text/x-rst" if using reStructuredText
    packages=find_packages(),
    install_requires=[],
    # Other metadata...
)
