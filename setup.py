"""Setup configuration for Station Exchange Format package.

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
import glob

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='SEF',
    version='0.0.1',
    description='Station Exchange Format',

    # From README - see above
    long_description=long_description,
    # long_description_content_type='text/x-rst',

    url='https://brohan.org/SEF/',

    author='Philip Brohan',
    author_email='philip.brohan@metofice.gov.uk',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],

    # Keywords for your project. What does your project relate to?
    keywords='weather observations assimilation',

    # Automatically find the software to be included
    package_dir={'': '.'},
    packages=find_packages(where='.'),


    # Other packages that your project depends on.
    install_requires=[
        'pandas>=0.23.4',
    ],


)
