from setuptools import setup, find_packages

setup(
    name='main',
    version='0.1.0',
    py_modules= find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        mypackage=main:cli
    ''',
)
