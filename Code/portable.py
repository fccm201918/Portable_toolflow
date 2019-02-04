#!/usr/bin/env python

'''

'''







import os
import supp1
import supp2
import fileinput
import sys
import random
from beautifultable import BeautifulTable
from tabulate import tabulate
from texttable import Texttable

# display number design files in designs folder

print ("\n \n")

print("------------------------------------------Welcome to programme *** Generate Portable VHDL design  ***------------------------ ")
print ("\n \n")
print( "---------List of Design files available---------")
path = 'designs'

files=os.listdir(path)

i=1

for file in files:
	print  i,") File name----- ", file
	
    
	i=i+1
print ("\n \n")

print(" -------------------------------------------------------------------------------------------------------------------------------- ") 
print(" PIPELINE STAGES                          FLIP FLOP                         BRAM                          DSP         ")
print(" -------------------------------------------------------------------------------------------------------------------------------- ") 
print(" PIPELINED=0 (Non pipelined)              FLIPFLOP=0 (less flipflop)        BRAM=0 (less bram)            DSP=0(less dspblocks)   ")
print(" PIPELINED=1 (Pipelined stages=1)         FLIPFLOP=1 (more flipflop)        BRAM=1 (more bram)            DSP=1 (more dspblocks)  ")
print(" PIPELINED=2 (Pipelined stages=2)                                                                                                ")
print(" PIPELINED=3 (Pipelined stages=3)                                                                                                ")        
print ("\n \n")     

print(" -------------------------------------------------------------------------------------------------------------------------------- ") 
print(" Enter your selction to run portable VHDL design Tool flow                                                                                   ")
print("\n")
print(" 1). Selcet numeric one to run AUTOMATED selection (selecting one set of parameters for all avai design files)")
print(" 2). Selcet numeric two to run CUSTOM selection (between diff design paramers for each design file)  ")
print("\n")


# asking user to enter valid selection

	
se=[1,2]

while True:
	try:
		sel=input("Enter your selection >>>> ")
		if sel  in se:
			break
		
		else:
			print(" Enter valid number 1 or 2")
			continue
			
	except:
		print("Enter valid option (Intiger )")	
		
			
			
	
	
if (sel==1):
	
	
	supp1.main()
	
	
else:
	
	supp2.main()
				
		
		
	

t6=open("temp54.txt","r")
	
for line in t6:
		line=line.replace(".vhd","")
		tt=line
		print'VVVVVVVVVVVVVVVVVVV'
		print(tt)
		tt=tt.replace("\n","")
		tt=tt.replace("\t","")
		print(tt)
		t24="vivado -mode batch -source "
		tt=tt+".tcl"
		ve=t24+tt
		os.system(ve)
			
			
	#generating list
	
lut=[]
lutl=[]
lutm=[]
ff=[]
bram=[]
dsp=[]
design=[]
design.append("Resource. List (FPGA)")
lut.append("slice LUTs* ")
lutl.append(" LUT Logic* ")
lutm.append("LUT Memory ")
ff.append(" Flip Flop ")
bram.append("Block RAM")
dsp.append("DSPs ")




t6=open("temp54.txt","r")
for line in t6:
	
		ee = line
		ee=ee.replace("\n","")
		ee=ee.replace(".vhd","")
		design.append(ee)
       
    
		ew=ee+"/"+ "post_syth_util.rpt" 
		q1=open( ew,"r")
		for line in q1:
		
		
			if "| Slice LU" in line:
		
				line =line [30:35]
				line=line.replace( " | " , "")
				lut.append(line)
		
			
			if "|   LUT as Logic "in line:
		
				line=line [30:35]
				line=line.replace( " | " , "")
				lutl.append(line)
		
			
			
			if "|   LUT as Memory "in line:
			
				line=line[30:35]
				line=line.replace( " | " , "")
				lutm.append(line)
		
			
			
			if "|   Register as Flip Flop" in line:
	
				line=line[30:35]
				line=line.replace( " | " , "")
				ff.append(line)
		
			
			if "| Block RAM Tile "in line:
		
				line=line[21:24]
				bram.append(line)
		
			
			if "| DSPs"in line:
		
				line=line[14:18]
				line=line.replace( " | " , "0")
				dsp.append(line)
	
					
print("\n")	
print("\n")
design.append("Total resources available list")	

				
			

lut.append(53200)
lutl.append(53200)
lutm.append(17400)
ff.append(106400)
bram.append(140)
dsp.append(220)








t = Texttable()			

t.add_rows([ design, lut, lutl, lutm, ff, bram, dsp ])
print t.draw()		 
 
print("\n")	

t6.close()
     



print("***************************************************Finished******************************************")

                                                                                     




	         
		



   

		
		
		
	


				
			












     




    		
		
		
	 




       	













