from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in imperial_design_app/__init__.py
from imperial_design_app import __version__ as version

setup(
	name="imperial_design_app",
	version=version,
	description="An app for Imperial_Design listing",
	author="Devi",
	author_email="devieorchids@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
