# colors.py
Convert colors between rgb, hsv, and hex, and generating random colors within boundaries
## Installation
```$ pip install ...```
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