try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

print(find_packages())

setup(
    name="wunderapi",
    version='0.1',
    description='A wrapper for the Weather Underground Rest API.',
    author='Jason Paris',
    author_email='paris3200@gmail.com',
    license='MIT',
    url='https://github.com/paris3200/wunderapi',
    packages=find_packages(),
    install_requires=['Click', 'Requests', 'terminaltables'],
    test_suite='nose.collector',
    entry_points={
        'console_scripts': ['weather = wunderapi.cli:cli'],
        }
)
