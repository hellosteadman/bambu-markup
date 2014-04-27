#!/usr/bin/env python
from distutils.core import setup

setup(
	name = 'bambu-markup',
	version = '2.0',
	description = 'Replacements for Django\'s Markdown and reStructuredText support',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'http://pypi.python.org/pypi/bambu-markup',
    long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	install_requires = [
		'Django>=1.4',
		'markdown',
		'docutils'
	],
	packages = [
		'bambu.markup',
		'bambu.markup.templatetags'
	],
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)