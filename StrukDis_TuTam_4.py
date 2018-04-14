def FSA(string):
	state = ''
	str_list = list(string)
	#print(str_list)
	for i in str_list:
		#print("input:",i)
		if state == '':
			state = state + str(i)
		else:
			if state != str(i):
				state = ''
			else:
				if len(state) == 1:
					state = state + str(i)

		#print("current state",state)

	if len(state) > 1:
		return True
	else:
		return False

print(FSA('0101010100011'))
print(FSA('010101010001'))
print(FSA('0101010100'))