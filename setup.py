import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup_kwargs = {
	'name' : "magicjson",
	'version' : "0.0.1",
	'author' : "Henk Hogan",
	'author_email' : "henkhogan@gmail.com",
	'description' : ("The author is lazy"),
	'license' : "N/A",
	'keywords' : "N/A",
	'url' : "N/A",
	'packages' : ["magicjson"],
	'dependency_links' : [],
	'long_description' : read('README.md'),
	'classifiers' : [
		"Development Status :: 3 - Alpha",
		"Topic :: Utilities",
		"License :: OSI Approved :: BSD License",
		],
}

if __name__ == '__main__':
	setup(**setup_kwargs)
