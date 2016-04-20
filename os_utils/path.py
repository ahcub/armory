import os
from distutils.dir_util import remove_tree
from os.path import join, isdir, isfile, islink, exists
from pathlib import Path
from stat import *


WRITE = S_IWUSR | S_IWGRP | S_IWOTH


def clear_dir(path):
    delete(path)
    Path.mkdir(path, parents=True, exist_ok=True)


def delete(path):
    if exists(path):
        if isdir(path):
            add_permissions_to_dir_rec(path, WRITE)
            remove_tree(path)
        elif isfile(path):
            add_permissions_to_path(path, WRITE)
            os.remove(path)
        elif islink(path):
            add_permissions_to_path(path, WRITE)
            os.unlink(path)


def add_permissions_to_path(path, permissions):
    return os.chmod(path, os.stat(path)[ST_MODE] | permissions)


def add_permissions_to_multiple_paths(root, paths, permissions):
    for path in paths:
        add_permissions_to_path(join(root, path), permissions)


def add_permissions_to_dir_rec(path, permissions):
    for root, dirs, files in os.walk(path):
        add_permissions_to_multiple_paths(root, dirs + files, permissions)
