import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "validPy",
    version = "0.0.1",
    author = "Joli Holmes",
    author_email = "holmesjoli@gmail.com",
    description = "Python package for data validation",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/holmesjoli/validPy",
    packages = setuptools.find_packages(),
    install_requires=[
        'numpy==1.16.2',
        'pandas==0.24.2',
        'pytest==4.3.1'
    ]
)
