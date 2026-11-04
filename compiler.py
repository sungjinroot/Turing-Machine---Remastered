from Remastered import Lexical,Syntax

Tokens = Lexical.Lex.scan("test.txt")

for Token in Tokens:
    if Token.size == 4:
        Syntax.Verify.validateCondition(Token)
    
    elif Token.size == 2:
        Syntax.Verify.validateAction(Token)
    
    elif Token.size == 1:
        Syntax.Verify.validateInstruction(Token)
    