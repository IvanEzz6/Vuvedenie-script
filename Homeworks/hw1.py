#Decoding:
string = input('Enter string to decode: ')
res = ''
for i in range(0, len(string), 2):
	res += int(string[i+1])*string[i]
print(f'Result: {res}')

#Encoding:
string = input('Enter a string to encode: ')
res=''
count=0
targetChar=string[0]
for char in string:
	if char == targetChar:
		count+=1
	else:
		res += targetChar + str(count)
		count=1
		targetChar=char
res+= targetChar + str(count)
print(f"Result: {res}")