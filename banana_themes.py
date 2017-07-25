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
        Comment: '#969696',

        Keyword: '#A71D5D',

        Operator: '#000000',
        Operator.Word: '#A71D5D',

        Number: '#000000',

        Punctuation: '#000000',

        Name: '#000000',
        Name.Builtin: '#0086BF',
        Name.Exception: 'bold #000000',
        Name.Decorator: '#795DC1',

        String: '#183691',

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
