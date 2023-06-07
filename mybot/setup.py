from setuptools import setup, find_packages

setup(
      name='personal-helper',
      version='1.0',
      py_modules=['main'],
      description='It`s a personal helper, witch can be use like the address book, notes manager and file sorter.',
      url='https://github.com/pvtokun/project_team-6-',
      author='Назар, Віталій х2, Влад, Віктор',
      author_email='evciu97@gmail.com',
      license='MIT',
      install_requires=[
            'Click',
      ],
      entry_points='''
            [console_scripts]
            personal-helper=main:personal_helper
      ''',
      packages=find_packages()
)
