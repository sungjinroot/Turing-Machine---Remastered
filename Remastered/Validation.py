
class Validate:
    @staticmethod
    def isLabel(token):
        if token[0][-1] == ":":
            return True
        return False
    
    @staticmethod
    def isLineLabelized(instruction):
        if instruction[0][-1] == ":" and len(instruction) != 1:
            return True
        return False