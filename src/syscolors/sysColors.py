import sys
from syscolors.rgbColors import *

class SystemColors:
    def __init__(self):
        self.red = u'\u001b[31m'
        self.yellow = u'\u001b[93m'
        self.blue = u'\u001b[34m'
        self.green = u'\u001b[32m'
        self.magenta = u'\u001b[35m'
        self.black = u'\u001b[30m'
        self.white = u'\u001b[37m'
        self.bgRed = u'\u001b[48;5;124m'
        self.bgYellow = u'\u001b[48;5;220m'
        self.bgBlue = u'\u001b[48;5;21m'
        self.bgGreen = u'\u001b[48;5;34m'
        self.bgBlack = u'\u001b[48;5;16m'
        self.bgWhite = u'\u001b[48;5;7m'
        self.reset = u'\u001b[0m'
        self.bold = u'\u001b[1m'
        self.underline = u'\u001b[4m'
        self.reversed = u'\u001b[7m'


    def setColor(self,colorInt):
        """Returns the color equivalent of the int value you specify.\n
        colorInt : paremater to 32 =>> Color Blue etc.\n"""
        return u"\u001b[38;5;"+str(colorInt)+"m"

    def getAllColor(self):
        """Returns all color codes and colors.\n\n"""
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
            print(u"\u001b[0m")

    def setBgClr(self,colorInt):
        """Returns the background color of the int value you specify.\n
        colorInt : paremater to 32 =>> Background Color Blue etc.\n
        """
        return u"\u001b[48;5;"+str(colorInt)+"m"

    def getAllBgColor(self):
        """Returns all background color codes and background colors.\n\n"""
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
            print(u"\u001b[0m")

    def RGBSetClr(self,rgb="240;248;255"):
        """Returns the color of the rgb code you specify.\n
        Default RGB = "240;248;255" => Type(string) \n"""
        return u"\u001b[38;2;{}m".format(rgb)

    def RGBSetBgClr(self,rgb="240;248;255"):
        """Returns the background color of the rgb code you specify.\n
        Default RGB = "240;248;255" => Type(string) \n"""
        return u"\u001b[48;2;{}m".format(rgb)

    def getAllRGB(self,detail=False):
        """Returns all rgb color codes and colors.\n
        detail = True =>> Returns color and rgb code if detail parameter is true.\n
        detail = False =>> If the parameter is False, the dictionary is returned.\n"""
        if detail :
            n = 0
            text = ""
            for i in range(int((len(RgbColors)-1)/3)):
                for j in range(3):
                    text += u"\u001b[48;2;"+RgbColors[list(RgbColors.keys())[n]]+"m"+list(RgbColors.keys())[n] +" : "+ RgbColors[list(RgbColors.keys())[n]]+u"\u001b[0m "
                    sys.stdout.write(text)
                    n+=1
                print(u"\u001b[0m")
                text = ""
        else :  
            return RgbColors
