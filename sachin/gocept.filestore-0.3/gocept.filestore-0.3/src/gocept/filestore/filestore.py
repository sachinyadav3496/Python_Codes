# Copyright (c) 2006-2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id: filestore.py 30203 2009-10-08 13:09:31Z wosc $

import os
import os.path
import shutil

import zope.interface

import gocept.filestore.interfaces


class FileStore(object):

    zope.interface.implements(gocept.filestore.interfaces.IFileStore)

    sub_dirs = ('tmp', 'new', 'cur')

    def __init__(self, path):
        self.path = path

    def prepare(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        for dir in self.sub_dirs:
            dir = os.path.join(self.path, dir)
            if not os.path.exists(dir):
                os.mkdir(dir)
            if not os.path.isdir(dir):
                raise RuntimeError("Could create directory %r, "
                                   "something is in the way." % dir)

    def create(self, filename, mode='w'):
        path = os.path.join(self.path, 'tmp', filename)
        f = file(path, mode)
        return f

    def copy(self, filename, source, destination):
        filename = os.path.basename(filename)
        source_path = os.path.join(self.path, source, filename)
        dest_path = os.path.join(self.path, destination, filename)
        shutil.copy(source_path, dest_path)

    def move(self, filename, source, destination):
        filename = os.path.basename(filename)
        source_path = os.path.join(self.path, source, filename)
        dest_path = os.path.join(self.path, destination, filename)
        os.rename(source_path, dest_path)

    def remove(self, filename, source):
        path = os.path.join(self.path, source, filename)
        os.remove(path)

    def list(self, section):
        path = os.path.join(self.path, section)
        return [os.path.join(self.path, section, path)
                for path in  os.listdir(path)]
