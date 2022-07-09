def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def isOperator(x): 
    if x == "+":
        return True 
    if x == "-":
        return True 
    if x == "/":
        return True 
    if x == "*":
        return True 
    return False
 
def PostfixToInfix(exp) : 
    s = [] 
    for i in exp:                     
        if (isOperand(i)) :        
            s.insert(0, i)
        else:         
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i +
                             op1 + ")")                 
    return s[0]

def PostfixToPrefix(post_exp): 
    s = []
    length = len(post_exp) 
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)        
        else:
            s.append(post_exp[i])     
    ans = ""
    for i in s:
        ans += i
    return ans  