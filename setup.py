###
#  (C) Copyright 2014 Hewlett-Packard Development Company, L.P
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


from distutils.core import setup

setup(name='hpICsp',
      version='1.0',
      description='HP Insight Control Server Provisioning Python Library',
      url='https://github.com/HewlettPackard/python-hpICsp',
      download_url="https://github.com/HewlettPackard/python-hpICsp/tarball/v1.0",
      author='Hewlett-Packard Development Company L.P.',
      author_email='oneview-pythonsdk@hpe.com',
      license='MIT',
      packages=['hpICsp'],
      install_requires=['future>=0.15.2'])
