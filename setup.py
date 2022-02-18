from setuptools import setup
import re
import os
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

# Copying module
import site
copyfrom = "/".join(__file__.split("/")[:-1] + ["campfire"])
copyto = site.getsitepackages()[0] + "/campfire"
if os.path.exists(copyto):
    rmtree(copyto)
copytree(copyfrom, copyto)

setup(
    name="campfire.py",
    version=version,
    install_requires=requirements,
    python_requires=">=2.7",
    description="Campfire API",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Camper-CoolDie",
    author_email="campercooldie@yandex.ru",
    url="https://github.com/Camper-CoolDie/campfire.py",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)