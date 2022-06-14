import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.6'
DESCRIPTION = 'A Python CLI tool for displaying Quotes'
LONG_DESCRIPTION = 'QuotesPy is Scraping tool that Displays Quotes as a notification or deirectely to the console.'

# Setting up
setup(
    name="quotescli",
    version=VERSION,
    author="ramsy (Mohamed Said EL-yemlahi)",
    author_email="<0ramsy0@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=  [ "pyler",
                         "colorama",
                         "bs4 ",
                         "prettytable"
                ],
    keywords=["Quotes", "Python", "scraping", "notification", "cli"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
