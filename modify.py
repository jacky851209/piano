#!/usr/bin/python
import read_lilypond
def printing(input_file = ""):
	fp = open(input_file,"r")
	print()
	for x in range(1,5):
		line = fp.readline()
		
	line = fp.readline()
	note = []
	counted = 1
	print("-----------------------------------------------------------------------------------------------")
	while line:
	
		note = line.split()
		line2 = fp.readline()
		note = note + line2.split()
		line3 = fp.readline()
		note = note + line3.split()
		line4 = fp.readline()
		note = note + line4.split()
		
		count = []
		print("-----------------------------------------------------------------------------------------------")
		print()
		for x in range(0,len(note)):
			if note[x]== "\\break":
				break
			else:
				count.append(split_number(note[x]) + str(x))


		
		print(note)
		if note[0] != "\\break":
			print_line(count)
			print("        ",end = "")
			for x in range(0,len(note)):
				if note[x]== "\\break":
					break
				else:
					if counted < 10:
						print(" "+ str(counted) + "   " ,end = '')
					else:
						print(" "+ str(counted) + "  " ,end = '')
					counted = counted + 1
			print()
			
			note = []
			line = fp.readline()
			print("-----------------------------------------------------------------------------------------------")
		else:
			break
		
def split_number(noted):
	type = []

	if len(noted) == 1:
		type = str(0)
		type = type + noted[0]
	elif len(noted) == 2:
		type = str(1)
		type = type + noted[0]
	elif len(noted) == 3:
		if noted[-1] != "'":
			type = str(2)
			type = type + noted[0]
		else:
			type = str(5)
			type = type + noted[0]
	elif len(noted) == 4:
		if noted[-1] != "'":
			type = str(3)
			type = type + noted[0]
		else:
			type = str(6)
			type = type + noted[0]
	elif len(noted) == 5:
		if noted[-1] != "'":
			type = str(4)
			type = type + noted[0]
		else:
			type = str(7)
			type = type + noted[0]
	elif len(noted) == 6:
		type = str(8)
		type = type + noted[0]
	elif len(noted) == 7:
		type = str(9)
		type = type + noted[0]	
	return type
	
	
	
def print_line(count):
	do = []
	do_H = []
	re = []
	re_H = []
	mi = []
	mi_H = []
	fa = []
	fa_H = []
	so = []
	so_H = []
	la = []
	la_H = []
	si = []
	si_H = []

	print("        ",end = '')
	for x in range(0, len(count)):
		high = 0
		if int(count[x][0]) < 6:
			num = int(count[x][0])- 1
		else:
			high = 1
			num = int(count[x][0])- 6
			
		if num == 0:
			print( " " + str(num) + "   ",end = '')
		elif num > 0:
			print( "+" + str(num) + "   ",end = '')
		else:
			print( str(num) + "   ",end = '')
		
		
		if count[x][1] == 'b':
			si_H.append(high)
			si.append(count[x][2:])
		elif count[x][1] == 'a':
			la_H.append(high)
			la.append(count[x][2:])
		elif count[x][1] == 'g':
			so_H.append(high)
			so.append(count[x][2:])
		elif count[x][1] == 'f':
			fa_H .append(high)
			fa.append(count[x][2:])
		elif count[x][1] == 'e':
			mi_H.append(high)
			mi.append(count[x][2:])
		elif count[x][1] == 'd':
			re_H.append(high)
			re.append(count[x][2:])
		else:
			do_H.append(high)
			do.append(count[x][2:])

	print("\n")
	print("    $  ",end = '')
	print("--------------------------------------------------------------------------------")
	print("    $  ",end = '')
	print()
	print("    $  ",end = '')
	print("--------------------------------------------------------------------------------")
	print("    $  ",end = '')
	print()
	print_even(si, si_H)
	print_odd(la, la_H)
	print_even(so, so_H)
	print_odd(fa, fa_H)
	print_even(mi, mi_H)
	print_odd(re, re_H)
	for_do(do, do_H)
	print()


def print_even(notee = [], high = []):
	print("    $  ",end = '')
	count = 0
	for x in range(0,16):
		counting = True
		for y in notee:
			if int(y) == x:
				if high[count] == 0:
					print("--o--",end = '')
					counting = False
					break
				else:
					print("-#o--",end = '')
					counting = False
					break
				count = count + 1
		if counting == True:
			print("-----",end = '')

	print()

def print_odd(notee = [], high = []):
	print("    $  ",end = '')
	count = 0
	for x in range(0,16):
		counting = True
		for y in notee:
			if int(y) == x:
				if high[count] == 0:
					print("  o  ",end = '')
					counting = False
					break
				else:
					print(" #o  ",end = '')
					counting = False
					break
				count = count + 1
		if counting == True:
			print("     ",end = '')

	print()

def for_do(notee = [], high = []):
	print("       ",end = '')
	count = 0
	for x in range(0,16):
		counting = True
		for y in notee:
			if int(y) == x:
				if high[count] == 0:
					print("--o--",end = '')
					counting = False
					break
				else:
					print("-#o--",end = '')
					counting = False
					break
				count = count + 1
		if counting == True:
			print("     ",end = '')

	print()
def main(input_file):

	printing(input_file)
	read_lilypond.main(input_file)

	