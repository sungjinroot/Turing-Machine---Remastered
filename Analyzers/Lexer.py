
class Tokenize:
    
    @staticmethod
    def scan(filename):
        instructions = []

        with open(filename,"r") as input_file:
            for line in input_file:

                instruction = line.strip().split()

                if len(instruction) != 0:
                    instructions.append(instruction)
                    
        return instructions        

    @staticmethod
    def isLabel(instruction):
        label = instruction[0]

        if label[-1] == ":":
            return True
        return False

    @staticmethod
    def parse(Tokens):
        
        instructions = []

        for Token in Tokens:
            if Tokenize.isLabel(Token):
                instruction = Token
        
                instructions.append([instruction[0]])
                instruction.pop(0)
                instructions.append(instruction)        
                  
            else:
                instructions.append(Token)

        return instructions