from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fivestarstours_dev/__init__.py
from fivestarstours_dev import __version__ as version

setup(
	name="fivestarstours_dev",
	version=version,
	description="Five Stars Tours Development App",
	author="Karim K",
	author_email="karim.kashmar@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
