
from random import choice
def stone_paper_scissor(): #g = guess

  print("Choose either of the following:")
  print("     stone, paper, scissor")
  comp = 0  # computer's score
  user = 0  # user's score
  guess = ("stone", "paper", "scissor")  # guess
  for i in range(3):

#------------------------------------------------------------------------------
    guess = ("stone", "paper", "scissor")# guess
    user_g = input('ENTER YOUR GUESS:')
    user_g.lower()
    comp_g = choice(guess) #computer"s guess
#------------------------------------------------------------------------------
      # when both parties guess are the same
    if comp_g == user_g:
        print( "--------------------------------------" )
        print( "IT'S A DRAW!" )
        print( "--------------------------------------" )
#-------------------------------------------------------------------------
      # when computer chooses stone(guess[0])
    if comp_g == guess[0]:
         if user_g == guess[1]:
               print( "----------------------------------" )
               print( "YOU WIN!" )
               print( "----------------------------------" )
               print("COMPUTER:"+ comp_g)
               print("USER:"+ user_g)
               user += 1
               print("USER: %d" %(user))
               print("COMPUTER: %d" %(comp))
         elif user_g == guess[2]:
               print( "----------------------------------" )
               print( "YOU LOSE!" )
               print( "----------------------------------" )
               print("COMPUTER:"+ comp_g)
               print("USER:"+ user_g)
               comp += 1
               print("USER: %d" %(user))
               print("COMPUTER: %d" %(comp))
#-------------------------------------------------------------------------
      # when computer chosses paper(guess[1])
    if comp_g == guess[1]:
         if user_g == guess[0]:
               print( "----------------------------------" )
               print( "YOU LOSE!" )
               print( "----------------------------------" )
               print("COMPUTER:"+ comp_g)
               print("USER:"+ user_g)
               comp += 1
               print("USER: %d" %(user))
               print("COMPUTER: %d" %(comp))
         elif user_g == guess[2]:
               print( "----------------------------------" )
               print( "YOU WIN!" )
               print( "----------------------------------" )
               print("COMPUTER:" + comp_g)
               print("USER:" + user_g)
               user += 1
               print("USER:  %d" %(user))
               print("COMPUTER: %d" %(comp))
#---------------------------------------------------------------------------
      # when computer chooses scissor (guess[2])
    if comp_g == guess[2]:
         if user_g ==  guess[0]:
               print( "----------------------------------" )
               print( "YOU WIN!" )
               print( "----------------------------------" )
               print("COMPUTER:"+ comp_g)
               print("USER:"+ user_g)
               user += 1
               print("USER:  %d" %(user))
               print("COMPUTER:  %d" %(comp))
         elif user_g == guess[1]:
               print( "----------------------------------" )
               print( "YOU LOSE!" )
               print( "----------------------------------" )
               print("COMPUTER:"+ comp_g)
               print("USER:"+ user_g)
               comp += 1
               print("USER: %d" %(user))
               print("COMPUTER: %d" %(comp))
#--------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------

 #---------------------------------------------------------------
  if comp > user:
      print("-----------------------------------")
      print("YOU LOSE")
      print("-----------------------------------")
      print("USER: %d" % (user))
      print("COMPUTER: %d" % (comp))
 #---------------------------------------------------------------
  elif comp < user:
      print("-----------------------------------")
      print("YOU WIN")
      print("-----------------------------------")
      print("USER: %d" % (user))
      print("COMPUTER: %d" % (comp))
 #---------------------------------------------------------------
  else:
      print("-----------------------------------")
      print("IT'S A DRAW")
      print("-----------------------------------")
      print("USER: %d" % (user))
      print("COMPUTER: %d" % (comp))
  #---------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
  

print(stone_paper_scissor())
print(input("PRESS ENTER TO CLOSE:"))