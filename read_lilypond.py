import save_notefile
def main(input_file = ""):
	
	fp = open(input_file,"r") #file to modify
	
	
	line = fp.readline()
	c = 1 #current line
	noteBuffer = []	#store notes
	speed = []
	avaiNotes = ["c,", "d,", "e,", "f,", "g,", "a,", "b,",
	"des,", "ees,", "ges,", "aes,", "bes,",
	"c", "d", "e", "f", "g", "a", "b",
	"des", "ees", "ges", "aes", "bes",
	"c'", "d'", "e'", "f'", "g'", "a'", "b'",
	"des'", "ees'", "ges'", "aes'", "bes'",
	"c''", "d''", "e''", "f''", "g''", "a''", "b''",
	"des''", "ees''", "ges''", "aes''", "bes''",
	"c'''", "d'''", "e'''", "f'''", "g'''", "a'''", "b'''",
	"des'''", "ees'''", "ges'''", "aes'''", "bes'''"] #available notes
	#read file
	while line:
		if c < 4: #skip first 3 lines
			c += 1
			line = fp.readline()
		elif c == 4: #get time
			t1 = line[7]
			t2 = line[9]
			c += 1
		else: #start read note
			line = fp.readline()
			temp = line.split() #whitespace as delimiter
			attr = line[0] #attribute of line	
			if attr == "}": #finish read note
				break
			else:
				for t in temp:
					noteBuffer.append(t) 
					speed.append(400)
		
	while 1: #user option	
		print("\nWhat would you like to do?")
		print("1.View notes\n2.Modify notes")
		print("3.Add notes\n4.Delete notes")
		print("5.Modify speed\n6.Save notes")
		user = input("-1 for exit: ")
		
		if int(user) == -1: #end of modify
			break
		elif int(user) == 1:
			view_note(noteBuffer, t1, t2)
		elif int(user) == 2:
			modify_note(noteBuffer, avaiNotes)
		elif int(user) == 3:
			add_note(noteBuffer, avaiNotes)
		elif int(user) == 4:
			delete_note(noteBuffer)
		elif int(user) == 5:
			speed = modify(noteBuffer, speed)
		elif int(user) == 6:
			save_note(noteBuffer, input_file, speed)
		else:
			print("Invalid number, please try again!")
			
	fp.close()
	
	#write file
	fw = open(input_file,"w")
	fw.write("% set the starting point to middle C\n")
	fw.write("\n{\n")
	fw.write("\t\\time " + str(t1) + "/" + str(t2) + "\n\t")
	j = 1	
	for i in noteBuffer:
		fw.write(str(i) + " ")
		if j % 4 == 0:
			fw.write("\n\t")
		j += 1
	fw.write("\n}")
	
	fw.close()

	
def view_note(noteBuffer, t1, t2):
	print("\ntime: " + str(t1) + "/" + str(t2))
	print(str(noteBuffer))					
	print("There are " + str(len(noteBuffer)) + " notes in the list")

def modify_note(noteBuffer, avaiNotes):
	while 1:	
		print("\nPlease enter the index of the note which you want to change(index start with 1)")
		index = input("-1 to exit modify: ")
		if int(index) == -1:
			break		
		if int(index) > len(noteBuffer) - 1 or int(index) < 1: #last one is '\break'
			print("Your input is not available, please try again!!")
			continue
		symbol = input("Please enter the note symbol: ")
		if symbol not in avaiNotes: #skip invalid notes
			print("Your input is not available, please try again!!")
			continue            		
		noteBuffer[int(index) - 1] = symbol #replace note

def add_note(noteBuffer, avaiNotes):
	while 1:	
		print("\nPlease enter the index of the note which you want to add(index start with 1)")
		index = input("-1 to exit add: ")
		if int(index) == -1:
			break		
		if int(index) > len(noteBuffer) or int(index) < 1:
			print("Your input is not available, please try again!!")
			continue  
		symbol = input("Please enter the note symbol: ")
		if symbol not in avaiNotes: #skip invalid notes
			print("Your input is not available, please try again!!")
			continue      		
		noteBuffer.insert(int(index) - 1, symbol) #add note
		
def delete_note(noteBuffer):
	while 1:	
		print("\nPlease enter the index of the note which you want to delete(index start with 1)")
		index = input("-1 to exit delete: ")
		if int(index) == -1:
			break		
		if int(index) > len(noteBuffer) - 1 or int(index) < 1: #last one is '\break'
			print("Your input is not available, please try again!!")
			continue      		
		del noteBuffer[int(index) - 1] #delete note

def save_note(noteBuffer, input_file, speed):
	save_notefile.main(noteBuffer, input_file, speed)
	
def modify(noteBuffer, speed):
	while 1:
		print("\nPlease enter the index of the note which you want to modify(index start with 1)")
		index = input("-1 to exit add: ")
		if int(index) == -1:
			break
		if int(index) > len(noteBuffer) - 1 or int(index) < 1:
			print("Your input is not available, please try again!!")
			continue
		spe = input("Please enter the speed(default:400): ")
		speed[int(index) -1] = int(spe)
	return speed
