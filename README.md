# colors.py
Convert colors between rgb, hsv, and hex, perform arithmetic, blend modes, and generate random colors within boundaries
## Installation
```$ pip install colors.py```
## Basic Uses
### Importing
```python
>>> from colors import rgb, hsv, hex, random
```
### Create an RGB color object
```python
>>> rgb(100, 100, 100)
<RGBColor red: 100, green: 100, blue: 100>
```
### Convert it to hexadecimal
```python
>>> rgb(100, 100, 100).hex
<HexColor red: 64, green: 64, blue: 64>
```
### Coerce the hexadecimal to a normal string
```python
>>> str(rgb(100, 100, 100).hex)
646464
```
### Create a Hexadecimal color object
```python
>>> hex('646464')
<HexColor red: 64, green: 64, blue: 64>
```
### Extract the red/green/blue value from a hexadecimal
```python
>>> hex('646464').rgb.red
100
```
### Convert a hexadecimal to HSV
```python
>>> hex('646464').hsv
<HSVColor hue: 0.0, saturation: 0.0, value: 0.392156862745>
```
### Coerce hsv/rgb values to a list/tuple of values
```python
>>> list(hex('646464').hsv)
[0.0, 0.0, 0.39215686274509803]
```
### Create an HSV color object
```python
>>> hsv(0, 1, 1)
<HSVColor hue: 0, saturation: 1, value: 1>
```
### Convert it to RGB
```python
>>> hsv(0, 1, 1).rgb
<RGBColor red: 255, green: 0.0, blue: 0.0>
```
### Gimme a random color, any color!
```python
>>> random()
<HSVColor hue: 0.812436498638, saturation: 0.621033239007, value: 0.379850638405>
```
### Coerce a hexadecimal color to a string with formatting
```python
>>> '#%s' % random().hex
'#2f2336'
```
### Coerce RGB/HSV objects to a string for formatting
```python
>>> 'style="color: rgb(%s)"' % random().rgb
'style="color: rgb(80.3414147839, 124.403236079, 71.4620739603)"'
```
### Compare color equality
```python
>>> rgb(100, 100, 100) == hex('646464')
True
>>> hsv(0, 1, 1) == rgb(255, 0, 0)
True
```
## Arithmetic
**Note**: All arithmetic operations return `rgb` color.
### Multiply
```python
>>> hex('ff9999') * hex('cccccc')
<RGBColor red: 204.0, green: 122.4, blue: 122.4>
>>> _.hex
<HexColor red: cc, green: 7a, blue: 7a>
>>> rgb(100, 100, 100).multiply(hsv(0, 1, 1)).hex
>>> <HexColor red: 64, green: 00, blue: 00>
```
### Add
```python
>>> hex('ff9999') + rgb(10, 10, 10)
<RGBColor red: 255, green: 163, blue: 163>
>>> hex('aaffcc').add(rgb(10, 10, 10))
<RGBColor red: 180, green: 255, blue: 214>
```
### Subtract
```python
>>> hex('ff9999') - rgb(10, 10, 10)
<RGBColor red: 245, green: 143, blue: 143>
>>> hex('aaffcc').subtract(rgb(10, 10, 10))
<RGBColor red: 160, green: 245, blue: 194>
```
### Divide
```python
>>> hex('ff9999') / rgb(10, 10, 10)
<RGBColor red: 25.5, green: 15.3, blue: 15.3>
>>> hex('aaffcc').divide(rgb(10, 10, 10))
<RGBColor red: 17.0, green: 25.5, blue: 20.4>
>>> rgb(100, 100, 100) / hex('00ffff')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "colors.py", line 73, in divide
    raise ZeroDivisionError
ZeroDivisionError
```
## Blend Modes
**Note**: All blend modes return `rgb` color.
### Screen
```python
>>> hex('ff9999').screen(rgb(10, 10, 10)).hex
<HexColor red: ff, green: 9d, blue: 9d>
```
### Difference
```python
>>> hex('ff9999').difference(rgb(10, 10, 10)).hex
<HexColor red: f5, green: 8f, blue: 8f>
```
### Overlay
```python
>>> hex('ff9999').overlay(rgb(10, 10, 10)).hex
<HexColor red: ff, green: 9b, blue: 9b>
```
### Invert
```python
>>> hex('000000').invert()
<RGBColor red: 255, green: 255, blue: 255>
```
## Color palettes
`colors.py` current ships with three color palettes full of constants. See source for all available colors.
### `colors.primary`
```python
>>> import colors.primary
>>> colors.primary.red
<RGBColor red: 255, green: 0, blue: 0>
```
### `colors.rainbow`
```python
>>> import colors.rainbow
>>> colors.rainbow.indigo
<RGBColor red: 75, green: 0, blue: 130>
```
### `colors.w3c`
```python
>>> import colors.w3c
>>> colors.w3c.ghostwhite
<RGBColor red: 248, green: 248, blue: 255>
```
## The Color Wheel!
The color wheel allows you to randomly choose colors while keeping the colors relatively evenly distributed. Think generating random colors without pooling in one hue, e.g., not 50 green, and 1 red.
```python
>>> from colors import ColorWheel
>>> wheel = ColorWheel()
```
### Iterate the wheel to get the next value
ColorWheel is an iterable, but be careful if using inside any type of loop. It will iterate forever until you interject.
```python
>>> wheel.next()
<HSVColor hue: 0.177410230076, saturation: 1, value: 0.8>
>>> wheel.next()
<HSVColor hue: 0.278803914372, saturation: 1, value: 0.8>
>>> for color in wheel:
...   print color.hex
00cca4
002ecc
# Forever and ever and ever and ever
```