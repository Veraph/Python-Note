#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Veraph'


# codes above let py file run on unix/liux/mac; use utf-8; 
# represent the comment and show the author respectively
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == 'main':
    test()