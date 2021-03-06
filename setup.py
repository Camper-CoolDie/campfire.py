from setuptools import setup
import re
import os
import sys
from shutil import rmtree, copytree

requirements = []
with open("requirements.txt", "r") as f:
    requirements = f.read().split("\n")

version = None
with open("campfire/__init__.py", "r") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("__version__ is not set")

readme = ""
with open("README.rst", "r") as f:
    readme = f.read()

package_data = {
    "": ["components/cert.pem"]
}

packages = (
    "campfire",
    "campfire.components",
    "campfire.components.reqs",
    "campfire.components.reqs.request",
    "campfire.components.models",
    "campfire.components.models.publications"
)

setup(
    name="campfire",
    version=version,
    packages=packages,
    package_data=package_data,
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
    description="Campfire API",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Camper-CoolDie",
    author_email="campercooldie@gmail.com",
    url="https://github.com/Camper-CoolDie/campfire.py",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)