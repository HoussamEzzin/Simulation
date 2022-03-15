

class Alea:
    def __init__(self,IX,IY,IZ):
        self.IX=IX
        self.IY=IY
        self.IZ=IZ


    def alea(self):
        self.IX = 171*(self.IX % 177)-2*(self.IX//177)
        self.IY = 172*(self.IY % 176)-35*(self.IY//176)
        self.IZ = 170*(self.IZ % 178)-63*(self.IZ//178)

        if(self.IX<0):
            self.IX=self.IX+30269
        if(self.IY<0):
            self.IY=self.IY+30307
        if(self.IZ<0):
            self.IZ=self.IZ+30323

        inter = ((self.IX/30269) + (self.IY/30307) + (self.IZ/30323))
        alea = inter-int(inter)
        return (alea)


    def affciher(self):
        print("les germes sont IX ={},IY ={},IZ ={}".format(self.IX,self.IY,self.IZ))



