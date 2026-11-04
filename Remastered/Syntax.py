from Remastered import Validation

class Verify:
    @staticmethod
    def validateInstruction(Token):
        if not (Validation.Validate.isLabel(Token.lexemme) or Token.lexemme[0] in ["LEFT","RIGHT","HALT"]):
            print(f"Syntax Error: {Token.lexemme[0]} at line {Token.line}")
            exit()
    
    @staticmethod
    def validateAction(Token):
        if Token.lexemme[0] == "GOTO":
            return
        elif Token.lexemme[0] == "WRITE":
            if len(Token.lexemme[1]) != 1:
                print(f"Syntax Error: {Token.lexemme[0]} {Token.lexemme[1]} at line {Token.line}")
                exit()
        else:
            print(f"Syntax Error: {Token.lexemme[0]} {Token.lexemme[1]} at line {Token.line}")
            exit()
   
    @staticmethod
    def validateCondition(Token):
        if Token.lexemme[0] != "IF":
            print(f"Syntax Error: {Token.lexemme[0]} at line {Token.line}")
            exit()

        if len(Token.lexemme[1]) < 1 or len(Token.lexemme[1]) > 1:
            print(f"Syntax Error: {Token.lexemme[0]} at line {Token.line}")
            exit()
        
        if Token.lexemme[2] != "GOTO":
            print(f"Syntax Error: {Token.lexemme[0]} at line {Token.line}")
            exit()