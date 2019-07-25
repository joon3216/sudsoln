import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudsoln",
    version="0.0.14",
    author="Junkyu Park",
    author_email="joon3216@gmail.com",
    description="A n ** 2-by-n ** 2 sudoku solver.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joon3216/sudsoln",
    packages=setuptools.find_packages(),
    python_requires='>=3',
    # install_requires=['numpy'],
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
