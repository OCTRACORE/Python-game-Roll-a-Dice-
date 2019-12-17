class password_manager():
    def __init__(self, n_,strength):
        self.strength = strength
        self.n_ = n_
    def input_(self):
        self.n_ = int(input("number of characters: "))
        self.strength =  input("Strength: ")
password_manager.input_(self)
