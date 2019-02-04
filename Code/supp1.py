#!/usr/bin/env python


import os

import fileinput
import sys
import random
from beautifultable import BeautifulTable
from tabulate import tabulate
from texttable import Texttable





def main():
	# path for design files to add
	path = 'designs'
	files=os.listdir(path)
	#path defined above
	print ("\n ")
	print ("----------------- DESIGN PARAMETERS available --------------")
	print("\n")
	#extracting each design parameter from design file
	print("Papameters avilable in design files ")
	print("\n")
	with open ("temp.txt","w+") as q1:
		for file in files:
			xx=file
			xx=xx.replace(".vhd","")
			for line in fileinput.input(file):
				if "--#" in line:
					line = line.replace(" ","")
					line =line.replace("--#","")
					line=line.replace("\t","")
					q1=open("temp.txt", "r")
					if line in q1:
						continue
					else:
						with open("temp.txt", "a") as q1:
							q1.write(line)
	# to print parametrs in input design files
	t=1
	with open("temp.txt","r") as q1:
		for line in q1:
			print t,')', line
			t+=1
	#Asking user to select one parameter in each section
	q2= open ("para.txt","w+")
	with open ("temp.txt","r") as q1:
		for line in q1:
			if "pipelined=0" in line:
				q2.write(line)
			elif "pipelined=1" in line:
				q2.write(line)
			elif "pipelined=2" in line:
				q2.write(line)
			elif "pipelined=3" in line:
				q2.write(line)
	q2.close()
	q1.close()
	with open("para.txt","r") as q1:
		i=0
		for line in q1:
			i+=1
	
	if (i>0):
		print("\n")
		q3=open("para1.txt","w+")
		print("Select one parameter from pipelining")
		q1=open("para.txt","r")
		print(q1.read())
		print("\n")
		sel=raw_input("Enter the selection >>>  ")
		q3.write(sel)
		q3.write("\n")
	q1.close()
	q3.close()
	# flipflop	
	q2= open ("para.txt","w+")
	with open ("temp.txt","r") as q1:
		for line in q1:
			if "flipflop=0" in line:
				q2.write(line)
			elif "flipflop=1" in line:
				q2.write(line)			
	q2.close()
	q1.close()
	with open("para.txt","r") as q1:
		i=0
		for line in q1:
			i+=1
	
	if (i>0):
		print("\n")
		q3=open("para1.txt","a")
		print("Select one parameter for FLIPFLOP")
		q1=open("para.txt","r")
		print(q1.read())
		print("\n")
		sel=raw_input("Enter the selection >>>  ")
		q3.write(sel)
		q3.write("\n")
	q1.close()
	q3.close()
	#dsp
	q2= open ("para.txt","w+")
	with open ("temp.txt","r") as q1:
		for line in q1:
			if "dsp=0" in line:
				q2.write(line)
			elif "dsp=1" in line:
				q2.write(line)			
	q2.close()
	q1.close()
	with open("para.txt","r") as q1:
		i=0
		for line in q1:
			i+=1
	
	if (i>0):
		print("\n")
		q3=open("para1.txt","a")
		print("Select one parameter for DSP Blocks")
		q1=open("para.txt","r")
		print(q1.read())
		print("\n")
		sel=raw_input("Enter the selection >>>  ")
		q3.write(sel)
		q3.write("\n")
	q1.close()
	q3.close()
	#bram
	q2= open ("para.txt","w+")
	with open ("temp.txt","r") as q1:
		for line in q1:
			if "bram=0" in line:
				q2.write(line)
			elif "bram=1" in line:
				q2.write(line)			
	q2.close()
	q1.close()
	i=0
	with open("para.txt","r") as q1:		
		for line in q1:
			i+=1
	h=i
	if (h>0):
		print("\n")
		q3=open("para1.txt","a")
		print("Select one parameter for BRAM Block")
		q1=open("para.txt","r")
		print(q1.read())
		print("\n")
		sel=raw_input("Enter the selection >>>  ")
		q3.write(sel)
	q1.close()
	q3.close()
	
	# generating VHDL files
	des=[]
	
	for file in files:
		q1=open("y1.txt","w+")		
		xx=file
		xx=xx.replace(".vhd","")
		for line in fileinput.input(file):
			if "--#"in line:
				line=line.replace(" ","")
				line=line.replace("--#","")
				line=line.replace("\t","")
				q1=open("y1.txt","r")
				if line in q1:
					continue
				else:
					with open ("y1.txt","a") as q1:
						q1.write(line)		
		q1.close()
		 	
		file1_lst = []
		file2_lst = []
		temp26=[]
		with open ("para1.txt","r") as file1:
			
			for line_1 in file1:
				line_1=line_1.replace("\n","")
				file1_lst.append(line_1)
			with open ("y1.txt","r")as file2:
				
				for line_2 in file2:
					line_2=line_2.replace("\n","")
					file2_lst.append(line_2)
				same=set(file1_lst).intersection(file2_lst)
		same.discard("\n")
		for line in same:
				temp26.append(line)
                                                
						
		w=0				
		for x in range(len(temp26)):
			 print temp26[x]
			 w+=1
		
		print(w)
		
		
		
		if (w==4):
			y3=file
			y3=y3.replace(".vhd","")
			y7=y3
			y3= y3+"_"+"mod"
			y6=y3
			y3=y3+".vhd"
			des.append(y3)
			q1=open (y3,"w+")
			
			y8=temp26[0]
			y8="--#"+y8
			y10=temp26[1]
			y10="--#"+y10
			y11=temp26[2]
			y11="--#"+y11
			y12=temp26[3]
			y12="--#"+y12
			y9="--#"	
			with open (file) as f:
				try:
					for line in f:
						if y8 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y8 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
								
						elif y10 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y10 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
								
								
								
						elif y11 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y11 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
								
						elif y12 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y12 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
														
						elif y9 in line:
							
							
							line=next(f)
							while y9 not in line:
								
								
								line=next(f)
						else:
							q1.write(line.replace(y7, y6))		 		
				except StopIteration:
					print'ERROR in defining parameters in design file'
				else:
					print'-------------------File generated succesfully------------------------'
					
			
		elif (w==3):
			y3=file
			y3=y3.replace(".vhd","")
			y7=y3
			y3= y3+"_"+"mod"
			y6=y3
			y3=y3+".vhd"
			des.append(y3)
			q1=open (y3,"w+")
			line=temp26[0]
			y8=line
			y10=temp26[1]
			y10="--#"+y10
			y11=temp26[2]
			y11="--#"+y11
			print(y8)
			y8="--#"+y8
			print(y8)
			y9="--#"	
			with open (file) as f:
				try:
					for line in f:
						
						if y8 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--"," ")
							
							q1.write(line)
							line=next(f)
							while y8 not in line:
								line=line.replace("--"," ")
								q1.write(line)
								line=next(f)
						elif y10 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--"," ")
							
							q1.write(line)
							line=next(f)
							while y10 not in line:
								line=line.replace("--"," ")
								q1.write(line)
								line=next(f)
						elif y11 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--"," ")
							
							q1.write(line)
							line=next(f)
							while y11 not in line:
								line=line.replace("--"," ")
								q1.write(line)
								line=next(f)		
							
							
							
							
									
						elif y9 in line:
							
							
							line=next(f)
							while y9 not in line:
								
								
								line=next(f)
						else:
							q1.write(line.replace(y7, y6))		 		
				except StopIteration:
					print'ERROR in defining parameters in design file'
				else:
					print'-------------------File generated succesfully------------------------'
			q1.close()		
			
			
			
			
						
		elif (w==2):
			y3=file
			y3=y3.replace(".vhd","")
			y7=y3
			y3= y3+"_"+"mod"
			y6=y3
			y3=y3+".vhd"
			des.append(y3)
			q1=open (y3,"w+")
			
			y8=temp26[0]
			y8="--#"+y8
			y10=temp26[1]
			y10="--#"+y10
			
			y9="--#"	
			with open (file) as f:
				try:
					for line in f:
						if y8 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y8 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
								
						elif y10 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y10 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
								
										
						elif y9 in line:
							
							
							line=next(f)
							while y9 not in line:
								
								
								line=next(f)
						else:
							q1.write(line.replace(y7, y6))		 		
				except StopIteration:
					print'ERROR in defining parameters in design file'
				else:
					print'-------------------File generated succesfully------------------------'
					
			
						
		elif (w==1):
			y3=file
			y3=y3.replace(".vhd","")
			y7=y3
			y3= y3+"_"+"mod"
			y6=y3
			y3=y3+".vhd"
			des.append(y3)
			q1=open (y3,"w+")
			y8=temp26[0]
			
			y8="--#"+y8
			y9="--#"
				
			with open (file) as f:
				try:
					for line in f:
						if y8 in line:
							q1.write(line)
							line=next(f)
							line=line.replace("--","")
							q1.write(line)
							line=next(f)
							while y8 not in line:
								line=line.replace("--","")
								q1.write(line)
								line=next(f)
						elif y9 in line:
							
							line=next(f)
							while y9 not in line:
								
								line=next(f)
						else:
							q1.write(line.replace(y7, y6))		 		
				except StopIteration:
					print'ERROR in defining parameters in design file'
				else:
					print'-------------------File generated succesfully------------------------'
					
				
		elif (w==0):
			y3=file
			y3=y3.replace(".vhd","")
			y7=y3
			y3=y3+"_"+"org"
			y6=y3
			y3=y3+".vhd"
			des.append(y3)
			q1=open(y3,"w")
			with open(file) as f:
				try:
					for line in f:
						q1.write(line.replace(y7,y6))
				except StopIteration:
					print'ERROR in defining parameters in design file'
				else:
					print'--------------------File generated succesfully-----------------------------'
								
								
			
		
	# generating tcl file
	print'generating tcl files'
	g9=open("temp54.txt","w")
	for x1 in range(len(des)):
		des[x1]=des[x1].replace(".vhd","")
		
		ee=des[x1]
		g9.write(ee)
		g9.write("\n")
		ez=ee+".vhd"
		ef=ee+".tcl"
		el=ee+".vhd"
		ra1=open(ef,"w")
		ra= open("ma.py","r")
		for line in ra:
			if "read_vhdl"in line:
				ra1.write(line.replace("design1_pipelined.vhd",ez))
			elif "synth_design"in line:
				ra1.write(line.replace("design1_pipelined",ee))
			elif "set outputDir"in line:
				ra1.write(line.replace("my_design_output",ee))
			else:
				ra1.write(line)	
	
	
	
	
	g9.close()
	
'''	
	# running tcl file
	for line in range(len(des)):
		des[line]=des[line].replace(".vhd","")
		tt=des[line]
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




	
	for line in range(len(des)):
	
		ee = des[line]
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


     



	print("***************************************************Finished******************************************")

	
	q1.close()
	ra.close()
	ra1.close()
	x="rm viv*"
	y="rm -rf d1_*"
	y1="rm -rf d2_*"
	y2="rm -rf d3_*"
	y3="rm *.pyc"
	y4="rm *.txt"
	y5="rm -rf d*_mod"
	os.system(x)
	os.system(y)
	os.system(y1)
	os.system(y2)
	os.system(y3)
	os.system(y4)
	os.system(y5)

	
'''						
					
	
		 		

	

