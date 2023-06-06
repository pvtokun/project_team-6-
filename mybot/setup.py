from setuptools import setup, find_packages

setup(
    name='mybot',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mybot = mybot.main:main',
        ],
    },
    author='Your Name',
)
