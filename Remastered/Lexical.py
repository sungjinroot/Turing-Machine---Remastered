from Remastered import Tokenize,Validation

class Lex:
    @staticmethod
    def scan(filename):
        instructions = []
        sourceLine = 0

        with open(filename,"r") as source:
            for line in source:
                instruction = line.strip().split()
                sourceLine += 1

                if len(instruction) != 0: 
                    if Validation.Validate.isLineLabelized(instruction):
                        instructions.append(Tokenize.Token(sourceLine,[instruction[0]]))
                        instruction.pop(0)
                        instructions.append(Tokenize.Token(sourceLine,instruction))
                        
                    else: 
                        if Validation.Validate.isLabel(instruction):
                            print(f"Label only line found in {sourceLine}")
                            exit()

                        instructions.append(Tokenize.Token(sourceLine,instruction))
                    
        return instructions  
    
