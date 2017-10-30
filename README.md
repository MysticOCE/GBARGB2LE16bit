# GBARGB2LE16bit
To run this program, edit the code in the main .py so that the program can find the path. Currently, it does not open a file prompt or work if you drag the file on to the .py. You can also modify the name of the output file if you wish.

The format of the input is any number of colors in format RRGGBB where RR/GG/BB could be values from 0 to 31.  6 numbers per color, so make sure your input has 6*(number of colors) characters.

## Explanation of 16 bit color.

Standard RGB uses 8 bits per color so that you can have values from 0 to 255. 16 bit color uses 5 bits for the RR/GG/BB values so the format per color is xRRRRRGGGGGBBBBB wheree the x is a dead bit. This means that you can only have 32 possible values for each color and 32 to the 3 (32768) different color combo's (I think). The perk of this is that you save a byte per color, only needing 16 bits for a color vs standard RGB's 24.

## Explanation of input format

Put all your input on the first line of like in testing.txt. Ensure that you have 6 characters per color.

310031 would output a LE hex dump with a very nice purple.

This program will keep processing things until it hits the end of file. If you provide a color that is missing some numbers, the program will break.

It's an old project that I'm likely not coming back to, but I figured it would be a good idea to share it rather than have it stuck on my hard drive forever.