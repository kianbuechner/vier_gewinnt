import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vier_gewinnt_kianbuechner",
    version="1.0.1",
    author="Kian Büchner",
    author_email="kbuechner@stud.macromedia.de",
    description="Vier Gewinnt mit OOP verbessert",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kianbuechner/vier_gewinnt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
