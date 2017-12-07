import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "todev",
    version = "0.0.1",
    author = "Mikaeil Orfanian",
    author_email = "mokt@outlook.com",
    description = ("A note-taking app for software developers"),
    license = "BSD",
    keywords = "productivity note-taking",
    url = "http://packages.python.org/todev",
    packages=['todev'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
