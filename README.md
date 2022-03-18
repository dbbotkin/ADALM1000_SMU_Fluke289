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
