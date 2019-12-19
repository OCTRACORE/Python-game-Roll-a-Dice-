import random
class password_creator(): 
    def __init__(self,n,jumbled_output,final_output): #making the local variable
        self.n  = n
        self.jumbled_output = jumbled_output
        self.final_output = final_output
    def alpha_rand_func(self): # for alphabetical part of the password
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_pass = "" # stores alphabetical part of the variable
        for i in range(0,(self.n//2)): #for inserting random alphabets
            alpha_pass +=  random.choice(alpha)
        
        for x in range(self.n // 2):
            self.jumbled_output += random.choice(alpha_pass) #for inserting random alphabets shortlisted previously in jumbled_output
        self.n -= self.n // 2
        #print(alpha_pass)

    def int_rand_func(self):  #for numerical part of the password
        int_ = str(1234567890) 
        int_pass = "" #stores numerical part of the variable
        for i in range(0,self.n):       
            int_pass  += random.choice(int_) #inserting random integers for the
        for x in range(self.n): #for inserting random numbers shortlisted previously in jumbled_output
            self.jumbled_output += random.choice(int_pass)        
        #print(int_pass)
    def symbol_rand_func(self):
        symbol = ",./;'\[]-=`<>?:|{ }_+~" 
        sym_pass = "" #for storing symbolic prt of the password
        for i in range(0,5):
            sym_pass += random.choice(symbol) #inserting random symbols in sym_pass
        for i in range(5):
            self.jumbled_output += random.choice(sym_pass) #for inserting random symbols shortlisted previously in jumbled_output
        self.n -= 5

        #print(sym_pass)
    def jumbling_func(self):
       for i in self.jumbled_output:
           self.final_output += random.choice(self.jumbled_output)
       print(self.final_output)
     
    def clear(self): # for clearing the final_output and jumbled_output
        self.final_output = ""
        self.jumbled_output = ""
        
    
def inp_ut(): # for user input
  suggestions = int(input("no. of suggestions: ")) # for the no. of suggestions of password the user wants
  inp_ = password_creator(int(input("no. of characters: ")),"","")
  while inp_.n <=5 : # no. of characters cannot be less or equal to 5
   inp_ = password_creator(int(input("no. of characters: ")),"","")
  else:
    for x in range(suggestions): #running the methods the desired number of times
  
      inp_.symbol_rand_func()
      inp_.alpha_rand_func()
      inp_.int_rand_func()
      inp_.jumbling_func()
      inp_.clear()
  return " "   
print(inp_ut())
