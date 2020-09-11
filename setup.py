
# python
import pathlib
import setuptools

README_FILE_PATH = pathlib.Path(__file__).parent.absolute().joinpath(
    'README.md',
)
with open(README_FILE_PATH) as f:
    long_description = f.read()

setuptools.setup(
    name='wkd',
    version='0.0.1',
    author='Erik Soma',
    author_email='stillusingirc@gmail.com',
    description='Game Development Library',
    tests_require=['pytest'],
    install_requires=[],
    extras_require={
        "lint":  [
            'flake8', 'flake8-broken-line', 'flake8-bugbear',
            'flake8-builtins', 'flake8-commas', 'flake8-comprehensions',
            'flake8-fixme', 'flake8-print', 'flake8-use-fstring',
            'flake8-annotations-complexity',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/esoma/wkd',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment',
    ],
    python_requires='>=3.9',
)
