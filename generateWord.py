# 3[a] --> aaa
# 3[a]2[b] --> aaabb
# 3[2[a]b] --> aabaabaab

def generateWord(inputStr):
	stack = list()	
	#temp_str = ""
	for idx in range(0, len(inputStr)):
		if inputStr[idx] != "]":
			stack.append(inputStr[idx])
		else:
			temp_char = ""
			while (stack[len(stack) - 1] != "[" ):
				temp_char = stack.pop() + temp_char
			stack.pop()	
			numOfTimes = int(stack.pop())
			stack.append(temp_char * numOfTimes)
	return "".join(stack)

print generateWord("3[a]")
print generateWord("3[a]2[b]")
print generateWord("3[2[a]b]")
print generateWord("2[3[2[a]b]c]")
					
			
