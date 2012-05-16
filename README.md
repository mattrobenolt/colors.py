# colors.py
Convert colors between rgb, hsv, and hex, and generating random colors within boundaries
## Installation
```$ pip install ...```
## Usages
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