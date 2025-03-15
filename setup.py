from setuptools import setup, find_packages

setup(
    name="argconfig",
    version="0.1.0",
    author="Jun Hu",
    author_email="hujunxianligong@gmail.com",
    description="A lightweight configuration management library using dataclasses and argparse",
    long_description="A lightweight configuration management library using dataclasses and argparse",
    # long_description_content_type="text/markdown",
    url="https://github.com/CrawlScript/argconfig",
    packages=find_packages(exclude=["demo_argconfig.py"]),
    install_requires=[],
    python_requires=">=3.6",
)
