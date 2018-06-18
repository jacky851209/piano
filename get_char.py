import modify
def main(input_file = ""):
	
	fp = open(input_file,"r")
	fw = open(input_file[0:-3]+"lytex","w")
	fw.write("% set the starting point to middle C\n")
	fw.write("\n")
	fw.write("{\n")
	name = input("Enter your Rhythm: ")
	while int(name) < 10:
		name = input("Enter your Rhythm: ")
	fw.write("\t\\time " + name[0] + "/" + name[1] + "\n")
	line = fp.readline()
	count = 0
	Note = ""
	Level = ""
	White = ""
	begin = 0
	while line:
		if count != 7:
			count = count + 1
		else:
			count = 0

			if begin == 0:
				fw.write("\t")

			if White == "true":
				begin = begin + 1

				if Level == "1":
					fw.write(str(Note).lower() + ' ')
				elif Level == "2":
					fw.write(str(Note).lower()+ "'" + ' ')
				elif Level == "3":
					fw.write(str(Note).lower()+ "''"+ ' ')
				elif Level == "4":
					fw.write(str(Note).lower()+ "'''"+ ' ')
				elif Level == "5":
					fw.write(str(Note).lower()+ "''''" + ' ')

				
			else:
				begin = begin + 1
				if Level == "1":
					fw.write(set_black(Note) + ' ')
				elif Level == "2":
					fw.write(set_black(Note)+ "'" + ' ')
				elif Level == "3":
					fw.write(set_black(Note)+ "''" + ' ')
				elif Level == "4":
					fw.write(set_black(Note)+ "'''" + ' ')
				elif Level == "5":
					fw.write(set_black(Note)+ "''''" + ' ')

			if begin == 4:
				begin = 0
				fw.write("\n")
				
		if count == 2:
			Note = line[4:-1]
			#print(line[4:])
			
		if count == 3:
			Level = line[4:-1]
			#print(line[4:])
			
		if count == 7:
			White = line[4:-1]
			#print(line[4:])
		line = fp.readline()
	fw.write("\\break\n")
	fw.write("}")
	fw.close()
	fp.close()

def set_black(note):
	if note == "cs":
		return "des"
	elif note == "ds":
		return "des"
	elif note == "fs":
		return "ges"
	elif note == "gs":
		return "aes"
	elif note == "as":
		return "bes"
		
if __name__ == "__main__":
	input_file = input("Please input your file name (*.yml): ")
	main(input_file)
	modify.main(input_file[0:-3]+"lytex")