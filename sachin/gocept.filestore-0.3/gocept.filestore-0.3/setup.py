# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id: setup.py 30204 2009-10-08 13:09:44Z wosc $

import os.path

from setuptools import setup, find_packages


setup(
    name = 'gocept.filestore',
    version = '0.3',
    author = "Christian Zagrodnick",
    author_email = "cz@gocept.com",
    description = "Provides mdildir like access to files",
    long_description = file(os.path.join(os.path.dirname(__file__),
                                         'src', 'gocept', 'filestore',
                                         'README.txt')).read(),
    license = "ZPL 2.1",
    url='http://pypi.python.org/pypi/gocept.filestore',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    include_package_data = True,
    zip_safe = False,

    namespace_packages = ['gocept'],
    install_requires = [
        'setuptools',
        'zope.deferredimport',
        'zope.interface',
    ],
    extras_require = {
        'test': ['zope.testing'],
    },
    )
