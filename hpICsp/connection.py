# -*- coding: utf-8 -*
###
# (C) Copyright (2014-2017) Hewlett-Packard Development Company, L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()

__title__ = 'connection'
__version__ = '1.0.0'
__copyright__ = '(C) Copyright (2014-2017) Hewlett-Packard Development ' \
                ' Company, L.P.'
__license__ = 'MIT'
__status__ = 'Development'

import shutil
import mmap
import http.client
import os
import json
import sys
from hpICsp import connectionHPOneView


class connection(connectionHPOneView):
    """
    This module maintains communication with the appliance
    """

    def __init__(self, applianceIp, api_version=102):
        super(connection, self).__init__(applianceIp, api_version)

    def encode_multipart_formdata(self, fileName, extension):
        BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
        CRLF = '\r\n'
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        fin = open(fileName, 'rb')
        fout = open(fileName + extension, 'wb')
        fout.write(bytearray('--' + BOUNDARY + CRLF, 'utf-8'))
        fout.write(bytearray('Content-Disposition: form-data'
                             '; name="file"; filename="' +
                             fileName + extension + CRLF, "utf-8"))
        fout.write(bytearray('Content-Type: application/octet-stream' + CRLF,
                             'utf-8'))
        fout.write(bytearray(CRLF, 'utf-8'))
        shutil.copyfileobj(fin, fout)
        fout.write(bytearray(CRLF, 'utf-8'))
        fout.write(bytearray('--' + BOUNDARY + '--' + CRLF, 'utf-8'))
        fout.write(bytearray(CRLF, 'utf-8'))
        fout.close()
        fin.close()
        return content_type

    def post_multipart(self, path, fileName, extension, verbose, deleteAfterUpload):
        content_type = self.encode_multipart_formdata(fileName, extension)
        inputfile = open(fileName + extension, 'rb')
        mappedfile = mmap.mmap(inputfile.fileno(), 0, access=mmap.ACCESS_READ)
        conn = http.client.HTTPSConnection(self._host)
        conn.connect()
        conn.putrequest('POST', path)
        conn.putheader('uploadfilename', fileName)
        conn.putheader('auth', self._headers['auth'])
        conn.putheader('Content-Type', content_type)
        totalSize = os.path.getsize(fileName + extension)
        conn.putheader('Content-Length', totalSize)
        conn.endheaders()

        while mappedfile.tell() < mappedfile.size():
            # Send 1MB at a time
            # NOTE: Be careful raising this value as the read chunk
            # is stored in RAM
            readSize = 1048576
            conn.send(mappedfile.read(readSize))
            if verbose is True:
                sys.stdout.write('%d bytes sent... \r' % mappedfile.tell())
                sys.stdout.flush()
        mappedfile.close()
        inputfile.close()
        os.remove(fileName + extension)
        if deleteAfterUpload:
            os.remove(fileName)
        response = conn.getresponse()
        body = response.read().decode('utf-8')
        if body:
            try:
                body = json.loads(body)
            except ValueError:
                body = response.read().decode('utf-8')
        conn.close()
        return body
