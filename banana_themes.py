from pygments.style import Style
from pygments.token import (Comment, Keyword, Operator, String,
                            Number, Punctuation, Name, Error)

__all__ = ['HitGub', 'Zaab']


class HitGub(Style):
    background_color = '#ffffff'
    default_style = '#000000'

    # All the superfluous styles (i.e. the ones that are the same as
    # default_style) are there because for some reason styles don't inherit
    # default_style, even though the docs explicitly say so.
    styles = {
        Comment: '#6a737d',

        Keyword: '#d73a49',
        Keyword.Constant: '#005cc5',

        Operator: '#d73a49',
        Operator.Word: '#d73a49',

        Number: '#005cc5',

        Punctuation: '#000000',

        Name: '#000000',
        Name.Tag: '#ffffff',
        Name.Variable: '#005cc5',
        Name.Constant: '#005cc5',
        Name.Builtin: '#0086BF',
        Name.Exception: 'bold #000000',
        Name.Decorator: '#795DC1',
        Name.Class: '#6f42c1',
        Name.Function: '#6f42c1',
        Name.Function.Magic: '#005cc5',

        String: '#032f62',

        Error: 'bg:#ff0000 #000000',
    }


class Zaab(Style):
    background_color = '#1c1c1c'
    default_style = '#ffffff'

    # All the superfluous styles (i.e. the ones that are the same as
    # default_style) are there because for some reason styles don't inherit
    # default_style, even though the docs explicitly say so.
    styles = {
        Comment: '#808080',

        Keyword: '#6495ed',

        Operator: '#ffffff',
        Operator.Word: '#6495ed',

        Number: '#ffffff',

        Punctuation: '#ffffff',

        Name: '#ffffff',
        Name.Builtin: '#9f79ee',
        Name.Exception: 'bold #ff4500',
        Name.Decorator: '#1e90ff',

        String: '#00cd66',

        Error: 'bg:#ff0000 #ffffff',
    }
