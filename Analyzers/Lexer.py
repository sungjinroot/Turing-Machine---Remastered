
class Tokenize:
    
    @staticmethod
    def scan(filename):
        instructions = []

        with open(filename,"r") as input_file:
            for line in input_file:

                instruction = Tokenize.validate(line)

                if len(instruction) != 0:
                    if instruction == "Invalid":
                        return "Invalid"

                    instructions.append(instruction)

        return instructions
    
    @staticmethod
    def validate(line):
        parsed = line.strip().split()

        if len(parsed) == 1:

            if parsed[0][-1] == ":":
                return parsed

            if parsed[0] not in ["LEFT","RIGHT","HALT"]:
                print("Invalid Instruction")
                return "Invalid"
            
        
        elif len(parsed) == 2:
            pass
        
        elif len(parsed) == 3:
            print("Invalid Arguments")
            return "Invalid"
        
        elif len(parsed) == 4:
            pass
        
        elif len(parsed) > 4:
            print("Invalid Arguments")
            return "Invalid"

        return parsed        
        
        
        
        
        
        #1 Arg
        #Check if LEFT,WRITE,HALT,or has : at the end for 1. 

        #Check for GOTO [label]
        #Check for WRITE [char]

        #Check for IF [char] GOTO [label]
        
        pass

#Check if empty program
#Check if unknown command
#Wrong argument count
#invalid symbol or label 
#Duplicate label or missing target
