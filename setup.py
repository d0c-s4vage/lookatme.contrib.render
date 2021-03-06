"""
Setup for lookatme.contrib.render
"""


from setuptools import setup, find_namespace_packages
import os


req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
with open(req_path, "r") as f:
    required = f.read().splitlines()


readme_path = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme_path, "r") as f:
    readme = f.read()


setup(
    name="lookatme.contrib.render",
    version="{{VERSION}}",
    description="A renderer of code-block -> png for lookatme. Also requires an image-rendering extension",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/d0c-s4vage/lookatme.contrib.render",
    author="James Johnson",
    author_email="d0c.s4vage@gmail.com",
    python_requires=">=3.6",
    install_requires=required,
    packages=find_namespace_packages(include=["lookatme.*"]),
    classifiers=[
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Software Development :: Documentation",
    ],
)
