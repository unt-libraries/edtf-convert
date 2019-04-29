#! /usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='edtf-convert',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['edtf-to-temper=edtf_convert.edtf_to_temper:main'],
    },
    license='BSD',
    description='Convert to and from Extended Date/Time Format strings.',
    long_description=('Visit https://github.com/unt-libraries/edtf-convert '
                      'for the latest documentation.'),
    keywords=['edtf', 'temper'],
    author='University of North Texas Libraries',
    author_email='mark.phillips@unt.edu',
    url='https://github.com/unt-libraries/edtf-convert',
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
