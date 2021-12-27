[![syscolors](https://img.shields.io/pypi/v/syscolors?style=for-the-badge)](https://pypi.org/project/syscolors/)
[![syscolors](https://img.shields.io/pypi/pyversions/syscolors?style=for-the-badge)](https://www.python.org/downloads/release/python-396/)
[![syscolors](https://img.shields.io/github/repo-size/IMaresaLI/syscolors?style=for-the-badge)](https://pypi.org/project/syscolors/)
[![syscolors](https://img.shields.io/pypi/l/proxyCheck-mp?style=for-the-badge)](https://github.com/IMaresaLI/syscolors/blob/lastversion/LICENSE) 

# **SysColors**

# **How to use ?**

## **1-) Module Install and Import**
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
## **2-) proxyController class must be called.**
```python
clr = SystemColors()
```
## **3-) Default colors and Font Formating**
```python
Colors = clr.red | clr.yellow | clr.blue | clr.green | clr.magenta | clr.black | clr.white 
Background Colors  = clr.bgRed | clr.bgYellow | clr.bgBlue | clr.bgGreen | clr.bgBlack | clr.bgWhite
Color Reset = clr.reset
Font Formating = clr.bold | clr.underline | clr.reversed
```
## **4-) Outputs**

|Code 					| Output|
|-------------------------------	| -------------|
`print(clr.yellow + "Yellow Color")` | ![YellowColor](https://www.linkpicture.com/q/yellow_1.png)
`print(clr.green + "Green Color")` | ![GreenColor](https://www.linkpicture.com/q/green_2.png)
`print(clr.magenta + "Magenta Color")` | ![MagentaColor](https://www.linkpicture.com/q/green_3.png)
`print(clr.black + "Black Color")` | ![BlackColor](https://www.linkpicture.com/q/2_395.png)
`print(clr.white + "White Color")` | ![WhiteColor](https://www.linkpicture.com/q/1_656.png)
`print(clr.bgRed + "Red Background Color")` | ![RedBgColor](https://www.linkpicture.com/q/2_397.png)
`print(clr.bgYellow + "Yellow Background Color")` | ![YellowBgColor](https://www.linkpicture.com/q/3_254.png)
`print(clr.bgBlue + "Blue Background Color")` | ![BlueBgColor](https://www.linkpicture.com/q/blue_1.png)
`print(clr.bgGreen + "Green Background Color")` | ![GreenBgColor](https://www.linkpicture.com/q/green_4.png)
`print(clr.black + "Black Background Color")` | ![BlackBgColor](https://www.linkpicture.com/q/black_4.png)
`print(clr.white + "White Background Color")` | ![WhiteBgColor](https://www.linkpicture.com/q/white_14.png)
`print(clr.bold + "Font Style Bold")` | ![FontStyleBold](https://www.linkpicture.com/q/bold.png)
`print(clr.underline + "Font Style Underline")` | ![FontStyleUnderline](https://www.linkpicture.com/q/underline.png)
`print(clr.reversed + "Font Style Reversed")` | ![FontStyleReversed](https://www.linkpicture.com/q/reversed.png)

## **5-) setColor() and setBgClr() Methods**
```python
text = clr.setColor(35)
print(text + "SetColor"+reset)
```
> ### output _> 
>> ![](https://www.linkpicture.com/q/reversed_1.png)

```python
#If you don't know the color numbers, you can call the getAllColor() method.
clr.getAllColor()
```
> ### output2 _> 
>> ![](https://www.linkpicture.com/q/Adsız_83.png)

```python
bgColor = clr.setBgClr(202)
print(bgColor+"Background Color"+reset)
```
> ### output3 _> 
>> ![](https://www.linkpicture.com/q/Adsız_84.png)

```python
#If you don't know the background color numbers, you can call the getAllBgColor() method.
clr.getAllBgColor()
```
> ### output4 _> 
>> ![](https://www.linkpicture.com/q/Adsız_86.png)

## **6-) RGBSetClr() and RGBSetBgClr() Methods**
```python
#Default RGB = "240;248;255" => Type(string) 

color = clr.RGBSetClr("155;205;155")
print(color+"RGBSetColor Method"+reset)
```
>### output Default _>
>>![100](https://user-images.githubusercontent.com/70446049/127744773-2d930e24-d1f3-40f4-ba0a-36fe0875eac8.png)

> ### output set color _>
>>![200](https://user-images.githubusercontent.com/70446049/127744776-7f7a90f6-e90f-4d7f-bd08-5815d6aa8a74.png)

```python
# RGB Background Color
#Default RGB = "240;248;255" => Type(string) 

Bgcolor = clr.RGBSetBgClr("0;199;140") + clr.black
print(Bgcolor+"RGBSetBgColor Method"+reset)
```
> ### output Default BG _>
>>![100](https://user-images.githubusercontent.com/70446049/127745088-4ab002b5-77bc-46d4-abfa-b016bc218428.png)

> ### output set BgColor _>
>>![200](https://user-images.githubusercontent.com/70446049/127745092-415b42f6-da14-4dd5-81ab-31a2006e6b46.png)

## Use getAllRGB() Method 
```python
#detail = True =>> Returns color and rgb code if detail parameter is true.
#detail = False =>> If the parameter is False, the dictionary is returned.

print(clr.getAllRGB(detail=False))

#output _>

{'ALICEBLUE': '240;248;255', 'ANTIQUEWHITE': '250;235;215', 'ANTIQUEWHITE1': '255;239;219', 'ANTIQUEWHITE2': '238;223;204', 'ANTIQUEWHITE3': '205;192;176', 'ANTIQUEWHITE4': '139;131;120'...'YELLOW2': '238;238;0', 'YELLOW3': '205;205;0', 'YELLOW4': '139;139;0'}

print(clr.getAllRGB(detail=True))
```
> ### output getAllRGB > True _>
>>![100](https://user-images.githubusercontent.com/70446049/127745753-0b2518cb-55d2-4110-8afb-b5ff4d2a8fad.png)

## **7-) setHexColor() and setHexBg() Methods**
```python
#Default HexCode = "#B12345" => Type(string) 

color = clr.setHexColor("#dc143c")
print(color+"SetHexColor Method"+reset)


color = clr.setHexBg("#dc143c")
print(color+"SetHexBg Method"+reset)
```
> ### output SetHexColor _>
>> ![11](https://user-images.githubusercontent.com/70446049/128612518-17224ef5-728d-49e0-a74e-76aed8d93a50.png)

> ### output SetHexBg _>
>> ![231](https://user-images.githubusercontent.com/70446049/128612524-3729ea65-b35a-4766-b8d9-7700f0ed77d7.png)

## Use getAllHex() Method
```python
#Returns all hex color codes and colors.

clr.getAllHex()

#output _>
```
> ![Adsız](https://user-images.githubusercontent.com/70446049/128615556-794ceb7d-185e-4e20-8d48-3f83b2038cb4.png)
