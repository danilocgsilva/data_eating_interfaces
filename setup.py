from setuptools import setup, find_packages

setup(
    name="data_eating_interfaces",
    version="0.2.0",
    packages=find_packages(),
    python_requires=">=3.7",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    description="A data eating interface package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danilocgsilva/data_eating_interfaces",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)