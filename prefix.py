def PrefixToPosfix():    
    stack = []

    operators = set(['+', '-', '*', '/', '^'])    
    s = s[::-1]

    for i in s:
        if i in operators:            
            a = stack.pop()
            b = stack.pop()
            
            temp = a+b+i
            stack.append(temp)
        else:
            stack.append(i)    
    print(*stack)


def prefixToInfix(prefix):
	stack = []
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):		
			stack.append(prefix[i])
			i -= 1
		else:		
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False
