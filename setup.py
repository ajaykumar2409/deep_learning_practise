import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ajaykumar2409", # Replace with your own username
    version="None",
    author="Ajay kumar",
    author_email="ajaylearnml@gmail.com",
    description="A testCases package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajaykumar2409/deep_learning_practise",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
