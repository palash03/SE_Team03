import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="se20-hw1-package", # Replace with your own username
    version="0.0.1",
    author="z03",
    author_email="ajain37@ncsu.edu",
    description="A small example package for the creating a github project structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/palash03/SE_Team03",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)