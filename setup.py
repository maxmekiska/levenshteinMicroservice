import os

from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as file:
    long_description = file.read()

setup(
    author="Maximilian Mekiska",
    author_email="maxmekiska@gmail.com",
    description="Microservice example.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="service",
    version="0.0.1",
    packages=find_packages(include=["service", "service.*"]),
    install_requires=[
        "click==8.1.3",
        "colorama==0.4.6",
        "Flask==2.2.2",
        "importlib-metadata==5.1.0",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.1",
        "Werkzeug==2.2.2",
        "zipp==3.11.0",
        "Levenshtein==0.20.8"
    ],
    python_rquieres="== 3.8.*",
)