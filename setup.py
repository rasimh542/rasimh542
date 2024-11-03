# setup.py
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="your_package_name",
    version="0.1.0",
    author="Your Name",
    author_email="your-email@example.com",
    description="A short description of the package",
    long_description=long_description,
    long_description_content_type="text/markdown",  # or "text/x-rst" if using reStructuredText
    packages=["your_package_name"],
    install_requires=[],
    # Other metadata...
)
