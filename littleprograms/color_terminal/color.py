#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
    Sets up the terminal color scheme.
"""

import os
import sys

from django.utils import termcolors

#args:
#return:true:系统终端支持颜色;flase:系统终端不支持颜色
#doc:判断系统的终端是否支持颜色
#example:
#####test#####
    #supports_color()
#####test#####
def supports_color():
    """
    Returns True if the running system's terminal supports color, and False
    otherwise.
    """
    unsupported_platform = (sys.platform in ('win32', 'Pocket PC'))
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    #sys.stdout:File objects corresponding to the interpreter’s standard output,
    #isatty():判断file obj是否链接到了一个tty(终端)设备上
    if unsupported_platform or not is_a_tty:
        return False
    return True

#args:
#return:dummy(假的)对象，包含了对于能够改变终端样式的系统能够根据文本的定义不同(eg:ERROR,NOTICE),返回不同的样式的函数，eg:dummy().ERROR("this is a error!"),dummy().NOTICE("this is a notice!")
#doc:提供了用于格式文本的style，它可以改变字符串的样式，eg:dummy().ERROR("this is a error!"),dummy().NOTICE("this is a notice!")
#example:
#####test#####
    #color_style()
#####test#####
def color_style():
    """Returns a Style object with the Django color scheme."""
    if not supports_color():
        style = no_style()
    else:
        DJANGO_COLORS = os.environ.get('DJANGO_COLORS', '')
        #返回默认的palette,DARK_PALETTE
        color_settings = termcolors.parse_color_setting(DJANGO_COLORS)
        if color_settings:
            class dummy: pass
            style = dummy()
            # The nocolor palette has all available roles.
            # Use that pallete as the basis for populating
            # the palette as defined in the environment.
            for role in termcolors.PALETTES[termcolors.NOCOLOR_PALETTE]:
                format = color_settings.get(role,{})
                setattr(style, role, termcolors.make_style(**format))
            # For backwards compatibility,
            # set style for ERROR_OUTPUT == ERROR
            style.ERROR_OUTPUT = style.ERROR
        else:
            style = no_style()
    return style

#class A与class A(object)的区别是:A(object)拥有继承来自object的属性,                          eg:dir(A),>>>['__doc__', '__module__', 'a'],                                                dir(A),>>>['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a']

#dummy:虚拟的，假的

#args:
#return:一个dummy对象，此对象拥有['__doc__', '__module__']属性，并定义了__getattr__函数，无论获取什么属性，都会返回一个lambda函数,eg：dummy().b("123"),>>>'123'
#doc:返回一个dummy对象,表示不能使用终端样式表
#example:
#####test#####
    #color_style()
#####test#####
def no_style():
    """Returns a Style object that has no colors."""
    class dummy:
        def __getattr__(self, attr):
            return lambda x: x
    return dummy()
