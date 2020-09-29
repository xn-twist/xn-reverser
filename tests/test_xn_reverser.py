#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_xn_reverser
----------------------------------
Tests for `xn_reverser` module.
"""

import xn_reverser


def test_xn_reverser_apple_fullunicode():
    result = xn_reverser.xn_reverser("xn--80ak6aa92e.com")
    assert result["possible_spoofed_ascii"] == ['appie.com', 'apple.com']
