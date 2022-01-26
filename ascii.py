#!/usr/bin/python/
import ascii_magic, os

#::::::::::: Requirments :::::::::
print("\033[1;31mINSTALLING PACKAGES.... \033[0m")
os.system("pip3.10 install ascii_magic")

#/////////// Programe /////////////
img=input("\033[1;34mENTER YOUR NAME OF IMAGE==> \033[0m")
output = ascii_magic.from_image_file(img,colums=200,char="#")
ascii_magic.to_terminal(output)

