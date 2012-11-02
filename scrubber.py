f = open('final.csv', 'r')
x = open('postOfficeFinal.json', 'w')
for line in f:
	str = ""
	arr = line.split(",")
	str += arr[0][:-1] +  arr[3][1:-1] + arr[4][1:]+ ":["
	str += arr[1] + ","
	str += arr[3] + ","
	str += arr[4] + ","
	str += arr[5][1:-1] + ","
	str += arr[6][1:-1] + ","
	str += arr[7] + ","
	str += arr[8][:-1] + "]" + ","
 	x.write(str)