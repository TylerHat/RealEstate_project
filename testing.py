def getHouseInfoLEFT(lineNum, start_substring, end_substring_will_lookleft,file="sandbox.txt" ):
	with open(file, "r", encoding="utf-8") as file:
		lines = file.readlines()

	if len(lines) >= lineNum:
		line_2 = lines[(lineNum-1)]
		line_2 = line_2.strip()  # Optional: Remove leading/trailing whitespace

		# Print or use the value of line 2 as needed
		#print(line_2)
	else:
		print("The file does not any records")

	text = line_2

	start_index = text.find(start_substring)
	if start_index != -1:
		end_index = text.rfind(end_substring_will_lookleft, 0, start_index)
		if end_index != -1:
			#end_index += len(end_substring_will_lookleft)
			result = text[end_index + len(end_substring_will_lookleft):start_index]
			return(result)
		else:
			print(f"Substring {end_substring_will_lookleft} not found before {start_substring}")
	else:
		print(f"Substring {start_substring} not found")


tester = getHouseInfoLEFT(2,"on Zillow","\">")
print(tester)
