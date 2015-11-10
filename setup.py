#!usr/bin/python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='wunderapi',
    version='0.3.3',
    description='A wrapper for the Weather Underground Rest API.',
    author='Jason Paris',
    author_email='paris3200@gmail.com',
    package='wunderapi',
    package_dir={'': 'wunderapi'},
    url='https://github.com/paris3200/wunderapi',
    install_requires=['Click', 'Requests'],
    test_requires=['coverage', 'nose'],
    test_suite='nose.collector',
    entry_points={
        'console_scripts': [
            'wunderapi=wunderapi:cli'
        ],
    },
)
