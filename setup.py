#!/usr/bin/env python

"""The setup script."""


from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'mock',
    'numpy',
    'matplotlib',
    'pygraphviz',
    'dill']

setup_requirements = []

test_requirements = []

setup(
    author="Steven K Terry",
    author_email='stkterry@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Collatz sequence visualization and exploration.",
    entry_points={
        'console_scripts': [
            'c=collatzpy.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='collatzpy',
    name='collatzpy',
    packages=find_packages(include=['collatzpy', 'collatzpy.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/stkterry/collatzpy',
    version='0.1.0',
    zip_safe=False,
    data_files=[

    ]
)
