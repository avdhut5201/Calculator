
class Calculator:
    def __init__(self):
        self.expression= ""
        self.is_infix=True

    def set_Expression(self,expression):
       self.expression=expression
       return self.expression
    
    def get_Expression(self):
        return self.expression
    
    def get_Calculator(self,input):
        self.set_Expression(input)
        self.expression=self.get_Expression()
        return {"expression": self.expression, "is_infix": self.is_infix}
    
        
    def addition(self,first,second):
        self.first=first
        self.second=second

        return self.first + self.second
    
    def subtract(self,first,second):
        self.first=first
        self.second=second

        return self.first - self.second
    
    def multiplication(self,first,second):
        self.first=first
        self.second=second

        return self.first * self.second
    
    def divide(self,first,second):
        try:
            self.first=first
            self.second=second
        except:
            ZeroDivisionError("Can't divide by zero")
        else:
         return self.first / self.second
    def is_valid_infix(self,equation_object):
        operators = set("+-*/^")
        expression=equation_object["expression"]
        if(len(expression)<3 or expression.isnumeric() ):
            equation_object["is_infix"]=False
        infix_notation= expression.split()
        for note in range(0,len(infix_notation)):
           
            #  if((note%2==0 and not infix_notation[note].isdigit()) 
            #     and (note+1%2==1 and not infix_notation[note+1]not in operators) ):
            #     equation_object["is_infix"]=False
                
                
                if(note%2==0):
                    if(not infix_notation[note].isdigit()):
                        equation_object["is_infix"]=False
                        break;
                if(note%2==1):
                    if( infix_notation[note] not in operators):
                        equation_object["is_infix"]=False
                        break;



                

        return equation_object["is_infix"]


    def evaluation(self,expression_object):
        expression=expression_object["expression"]
        postfix_notation = expression.split()
        stack=[]
        for note in range(0,len(postfix_notation)):
            if(postfix_notation[note].isdigit()):
                stack.append(int(postfix_notation[note]))
            else:
                if(postfix_notation[note]=="+"):
                     a = stack.pop()
                     b = stack.pop()
                     temp=self.addition(b,a)
                     stack.append(temp)
                if(postfix_notation[note]=="-"):
                     a = stack.pop()
                     b = stack.pop()
                     temp=self.subtract(b,a)
                     stack.append(temp)
                if(postfix_notation[note]=="*"):
                     a = stack.pop()
                     b = stack.pop()
                     temp=self.multiplication(b,a)
                     stack.append(temp)
                if(postfix_notation[note]=="/"):
                     a = stack.pop()
                     b = stack.pop()
                     temp=self.divide(b,a)
                     stack.append(temp)




        result=stack.pop()
        return result
       
    



        


      