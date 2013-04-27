#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
    提供了能够用于定义终端样式的调色板，并且提供了能够包裹字符串的colorize函数，能够将其return值，用于sys.stderr.write()，使其能够输出带样式的字符串
"""

"""
termcolors.py
"""

#定义了颜色名
color_names = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
#{'blue': '34', 'yellow': '33', 'green': '32', 'cyan': '36', 'black': '30', 'magenta': '35', 'white': '37', 'red': '31'},为了在终端中显示颜色
foreground = dict([(color_names[x], '3%s' % x) for x in range(8)])
#{'blue': '44', 'yellow': '43', 'green': '42', 'cyan': '46', 'black': '40', 'magenta': '45', 'white': '47', 'red': '41'},为了在终端中显示颜色
background = dict([(color_names[x], '4%s' % x) for x in range(8)])

RESET = '0'
#定义了一些字体效果
opt_dict = {'bold': '1', 'underscore': '4', 'blink': '5', 'reverse': '7', 'conceal': '8'}

#underscore:下划线
#conceal:隐藏
#blink:眨眼,闪烁

#args:
#   text:要进行颜色装饰的字符串,默认值为'';
#   opts:字符要显示的样式,eg:bold,underscore;
#   kwargs:包含fg和bg,即背景色和前景色，用于设置字体颜色和字体背景色
#return:可以通过sys.stderr.write()输出的定义了颜色的字符串，eg:'\x1b[32;1mfuck you!\n\x1b[0m'
#doc:对字符串进行包裹，使其能被终端进行颜色和样式显示
#example:
#####test#####
    #colorize('hello', fg='red', bg='blue', opts=('blink',))
    #colorize()
    #colorize('goodbye', opts=('underscore',))
    #colorize('first line', fg='red', opts=('noreset',))
    #colorize('and so should this')
#####test#####
def colorize(text='', opts=(), **kwargs):
    """
    Returns your text, enclosed in ANSI graphics codes.

    Depends on the keyword arguments 'fg' and 'bg', and the contents of
    the opts tuple/list.

    Returns the RESET code if no parameters are given.

    Valid colors:
        'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'

    Valid options:
        'bold'
        'underscore'
        'blink'
        'reverse'
        'conceal'
        'noreset' - string will not be auto-terminated with the RESET code

    Examples:
        colorize('hello', fg='red', bg='blue', opts=('blink',))
        colorize()
        colorize('goodbye', opts=('underscore',))
        print colorize('first line', fg='red', opts=('noreset',))
        print 'this should be red too'
        print colorize('and so should this')
        print 'this should not be red'
    """
    code_list = []
    if text == '' and len(opts) == 1 and opts[0] == 'reset':
        return '\x1b[%sm' % RESET
    for k, v in kwargs.iteritems():
        if k == 'fg':
            code_list.append(foreground[v])
        elif k == 'bg':
            code_list.append(background[v])
    for o in opts:
        if o in opt_dict:
            code_list.append(opt_dict[o])
    if 'noreset' not in opts:
        text = text + '\x1b[%sm' % RESET
    return ('\x1b[%sm' % ';'.join(code_list)) + text

#即：kwargs中的opts的key会重写opts的默认选项，当同时用变量名和kwargs中指定时，会报错，eg:make_style(opts=('shit',),**{ 'fg': 'red', 'opts': ('bold',) })
#>>> def make_style(opts=(), **kwargs):
#...     print opts,kwargs
#>>> make_style(**{ 'fg': 'red', 'opts': ('bold',) })
#('bold',) {'fg': 'red'}

#args:
#   opts:字符要显示的样式,eg:bold,underscore;
#   kwargs:包含fg和bg,即背景色和前景色，用于设置字体颜色和字体背景色
#return:对colorize提供了一些参数的colorize的函数，类似于curry
#doc:对colorize提供一些参数进行设置，类似curry
#example:
#####test#####
    #bold_red = make_style(opts=('bold',), fg='red')
    #print bold_red('hello')
    #KEYWORD = make_style(fg='yellow')
    #COMMENT = make_style(fg='blue', opts=('bold',))
#####test#####
def make_style(opts=(), **kwargs):
    """
    Returns a function with default parameters for colorize()

    Example:
        bold_red = make_style(opts=('bold',), fg='red')
        print bold_red('hello')
        KEYWORD = make_style(fg='yellow')
        COMMENT = make_style(fg='blue', opts=('bold',))
    """
    return lambda text: colorize(text, opts, **kwargs)

#palette:调色板

#定义三种调色板
NOCOLOR_PALETTE = 'nocolor'
DARK_PALETTE = 'dark'
LIGHT_PALETTE = 'light'

#定义了几种调色板的样式
PALETTES = {
    NOCOLOR_PALETTE: {
        'ERROR':        {},
        'NOTICE':       {},
        'SQL_FIELD':    {},
        'SQL_COLTYPE':  {},
        'SQL_KEYWORD':  {},
        'SQL_TABLE':    {},
        'HTTP_INFO':         {},
        'HTTP_SUCCESS':      {},
        'HTTP_REDIRECT':     {},
        'HTTP_NOT_MODIFIED': {},
        'HTTP_BAD_REQUEST':  {},
        'HTTP_NOT_FOUND':    {},
        'HTTP_SERVER_ERROR': {},
    },
    DARK_PALETTE: {
        'ERROR':        { 'fg': 'red', 'opts': ('bold',) },
        'NOTICE':       { 'fg': 'red' },
        'SQL_FIELD':    { 'fg': 'green', 'opts': ('bold',) },
        'SQL_COLTYPE':  { 'fg': 'green' },
        'SQL_KEYWORD':  { 'fg': 'yellow' },
        'SQL_TABLE':    { 'opts': ('bold',) },
        'HTTP_INFO':         { 'opts': ('bold',) },
        'HTTP_SUCCESS':      { },
        'HTTP_REDIRECT':     { 'fg': 'green' },
        'HTTP_NOT_MODIFIED': { 'fg': 'cyan' },
        'HTTP_BAD_REQUEST':  { 'fg': 'red', 'opts': ('bold',) },
        'HTTP_NOT_FOUND':    { 'fg': 'yellow' },
        'HTTP_SERVER_ERROR': { 'fg': 'magenta', 'opts': ('bold',) },
    },
    LIGHT_PALETTE: {
        'ERROR':        { 'fg': 'red', 'opts': ('bold',) },
        'NOTICE':       { 'fg': 'red' },
        'SQL_FIELD':    { 'fg': 'green', 'opts': ('bold',) },
        'SQL_COLTYPE':  { 'fg': 'green' },
        'SQL_KEYWORD':  { 'fg': 'blue' },
        'SQL_TABLE':    { 'opts': ('bold',) },
        'HTTP_INFO':         { 'opts': ('bold',) },
        'HTTP_SUCCESS':      { },
        'HTTP_REDIRECT':     { 'fg': 'green', 'opts': ('bold',) },
        'HTTP_NOT_MODIFIED': { 'fg': 'green' },
        'HTTP_BAD_REQUEST':  { 'fg': 'red', 'opts': ('bold',) },
        'HTTP_NOT_FOUND':    { 'fg': 'red' },
        'HTTP_SERVER_ERROR': { 'fg': 'magenta', 'opts': ('bold',) },
    }
}
DEFAULT_PALETTE = DARK_PALETTE

#augment:增加，增大

#args:
#   config_string:一个字符串，格式为由;分开，可以是:'light;nocolor;dark'但是只有最后一个会起作用，也可以是：costom的字符串,eg：'ERROR=red/red,bold,blink;NOTICE=red,blink'，.........总之参数形式为:"palette;role=fg;role=fg/bg;role=fg,option,option;role=fg/bg,option,option"
#return:对终端进行设置的调色板
#doc:根据配置参数config_string返回对应的条色板palette
#example:
#####test#####
    #print termcolors.parse_color_setting('ERROR=red/red,bold,blink;NOTICE=red,blink')
    #print termcolors.parse_color_setting('ERROR=red/red,bold,blink')
    #print termcolors.parse_color_setting('light;nocolor;dark')
#####test#####
def parse_color_setting(config_string):
    """Parse a DJANGO_COLORS environment variable to produce the system palette

    The general form of a pallete definition is:

        "palette;role=fg;role=fg/bg;role=fg,option,option;role=fg/bg,option,option"

    where:
        palette is a named palette; one of 'light', 'dark', or 'nocolor'.
        role is a named style used by Django
        fg is a background color.
        bg is a background color.
        option is a display options.

    Specifying a named palette is the same as manually specifying the individual
    definitions for each role. Any individual definitions following the pallete
    definition will augment the base palette definition.

    Valid roles:
        'error', 'notice', 'sql_field', 'sql_coltype', 'sql_keyword', 'sql_table',
        'http_info', 'http_success', 'http_redirect', 'http_bad_request',
        'http_not_found', 'http_server_error'

    Valid colors:
        'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'

    Valid options:
        'bold', 'underscore', 'blink', 'reverse', 'conceal'

    """
    if not config_string:
        return PALETTES[DEFAULT_PALETTE]

    # Split the color configuration into parts
    parts = config_string.lower().split(';')
    palette = PALETTES[NOCOLOR_PALETTE].copy()
    for part in parts:
        if part in PALETTES:
            # A default palette has been specified
            palette.update(PALETTES[part])
        elif '=' in part:
            # Process a palette defining string
            definition = {}

            # Break the definition into the role,
            # plus the list of specific instructions.
            # The role must be in upper case
            role, instructions = part.split('=')
            role = role.upper()

            styles = instructions.split(',')
            styles.reverse()

            # The first instruction can contain a slash
            # to break apart fg/bg.
            colors = styles.pop().split('/')
            colors.reverse()
            fg = colors.pop()
            if fg in color_names:
                definition['fg'] = fg
            if colors and colors[-1] in color_names:
                definition['bg'] = colors[-1]

            # All remaining instructions are options
            opts = tuple(s for s in styles if s in opt_dict.keys())
            if opts:
                definition['opts'] = opts

            # The nocolor palette has all available roles.
            # Use that palette as the basis for determining
            # if the role is valid.
            if role in PALETTES[NOCOLOR_PALETTE] and definition:
                palette[role] = definition

    # If there are no colors specified, return the empty palette.
    if palette == PALETTES[NOCOLOR_PALETTE]:
        return None
    return palette
