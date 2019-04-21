from setuptools import setup

setup(
    name='alphabetsoup',
    author='Joan A. Pinol  (japinol)',
    version='1.0.2',
    license='MIT',
    description='Alphabet Soup Solver.',
    long_description='Alphabet Soup Solver v. 1.0.2. Solves an alphabet soup finding a given list of words inside it.',
    url='https://github.com/japinol7/alphabetsoup',
    packages = ['alphabetsoup'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'alphabetsoup=alphabetsoup.__main__:main',
        ],
    },
)
