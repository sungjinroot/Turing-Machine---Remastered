from Remastered import Errors,Validation

class Analyze:
    def __init__(self,Tokens):
        self.Tokens = Tokens
        self.labels = self.getLabels()
        self.indexes = self.getIndexes()
        self.verifyLabels()

    def getLabels(self):
        labels = []

        for Token in self.Tokens:
            if Token.isLabel:
                label = Token.lexemme[0][:-1]

                if label in labels:
                    Errors.Handle.handleDuplicateLabel(Token)
                else:
                    labels.append(label)
        return labels

    def verifyLabels(self):
        for Token in self.Tokens:
            if not Token.isLabel:
                if Token.lexemme[0] == "GOTO":
                    self.verifyExistence(Token.lexemme[1],Token.line)
                elif Token.lexemme[0] == "IF":
                    self.verifyExistence(Token.lexemme[3],Token.line)

    def verifyExistence(self,label,line):
        if label not in self.labels:
            Errors.Handle.handleNonExisting(label,line)

    def getIndexes(self):
        indexes = {}

        index = 0

        for Token in self.Tokens:
            if Token.isLabel:
                indexes[Token.lexemme[0]] = index
                index += 1
            else:
                index += 1

        return indexes
