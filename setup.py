from setuptools import setup, find_packages


setup(
    name="chansons",
    version="1.0.0",
    packages=find_packages(exclude=("unittests",)),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "songbook=chansons.book:main",
        ],
    },
)
