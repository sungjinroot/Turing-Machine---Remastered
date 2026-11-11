from Remastered import Validation

class Token:
    def __init__(self,line,lexemme):
        self.line = line 
        self.lexemme = lexemme
        self.token = None
        self.size = len(lexemme)
        self.isLabel = Validation.Validate.isLabel(lexemme)


