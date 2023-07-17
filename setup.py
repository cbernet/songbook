from setuptools import setup, find_packages


setup(
    name="songbook",
    version="1.0.0",
    packages=find_packages(exclude=("unittests",)),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "songbook=songbook.book:main",
        ],
    },
)
