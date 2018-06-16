=========
Filestore
=========

The filestore is an easy way to to process files with multiple processes
without needing locks.


Initialize a FileStore
======================

Create a filestore in a temporary area:

>>> import tempfile
>>> store_dir = tempfile.mkdtemp()
>>> from gocept.filestore import FileStore
>>> filestore = FileStore(store_dir)
>>> filestore
<gocept.filestore.filestore.FileStore object at 0x...>

So far nothing has happend:

>>> import os
>>> os.listdir(store_dir)
[]

Before using the store we need to prepare it:

>>> filestore.prepare()

Prepare has created the tmp/new/cur directory structure:

>>> sorted(os.listdir(store_dir))
['cur', 'new', 'tmp']

Calling prepare again does nothing:

>>> filestore.prepare()
>>> sorted(os.listdir(store_dir))
['cur', 'new', 'tmp']


Use a FileStore
===============

Adding files to the store works with the `create` method:

>>> f = filestore.create('a-file')

Files are created in the 'tmp' area with the 'w' mode (if not specified):

>>> f
<open file '.../tmp/a-file', mode 'w' at 0x...>

We find the file in the tmp area. Note that `filestore.list` lists files with
their full path names, so we could feed the name directly to file/open:

>>> filestore.list('tmp')
['.../tmp/a-file']

We got a plain file back, so write to it:

>>> f.write('Die Ente bleibt draussen!')
>>> f.close()

We have finished writing our file, so we can move it to the `new` space for
other applications to pick it up:

>>> filestore.move('a-file', 'tmp', 'new')
>>> filestore.list('tmp')
[]
>>> filestore.list('new')
['.../new/a-file']

The move operation uses os.move which is supposed to be atomic. When another
processes "sees" the file it can directly work with it and move it to 'cur':

>>> filestore.move('a-file', 'new', 'cur')
>>> filestore.list('new')
[]
>>> filestore.list('cur')
['.../cur/a-file']

Files can be copied, too:

>>> filestore.copy('a-file', 'cur', 'tmp')
>>> filestore.list('cur')
['.../cur/a-file']
>>> filestore.list('tmp')
['.../tmp/a-file']


Cleanup
=======

Remove the temporary directory after testing:

>>> import shutil
>>> shutil.rmtree(store_dir)
