#!/usr/bin/env python
# coding: utf8
# Part of the bioread package for reading BIOPAC data.
#
# Copyright (c) 2016 Board of Regents of the University of Wisconsin System
#
# Written Nate Vack <njvack@wisc.edu> with research from John Ollinger
# at the Waisman Laboratory for Brain Imaging and Behavior, University of
# Wisconsin-Madison
# Project home: http://github.com/njvack/bioread

# This contains the entry point for an executable to convert BIOPAC
# AcqKnowledge files into Matlab files.

"""Convert an AcqKnowledge file to a MATLAB file.

Usage:
  acq2mat [options] <acq_file> <mat_file>
  acq2mat -h | --help
  acq2mat --version

Options:
  -c, --compress  save compressed Matlab file

Note: scipy is required for this program.
"""

from __future__ import absolute_import

import sys
from bioread.vendor.docopt import docopt

from bioread.reader import Reader
from bioread.writers.matlabwriter import MatlabWriter
from bioread import version
import scipy
import os

def main():
    print('Enter path to acqknowledge files')
    dir = input()
    
    files = os.listdir(dir)
    acqfiles = filter(lambda s: '.acq' in s, files)

    for f in acqfiles:
        filepath = dir + '\\' + f
        print(filepath)
        amr = AcqToMatRunner(filepath)
        amr.run()
    
    print('Done, press enter to leave')
    input()


class AcqToMatRunner(object):
    """The little wrapper class that converts acq files to mat files"""

    def __init__(self, filepath, err=None):
        self.filepath = filepath
        if err is None:
            err = sys.stderr
        self.err = err

    def run(self):
        infile = self.filepath
        matfile = self.filepath.replace('.acq', '.mat')


        data = Reader.read(infile).datafile
        MatlabWriter.write_file(data, matfile)


if __name__ == '__main__':
    main()