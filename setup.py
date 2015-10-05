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
    url='github',
    install_requires=['Click', 'Requests'],
    test_suite='nose.collector',
    test_requires=['coverage', 'nose'],
    entry_points={
        'console_scripts': [
            'wunderapi=wunderapi:cli'
        ],
    },
)
