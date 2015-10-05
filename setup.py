#!usr/bin/python

from distutils.core import setup

setup(
    name='wunderapi',
    version='0.3.3',
    description='A wrapper for the Weather Underground Rest API.',
    author='Jason Paris',
    author_email='paris3200@gmail.com',
    package='wunderapi',
    package_dir={'': 'wunderapi'},
    url='URL to get it at.',
    install_requires=['nose', 'Click', 'Requests'],
    entry_points={
        'console_scripts': [
            'wunder=wunderapi:cli'
        ],
    },
)
