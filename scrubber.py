f = open('postOfficeConvert.csv', 'r')
x = open('postOffice.json', 'w')
for line in f:
	str = ""
	arr = line.split(",")
	str += arr[0] + ":["
	str += arr[1] + ","
	str += arr[2] + ","
	str += arr[3] + ","
	str += arr[4] + ","
	str += arr[5] + ","
	str += arr[6][1:-1] + ","
	str += arr[7][1:-1] + ","
	str += arr[8] + ","
	str += arr[9] + ","
	str += arr[10] + ","
	str += arr[11] + ","
	str += arr[12] + ","
	str += arr[13] + ","
	str += arr[14] + ","
	str += arr[15] + ","
	str += arr[16] + ","
	str += arr[17] + ","
	str += arr[18] + ","
	str += arr[19] + ","
	str += arr[20] + ","
	str += arr[21] + ","
	str += arr[22] + ","
	str += arr[23] + "]" + ","
 	x.write(str)