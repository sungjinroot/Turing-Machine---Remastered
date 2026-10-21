from Analyzers import Lexer

Tokens = Lexer.Tokenize.scan("test.txt")
Tokens = Lexer.Tokenize.parse(Tokens)

if len(Tokens) == 0:
    print("Empty Program")
    exit()

for Token in Tokens:
    print(Token)
    

#Check if empty program - 
#Check if unknown command - done
#Wrong argument count - done
#invalid symbol or label 
#Duplicate label or missing target
