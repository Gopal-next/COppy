from setuptools import setup

setup(
    name='mypackage',
    version='0.1',
    py_modules=['personal_finance_application.project.main'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=personal_finance_application.project.main:cli
    ''',
)
