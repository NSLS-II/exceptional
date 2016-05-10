#!/usr/bin/env python

from setuptools import setup

import versioneer

required = open('requirements.txt').read().split('\n')

setup(
    name='exceptional',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Report exceptions to the NSLS2 DAMA slack chat',
    author='ericdill',
    author_email='edill@bnl.gov',
    url='https://github.com/nsls-ii/exceptional',
    packages=['exceptional'],
    install_requires=required,
    long_description='See ' + 'https://github.com/nsls-ii/exceptional',
    license='BSD 3-clause',
    entry_points="""
    [console_scripts]
    exceptional=exceptional.app:start
    """

)
