# ADALM1000_SMU_Fluke289
This combines the Fluke 289 DMM with the ADLAM1000 module SMU "M1k"

The Fluke 289 is a large, expensive hand-held industrial DMM; the Analog Devices AALM1000 is a tiny, under $100US source-measure unit.
What do they have in common? Quality components and microAmp precision. Add a Python script to get them talking, and you have a working SMU for hobby projects, whatever.
What does the Python script accomplish? 
1) It shows how to connect Python to the Fluke 289 and get data
2) It shows how to connect Python to the M1k (it took me a while to figure that out)
3) It shows how to set the M1k to source voltage and measure current
4) It shows how to get four-quadrant measurements (-5V to +5V; sink 200mA or source 200mA)
5) It shows how to get useful data from the M1k on two channels
6) It shows how to print the output data
7) It shows how to open a CSV file and write data to it (that is the easy part)

OK, the M1k is designed for education and hobby use: a 5V 200mA SMU for demonstrating basic EE concepts. Right. And if you need 1000V or 10A, there are several SMU's from Keithley--starting at $5,000. Used on eBay go for $2,000 up. For many of my measurement tasks, a ten volt, four hundred mAmp range is more than enough. 

NOTE: this is a Python script--I run it in Thonny--not an "application." Thonny is about as entry-level as one can get in an IDE. Paste the script in the code window, press 'Run' and get the printout below.{see screenshot https://github.com/dbbotkin/ADALM1000_SMU_Fluke289/blob/main/Screen%20Shot%202022-03-18%20at%2014.18.13.png} You'll need to set up the output file, the USB to the Fluke 289, spend $100 for the M1k, configure a breadboard measurement, etc. OR, you can just comment out the stuff you don't need right away. I'm an old dog trying to learn some new tricks, so it took time to figure out the connections with things that arent meant to be connected. The M1k has some clever software (PixelPulse2) that does the UI for the kids--easy. Fluke has FormView for industrial documentation, rock-solid but about as locked-down as one would want in plant equipment.
