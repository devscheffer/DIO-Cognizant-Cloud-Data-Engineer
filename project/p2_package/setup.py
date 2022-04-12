from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="huffman-sch",
    version="0.0.1",
    author="scheffer",
    author_email="my_email",
    description="text compression using Huffman algorithm",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devscheffer/DIO-Cognizant-Cloud-Data-Engineer",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
