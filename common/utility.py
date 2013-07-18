# -*- coding:utf-8 -*-

""" Utility.
"""

from sys import argv
from os import walk, listdir
from os.path import abspath, join as path_join, dirname, basename, splitext
from fnmatch import fnmatch
from inspect import ismodule, getmembers

ROOT_PATH = dirname(abspath(argv[0]))
app_path = lambda n: path_join(ROOT_PATH, n)



def get_modules(pkg_name, module_filter = None):
    """
        返回包中所有符合条件的模块。

        参数:
            pkg_name        包名称
            module_filter   模块名过滤器 def (module_name)
    """
    path = app_path(pkg_name)
    py_filter = lambda f: all((fnmatch(f, "*.py"), not f.startswith("__"), module_filter and module_filter(f) or True))

    names = [splitext(n)[0] for n in listdir(path) if py_filter(n)]
    return [__import__("{0}.{1}".format(pkg_name, n)).__dict__[n] for n in names]



def get_members(pkg_name, module_filter = None, member_filter = None):
    """p
        返回包中所有符合条件的模块成员。

        参数:
            pkg_name        包名称
            module_filter   模块名过滤器 def (module_name)
            member_filter   成员过滤器 def member_filter(module_member_object)
    """
    modules = get_modules(pkg_name, module_filter)

    ret = {}
    for m in modules:
        members = dict(("{0}.{1}".format(v.__module__, k), v) for k, v in getmembers(m, member_filter))
        ret.update(members)

    return ret



__all__ = ["ROOT_PATH", "app_path", "get_modules", "get_members"]
