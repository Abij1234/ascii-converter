#!/usr/bin/python/
import ascii_magic
img=input("\033[1;34mENTER YOUR NAME OF IMAGE==> \033[0m")
output = ascii_magic.from_image_file(img,colums=200,char="#")
ascii_magic.to_terminal(output)

