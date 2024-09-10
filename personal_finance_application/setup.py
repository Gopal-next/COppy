from setuptools import setup

setup(
    name='mypackage',
    version='0.1',
    py_modules=['project.main'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=project.main:cli
    ''',
)
