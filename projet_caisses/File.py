class file:
    def __init__(self):
        self.file=[]

    def enfiler(self,info):
        if info not in self.file:
            self.file.insert(0,info)
            return (True)
        return (False)

    def defiler(self):
        if len(self.file) > 0:
            return self.file.pop()
        return ("File vide!")

    def size(self):
        return len(self.file)

    def affFile(self):
        return self.file