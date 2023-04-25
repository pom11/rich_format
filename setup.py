#!/usr/bin/env python

__author__ = "pom11"
__copyright__ = "Copyright 2023, Parsec Original Mastercraft S.R.L."
__license__ = "MIT"
__version__ = "0.0.4"
__maintainer__ = "pom11"
__email__ = "office@parsecom.ro"

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
	readme = readme_file.read()

requirements = ["rich","textual"]

setup_requirements = [ ]


setup(
	author="pom11",
	author_email='office@parsecom.ro',
	python_requires='>=3.6',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
	],
	description="Format rich Text",
	entry_points={
		'console_scripts': [
			'rich_format.test=rich_format.test:console_test',
			"rich_format.demo=rich_format.app:run"
		],
	},
	install_requires=requirements,
	license="MIT license",
	long_description=readme,
	long_description_content_type="text/markdown",
	include_package_data=True,
	keywords='rich',
	name='rich_format',
	packages=find_packages(include=['rich_format', 'rich_format.*']),
	setup_requires=setup_requirements,
	url='https://github.com/pom11/rich_format',
	version='0.0.4',
	zip_safe=True,
)