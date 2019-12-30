import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cuba_weather-correaleyval", # Replace with your own username
    version="0.0.2",
    scripts=['cuba-weather'],
    author="Cuban OpenSource",
    author_email="correaleyval@gmail.com",
    description="Python3 client for (https://www.redcuba.cu) weather API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/correaleyval/cuba-weather",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)