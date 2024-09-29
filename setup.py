from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ecowater_softener",
    version="2.1.3",
    author="barleybobs",
    description="A small package to pull data from Ecowater water softeners",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barleybobs/ecowater-softener",
    install_requires=[
        "ayla-iot-unofficial==1.4.1"
    ],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
