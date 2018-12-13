#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All file operations
"""

import pathlib
import shutil

def get_files_by_pat(path,pat,subdir=None):
    filelist = []
    for dir in pathlib.Path(path).iterdir():
        for fi in (dir/subdir).glob(pat):
            filelist.append(str(fi))
    return filelist

def get_parent(path,level=0,only_name=False):
    if only_name:
        return str(pathlib.Path(path).parents[level].name)

    return str(pathlib.Path(path).parents[level])

def copy_file(ab,bis,create_parent=None):
    if create_parent:
        pathlib.Path(pathlib.Path(bis)/str(create_parent)).mkdir(exist_ok=True)
        shutil.copy2(ab,bis+'/'+create_parent+'/')
    else:
        shutil.copy2(ab,bis)

    return 0

