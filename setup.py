import setuptools 

with open("README.md", "r", encoding="utf-8") as f:    # Read the README.md file
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Machine-learning-Project-MLflow"
AUTHOR_USER_NAME = "MalikZeeshan1122"
SRC_REPO = "MyProject"
AUTHOR_EMAIL = "malikzeeshan3.1417@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your project's dependencies here.
    ],
)