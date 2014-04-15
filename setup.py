import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='fakery',
    version='0.1',
    author='Gary Johnson',
    author_email = 'gary@gjtt.com',
    description = '',
    install_requires=['fudge'],
    tests_require=['fudge'],
    license = 'MIT License',
    py_modules = ['fakery'],
    entry_points = {
        'nose.plugins.0.10': [
            'fakery = fakery:Fakery'
            ]
        }

    )
