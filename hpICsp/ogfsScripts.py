# -*- coding: utf-8 -*-
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

__title__ = 'ogfsScripts'
__version__ = '1.0.0'
__copyright__ = '(C) Copyright (2014-2017) Hewlett-Packard Development ' \
                ' Company, L.P.'
__license__ = 'MIT'
__status__ = 'Development'

import hpICsp.common


class ogfsScripts(object):
    """
    This module implements OGFS Scripts HP ICsp REST API
    """

    def __init__(self, con):
        self._con = con

    def get_script(self, URI=None, start=0, count=-1):
        if (URI):
            body = self._con.get(URI)
        else:
            body = self._con.get(hpICsp.common.uri['ogfsScript'] + '?start=%s&count=%s' % (start, count))
        return body

    def update_script(self, body):
        scriptID = body['uri'].split('/')[-1]
        body = self._con.put(hpICsp.common.uri['ogfsScript'] + '/%s' % (scriptID), body)
        return body

    def add_script(self, body):
        body = self._con.post(hpICsp.common.uri['ogfsScript'], body)
        return body

    def delete_script(self, URI):
        body = self._con.delete(URI)
        return body
