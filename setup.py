#!/usr/bin/env python
from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name='golconda',
    version='0.1',

    description='Diamond model exploration tool',
    long_description=long_description,

    author='Doug Hellmann',
    author_email='doug.hellmann@gmail.com',

    url='https://github.com/AdamTheAnalyst/golconda',
    download_url='https://github.com/AdamTheAnalyst/golconda',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],
    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'gcli = golconda.main:main'
        ],
        'golconda.cli': [
            'create = golconda.create:Create',
            'delete = golconda.delete:Delete',
            'export = golconda.export:Export',
            'group = golconda.group:Group',
            'search = golconda.search:Search',
            'show =  golconda.show:Show'
        ]
    },

    zip_safe=False,
)