int_str = input('Enter something...')
char_count = {}
for char in int_str :
    char_count[char] = char_count.get(char,0)+1
#print("Freq of chars : ",char_count)

for k, v in char_count.items():
	print(k, '|',v)