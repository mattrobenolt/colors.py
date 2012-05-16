"""
colors.py
=========
Play with colors!
"""
import colorsys
import random as random_

__version__ = '0.0.0'
__all__ = ('Color', 'HSVColor', 'RGBColor', 'HexColor', 'ColorWheel',
           'rgb', 'hsv', 'hex', 'random',)


class _ColorMetaClass(type):
    """
    Metaclass for Color to simply map the cls.Meta.properties to getters.

    >>> RGBColor(r=150, g=0, b=100).red
    150

    """
    def __new__(cls, name, bases, attrs):
        # Check for internal Meta class providing a property map
        if 'Meta' in attrs and hasattr(attrs['Meta'], 'properties'):
            for index, prop in enumerate(attrs['Meta'].properties):
                # Assign pretty getters to each property name
                attrs[prop] = property(lambda self, index=index: self._color[index])
        return super(_ColorMetaClass, cls).__new__(cls, name, bases, attrs)


class Color(object):
    """ Abstract base class for all color types. """
    __metaclass__ = _ColorMetaClass

    @property
    def hex(self):
        """ Hex is used the same way for all types. """
        return HexColor('%02x%02x%02x' % tuple(self.rgb))

    @property
    def rgb(self):
        raise NotImplemented

    @property
    def hsv(self):
        raise NotImplemented

    def __iter__(self):
        """ Treat the color object as an iterable to iterate over color values
        Allows mapping such as:

        >>> list(rgb(100, 50, 0))
        [100, 50, 0]
        >>> for i in rgb(100, 50, 0): print i
        100
        50
        0

        """
        return iter(self._color)

    def __len__(self):
        return len(self._color)

    def __str__(self):
        return ', '.join(map(str, self._color))

    def __repr__(self):
        base = u'<%s %s>'
        properties = [
            '%s: %s' % (prop, getattr(self, prop)) \
                for prop in self.Meta.properties
        ]
        return base % (self.__class__.__name__, ', '.join(properties))


class HSVColor(Color):
    """ Hue Saturation Value """

    def __init__(self, h=0, s=0, v=0):
        self._color = h, s, v

    @property
    def rgb(self):
        return RGBColor(*map(lambda c: c * 255, colorsys.hsv_to_rgb(*self._color)))

    @property
    def hsv(self):
        return self

    class Meta:
        properties = ('hue', 'saturation', 'value')


class RGBColor(Color):
    """ Red Green Blue """

    def __init__(self, r=0, g=0, b=0):
        self._color = r, g, b

    @property
    def rgb(self):
        return self

    @property
    def hsv(self):
        return HSVColor(*colorsys.rgb_to_hsv(*map(lambda c: c / 255.0, self._color)))

    class Meta:
        properties = ('red', 'green', 'blue')


class HexColor(RGBColor):
    """ Typical 6 digit hexadecimal colors.

    Warning: accuracy is lost when converting a color to hex
    """

    def __init__(self, hex='000000'):
        if len(hex) != 6:
            raise ValueError('Hex color must be 6 digits')

        hex = hex.lower()
        for digit in hex:
            if digit not in '0123456789abcdef':
                raise ValueError('Not a valid hex number')

        self._color = hex[:2], hex[2:4], hex[4:6]

    @property
    def rgb(self):
        return RGBColor(*[int(c, 16) for c in self._color])

    @property
    def hsv(self):
        return self.rgb.hsv

    @property
    def hex(self):
        return self

    def __str__(self):
        return '%s%s%s' % self._color


class ColorWheel(object):
    """ Iterate random colors disributed relatively evenly
    around the color wheel.

    >>> from colors import ColorWheel
    >>> wheel = ColorWheel()
    >>> print '#%s' % wheel.next().hex
    #cc8b00
    >>> wheel = ColorWheel(start=0.2)
    >>> print '#%s' % wheel.next().hex
    #00cc26
    >>> print '#%s' % wheel.next().hex
    #009ecc

    """
    def __init__(self, start=0):
        self._phase = start

    def __iter__(self):
        return self

    def next(self):
        shift = (random_.random() * 0.1) + 0.1
        self._phase += shift
        if self._phase > 1:
            self._phase -= 1
        return HSVColor(self._phase, 1, 0.8)


def random():  # This name might be a bad idea?
    """ Generate a random color.

    >>> from colors import random
    >>> random()
    <HSVColor hue: 0.310089903395, saturation: 0.765033516918, value: 0.264921257867>
    >>> print '#%s' % random().hex
    #ae47a7

    """
    return HSVColor(random_.random(), random_.random(), random_.random())

# Simple aliases
rgb = RGBColor  # rgb(100, 100, 100), or rgb(r=100, g=100, b=100)
hsv = HSVColor  # hsv(0.5, 1, 1), or hsv(h=0.5, s=1, v=1)
hex = HexColor  # hex(BADA55')
