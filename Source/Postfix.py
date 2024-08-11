class Postfix:
    def __init__(self,expression) -> None:
        self.expression=expression
    
    def evaluation(self):
        postfix_notation = list(self.expression) 

        return postfix_notation