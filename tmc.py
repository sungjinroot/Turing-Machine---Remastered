from Analyzers import Lexer

Tokens = Lexer.Tokenize.scan("test.txt")

if Tokens == "Invalid":
    print("Invalid")
    exit()

for i in Tokens:
    print(i)

