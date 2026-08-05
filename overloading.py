# overloding
class instrument:
    def __init__(self,name):
        self.name = name
    def play(self):
        print("Playing the instrument")
class guitar(instrument):
    def __init__(self,name,brand):
        super().__init__(name)
        self.brand = brand
    def play(self):
        print("Playing the guitar")
        super().play()
i = guitar("Guitar","Fender")
i.play()
i1 = instrument("Piano")
i1.play()    