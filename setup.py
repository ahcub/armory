from distutils.core import setup

from setuptools import find_packages

setup(
    name='devut',
    packages=find_packages(include=('algorithms', 'os_utils', 'algorithms.*')),
    version='0.0.5',
    description='dev utils to reduce copy paste',
    author='Alex Buchkovsky',
    author_email='olex.buchkovsky@gmail.com',
    url='https://github.com/ahcub/armory',
    download_url='https://github.com/ahcub/armory/tarball/0.0.5',
    keywords=['logging', 'path', 'dirs', 'files'],
)
