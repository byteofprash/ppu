#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Operations on dicts """

def max_dict(dic):
    """
    Returns a the max key of a dict as a list. If more than 1 has the max values, returns them all.
    Parameters
    ----------
    dic : dict

    Returns
    ---------
    list
    """
    return  [k for k,v in dic.items() if v == max(dic.values())]

def min_dict(dic):
    """
    Returns a the max key of a dict as a list. If more than 1 has the max values, returns them all.
    Parameters
    ----------
    dic : dict

    Returns
    ---------
    list
    """
    return  [k for k,v in dic.items() if v == min(dic.values())]



