try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='wunderapi',
    version='0.1',
    description='A wrapper for the Weather Underground Rest API.',
    author='Jason Paris',
    author_email='paris3200@gmail.com',
    license='MIT',
    package='wunderapi',
    url='https://github.com/paris3200/wunderapi',
    install_requires=['Click', 'Requests'],
    test_suite='nose.collector',
    test_require=['coverage', 'nose'],
    entry_points={
        'console_scripts': ['wunderapi = wunderapi.cli:cli'],
        }
)
