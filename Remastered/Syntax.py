from Remastered import Validation,Errors

class Parse:
    @staticmethod
    def parseInstruction(Token):
        if not (Validation.Validate.isLabel(Token.lexemme) or Token.lexemme[0] in ["LEFT","RIGHT","HALT"]):
            Errors.Handle.handleSyntaxError(Token)
    
    @staticmethod
    def parseAction(Token):
        if Token.lexemme[0] == "GOTO":
            return
        elif Token.lexemme[0] == "WRITE":
            if len(Token.lexemme[1]) != 1:
                Errors.Handle.handleSyntaxError(Token)
        else:
            Errors.Handle.handleSyntaxError(Token)
   
    @staticmethod
    def parseCondition(Token):
        if Token.lexemme[0] != "IF":
            Errors.Handle.handleSyntaxError(Token)

        if len(Token.lexemme[1]) < 1 or len(Token.lexemme[1]) > 1:
            Errors.Handle.handleSyntaxError(Token)
        
        if Token.lexemme[2] != "GOTO":
            Errors.Handle.handleSyntaxError(Token)