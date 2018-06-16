# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id: interfaces.py 5111 2007-08-30 11:27:23Z zagy $

import zope.interface


class IFileStore(zope.interface.Interface):

    def prepare():
        """Create the necessary directory structures."""

    def create(filename, mode='w'):
        """Create a new file and return the open file handle.

        New files are always created in the 'tmp' space. The caller is
        responsible to close the file.

        """

    def move(filename, source, destination):
        """Move file from source space to destination space.

        Leading path elements are stripped from the filename.

        This method is used to move file from tmp to new or from new to cur.

        """

    def remove(filename, space):
        """Remove file from given space.

        """

    def list(space):
        """List files in the given space with their full path names.

        This is useful to pass names to external programms for instance.

        """
