#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Operations on Strings """
def string2nums(string,separator=',',dtype=int):
    vals = [dtype(x.strip()) for x in string.split(separator)]
    return vals
