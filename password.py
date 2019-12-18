import random
class password_creator():
    def __init__(self,n,total):
        self.total =  total
        self.n  = n
    def alpha_rand_func(self):
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_pass = ""
        for i in range(0,(self.n//2)):
            alpha_pass +=  random.choice(alpha)
        self.n -= self.n // 2
        self.total += alpha_pass
        #print(alpha_pass)
    def int_rand_func(self):
        int_ = str(1234567890) 
        int_pass = ""
        for i in range(0,self.n):       
            int_pass  += random.choice(int_)
        self.total += int_pass
        #print(int_pass)
    def symbol_rand_func(self):
        symbol = " ,./;'\[]-=`<>?:|{ }_+~"
        sym_pass = ""
        for i in range(0,5):
            sym_pass += random.choice(symbol)
        self.n -= 5
        self.total += sym_pass
        #print(sym_pass)
    def jumbling_func(self):
        length  = len(self.total)
        jumbled_output = ""
        for x in self.total:
            jumbled_output += random.choice(self.total)
        print("Password: ",jumbled_output)
        

def inp_():
   number_of_sug = int(input("How many password do you want to make: "))
   inp_ut = password_creator(int(input("No. of characters: ")),"")
   for x in range(0,number_of_sug):  
    
    inp_ut.symbol_rand_func()
    inp_ut.alpha_rand_func()
    inp_ut.int_rand_func()
    inp_ut.jumbling_func()
   return " "

    
print(inp_())
