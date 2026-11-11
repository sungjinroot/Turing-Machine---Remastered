
class Handle:
    @staticmethod
    def handleSyntaxError(Tokens):
        string = ""

        for Token in Tokens.lexemme:
            string += Token + " "
        print(f"Syntax Error: {string} at line {Tokens.line}")
        exit()
    
    @staticmethod
    def handleDuplicateLabel(Token):
        print("Duplicate label:", Token.lexemme[0],"on line:", Token.line)
        exit()

    @staticmethod
    def handleNonExisting(label,line):
        print("Non-Existent label:", label,"on line:", line)
        exit()