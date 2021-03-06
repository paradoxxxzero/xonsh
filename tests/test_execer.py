"""Tests the xonsh lexer."""
from __future__ import unicode_literals, print_function
import os
import sys
import ast

from xonsh.execer import Execer

from tools import mock_xonsh_env

DEBUG_LEVEL = 0
EXECER = None

#
# Helpers
#

def setup():
    # only setup one parser
    global EXECER
    EXECER = Execer(debug_level=DEBUG_LEVEL)

def check_exec(input):
    with mock_xonsh_env(None):
        if not input.endswith('\n'):
            input += '\n'
        EXECER.debug_level = DEBUG_LEVEL
        EXECER.exec(input)

def check_eval(input):
    with mock_xonsh_env(None):
        EXECER.debug_level = DEBUG_LEVEL
        EXECER.eval(input)

#
# Tests
#

def test_bin_ls():
    yield check_eval, '/bin/ls -l'

def test_ls_dashl():
    yield check_eval, 'ls -l'

def test_which_ls():
    yield check_eval, 'which ls'


if __name__ == '__main__':
    nose.runmodule()
