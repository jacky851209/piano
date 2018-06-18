def main(input_file = [], filename = "", speed = []):
	counting = 1
	fw = open( filename[0:-5] + "yml",'w')

	for x in range(0, len(input_file) - 1):
		fw.write("note_" + str(counting) + ":")
		fw.write("\n  - " + char(input_file[x]))
		fw.write("\n  - " + str(input_file[x].count("'") + 1))
		fw.write("\n  - 0")
		fw.write("\n  - " + str(speed[x]))
		fw.write("\n  - " + str(cout(input_file[x])))
		fw.write("\n  - " + deter(input_file[x]))
		fw.write("\n\n")
		counting = counting + 1
		
	fw.close()

def char(input = ""):
	out = input.strip("'")
	if len(out) == 1:
		return out
	else:
		return out[0] + "s"
	
def deter(input = ""):
	if len(input) < 3:
		return "true"
	else:
		if input[1] == "'":
			return "true"
		else:
			return "false"
			
def cout(input = ""):
	table = [28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121, 124, 127, 130]
	table2 = [30, 33, 39, 42, 45, 51, 54, 60, 63, 66, 72, 75, 81, 84, 87, 93, 96, 102, 105, 108, 114, 117, 123, 126, 129]
	counting = input.count("'")
	out = input.strip("'")
	if len(out) == 1:
		if out == "c":
			return table[7 * counting]
		elif out == "d":
			return table[7 * counting + 1]
		elif out == "e":
			return table[7 * counting + 2]
		elif out == "f":
			return table[7 * counting + 3]
		elif out == "g":
			return table[7 * counting + 4]
		elif out == "a":
			return table[7 * counting + 5]
		elif out == "b":
			return table[7 * counting + 6]
	else:
		if out[0] == "d":
			return table2[5 * counting]
		elif out[0] == "e":
			return table2[5 * counting + 1]
		elif out[0] == "g":
			return table2[5 * counting + 2]
		elif out[0] == "a":
			return table2[5 * counting + 3]
		elif out[0] == "b":
			return table2[5 * counting + 4]
