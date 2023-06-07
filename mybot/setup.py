from setuptools import setup

setup(
    name='personal-helper',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        personal-helper=main:personal_helper
    '''
)
