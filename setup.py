# -*- coding: utf-8 -*-

from setuptools import setup

setup(
        name='tv',
        version='0.0.1',
        packages=['tv'],
        install_requires=['Flask >= 0.10.1'],
        entry_points={'console_scripts': ['tv=tv:main']},
        author='Tobias Schäfer',
        author_email='omxd@blackoxorg',
        url='https://github.com/tschaefer/omxd',
        description="tv. REST API service for the awesome OMXPlayer and MPV.",
        license='BSD',
        include_package_data=True,
        zip_safe=False
)
