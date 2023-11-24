class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" and len(stack) > 0 and  stack[len(stack) - 1] == "(":
                stack.pop()
            elif i == "}" and len(stack) > 0 and  stack[len(stack) - 1] == "{":
                stack.pop()  
            elif i == "]" and len(stack) > 0 and  stack[len(stack) - 1] == "[":
                stack.pop()      

            else:
                return False
        
        
        if len(stack) > 0:
            return False
        else:
            return True