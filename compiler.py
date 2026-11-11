from Remastered import Lexical,Syntax,Semantic,Errors

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

Instructions = Semantic.Analyze(Tokens)




