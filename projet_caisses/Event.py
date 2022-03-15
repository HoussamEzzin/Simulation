

class Evenement:
    def __init__(self,ref,type,date):
        self.reference=ref
        self.type=type
        self.date=date

    def afficher_event(self):
        return ("[ref:{} type:{} date:{}]".format(self.reference,self.type,self.date))