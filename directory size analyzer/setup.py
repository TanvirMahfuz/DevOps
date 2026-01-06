from setuptools import setup, find_packages

setup(
    name="diskpeek",
    version="1.0.0",
    description="Colored cumulative directory size analyzer",
    author="Tanvir Mahfuz Apurba",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "diskpeek = diskpeek.cli:main"
        ]
    },
    python_requires=">=3.8",
)
