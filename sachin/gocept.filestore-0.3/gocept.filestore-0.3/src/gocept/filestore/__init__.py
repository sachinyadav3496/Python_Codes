# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id: __init__.py 5111 2007-08-30 11:27:23Z zagy $

import zope.deferredimport

zope.deferredimport.define(
    FileStore = 'gocept.filestore.filestore:FileStore'
    )
