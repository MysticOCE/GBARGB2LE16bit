from struct import *
import binascii
#f is the file to output the hex to, r is the file read for the colors
f = open('testing3.dmp','wb')
r = open('testing2.txt','r')
#i used readline() because I don't know why readlines gives a list or how to work with it
lines = r.readline()
#until the giant string of colors is depleted
while (lines):
	print(lines)
	#gets the R,G,B values from the string
	R = lines[:2]
	G = lines[2:4]
	B = lines[4:6]
	#removes the used colors from the input
	lines = lines[6:]
	print(lines)
	#converts R,G,B into the binary needed
	rbin = format(int(R),'05b')
	gbin = format(int(G),'05b')
	bbin = format(int(B),'06b')
	print(rbin,gbin,bbin)
	#concatenates the binary color strings together to BGR
	color = bbin + gbin + rbin
	#converts current color string to an int
	color2 = int(color,2)
	print(color2)
	#converts color int to a hex string
	color3 = color2.to_bytes(2, byteorder='big')
	#converts it to little endian
	color3a = pack('<H',color2)
	print(color3a)
	#writes the current color to the binary file
	f.write(color3a);
f.close()
r.close()
#an input so you know the thing actually ran
str = input("Done?")