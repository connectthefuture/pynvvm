# Copyright (c) 2013 NVIDIA Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This sample illustrates a simple LLVM IR -> PTX compiler implemented using
libNVVM. All command-line options are passed along to libNVVM. Arguments that
start with '-' are assumed to be options and are passed along accordingly.
Otherwise, options are treated as file names and are read as IR input(s).
"""

import sys
from pynvvm.compiler import Program, ProgramException


if len(sys.argv) < 2:
    print('Usage: %s ir-file-1 [ir-file-2 [ir-file-3 ...]]' % sys.argv[0])
    sys.exit(1)

try:
    p = Program()
    options = []
    for a in sys.argv[1:]:
        if a.startswith('-'):
            options.append(a)
        else:
            with open(a, 'rb') as f:
                p.add_module(f.read())
    ptx = p.compile(options)
    print(ptx)
except ProgramException as e:
    print('ERROR:\n%s\n' % repr(e))

