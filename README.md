# SysColors

# How to use ?

## 1-) Module Install and Import
 - **Install Module**
```python
pip install syscolors
```
```python
pip3 install syscolors
```
 - **Import Module**

```python
from syscolors.sysColors import SystemColors
```
## 2-) proxyController class must be called.
```python
clr = SystemColors()
```
## 3-) Default colors and Font Formating
```python
Colors = clr.red | clr.yellow | clr.blue | clr.green | clr.magenta | clr.black | clr.white 
Background Colors  = clr.bgRed | clr.bgYellow | clr.bgBlue | clr.bgGreen | clr.bgBlack | clr.bgWhite
Color Reset = clr.reset
Font Formating = clr.bold | clr.underline | clr.reversed
```
## 4-) Outputs

|Code 					| Output|
|-------------------------------	| -------------|
print(clr.red + "Red Color")  	| <span style="color: red"> Red Color </span>
`print(clr.yellow + "Yellow Color")` | <span style="color: Yellow"> Yellow Color </span>
`print(clr.blue + "Blue Color")` | <span style="color: Blue"> Blue Color </span>
`print(clr.green + "Green Color")` | <span style="color: green"> Green Color </span>
`print(clr.magenta + "Magenta Color")` | <span style="color: magenta"> Magenta Color </span>
`print(clr.black + "Black Color")` | <span style="color: black"> Black Color </span>
`print(clr.white + "White Color")` | <span style="color: white"> White Color </span>
`print(clr.bgRed + "Red Color")`  	| <span style="background-color: Red"> Background Color Red </span>
`print(clr.bgYellow + "Yellow Background Color")` | <span style="background-color: Yellow">Yellow Background Color </span>
`print(clr.bgBlue + "Blue Background Color")` | <span style="background-color: Blue">Yellow Background Color</span>
`print(clr.bgGreen + "Green Background Color")` | <span style="background-color: Green">Green Background Color</span>
`print(clr.black + "Black Background Color")` | <span style="background-color: Black">Black Background Color</span>
`print(clr.white + "White Background Color")` | <span style="background-color: White">White Background Color</span>
`print(clr.bold + "Font Style Bold")` | <span style="font-weight: bold;">Font Style Bold</span>
`print(clr.underline + "Font Style Underline")` | <span style="text-decoration: underline">Font Style Underline</span>
`print(clr.reversed + "Font Style Reversed")` | <span style="background-color:white; color:gray;">Font Style Reversed</span>
