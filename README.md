# RP2040-Interactive-KITT-Knight-Rider
Create your own KITT from the TV show Knight Rider using an RP2040 Microcontroller  <br />
YouTube video preview  <br />
https://www.youtube.com/watch?v=hxRDTuXU2fs
## Introduction
Welcome to the tutorial to build your very own Interactive KITT from the TV show Knight Rider!  This will be divided into 3 parts.  Part 1 will explain the hardware and PCBs needed for the project. <br />
Part 2 will explain the code and software needed to install on your RP2040 microcontroller. <br />
Part 3 will explain the asthetics including 3D printing the body, creating the labels for the indicators, and using colored sheets for the voicebox and indicators. <br />

# Part 1 Hardware
For this project, you will need to order 2 different PCBs to create KITT.  The Gerber files needed to have them made are available in this repository.  You will need to upload these files (two files already in zip format) to your preferred PCB manufacturer.  I usually use JLBPCB as they tend to be the cheapest but feel free to use anyone. <br />
You will also find a PDF called Parts which you can download and view. You'll need these parts to complete the PCBs.  Note that you should be comfortable in soldering as there are many components needed to be soldered onto the boards. Most of these parts can be ordered through websites like Adafruit, Amazon, Aliexpress, Mouser, etc... <br />
## Equipment
For equipment needed to build this part of the project, you'll need a soldering iron and stand, hot air gun, some shrink wrap for wires, wire cutters and wire stripper, solder, and solder paste. <br />
## Parts
One part that is required for this project but no longer manufactured by Adafruit is the UDA1334A DAC module.  However, you can find 3rd party versions of it on Amazon and Aliexpress. <br />
The PDM Mic used for this project is very sensitive and I had difficulty making it detect sound correctly.  If you have this issue, try disconnecting the VCC(power) from the board to the mic and run it that way.  That seems to fix the problem and I'm not sure why. <br />
Notice the connectors between the two boards are 2mm and not the standard 2.54mm.  I'd like to say this was intentional to save room but honestly it was a mistake I made in the original design but I decided to keep it as it does make the cables a little more compact. <br />
The RGB LEDs used for the indicator lights (Not the LED bars for KITT) are 5v versions.  Make sure you check before you buy as they also make them in 12v. (I ended up getting shipped the wrong voltage LEDs and it took me a few weeks of troubleshooting before I figured out why my LED board didn't work.) <br />
I chose the Waveshare RP-2040 Plus microcontroller because it has 4MB of memory.  However, you can use any rp2040 based microcontroller as long as it has (A) 4MB or more of flash memory and (B) it is in the same form factor as the original Raspberry Pi Pico.  If you decide to go with a different microcontroller, make sure the pins line up exactly as the Pico with the same GPIO assignments or it will not work. <br />
## Part 1 video
<div align="center">
  <a href="https://www.youtube.com/watch?v=F8oxOOc2xko"><img src="https://img.youtube.com/vi/F8oxOOc2xko/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>


# Part 2 Programming and Software needed
Coming soon <br />
# Part 3 Aesthetics and 3D printing
Coming soon
