from Remastered import Lexical,Syntax,Semantic,Errors,Storage
import time

Tokens = Lexical.Lex.scan("test.txt")

for Token in Tokens:
    if Token.size == 4:
        Syntax.Parse.parseCondition(Token)
    elif Token.size == 2:
        Syntax.Parse.parseAction(Token)
    elif Token.size == 1:
        Syntax.Parse.parseInstruction(Token)
    else:
        Errors.Handle.handleSyntaxError(Token)

instructions = Semantic.Analyze(Tokens)
TuringMachine = Storage.Tape()

Halted = False
index = 0
step = 0

while Halted != True or index < instructions.size:
    for counter in range(index,instructions.size):
        instruction = instructions.getInstruction(index)
        
        if len(instruction) == 1:
            if instruction[0] == "LEFT":
                TuringMachine.left()

            elif instruction[0] == "RIGHT":
                TuringMachine.right()
            #halt here    
        
        elif len(instruction) == 2:
            if instruction[0] == "GOTO":
                index = instructions.jumpTable[instruction[1]]
                break
            
            elif instruction[0] == "WRITE":
                TuringMachine.write(str(instruction[1]))
        
        elif len(instruction) == 4:
            if instruction[1] == TuringMachine.read():
                index = instructions.jumpTable[instruction[3]]
                break
        
        index += 1

        time.sleep(0.5)
    step += 1

    if step >= 10000:
        print("Runtime Error")
        break