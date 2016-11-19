# -*- coding: utf-8 -*-

from setuptools import setup

setup(
        name='omxd',
        version='0.0.1',
        packages=['omxd'],
        install_requires=['Flask >= 0.10.1'],
        entry_points={'console_scripts': ['omxdcli=omxd:main']},
        author='Tobias Schäfer',
        author_email='omxd@blackoxorg',
        url='https://github.com/tschaefer/omxd',
        description="omxd. REST API daemon for the awesome OMXPlayer.",
        license='BSD',
        include_package_data=True,
        zip_safe=False
)
