def arithmetic_progression():     # a = first term | d = common difference | l = last term
   a = int(input("first term:"))  # for the first term(start)
   l = int(input("last term:"))   # for the last term(stop)
   d = int(input("common difference:")) # for the common difference(step)
   range_list = [num for num in (range(a, l + 1, d))] # for the A.P(Range)
   n = len(range_list) # for the number of terms in the A.P
   sum = 0
   for num in range(a , l+1 , d): # for finding the sum of n number of terms of the A.P
       sum += num # iterating through every number of the A.P
   print('Sum of %d terms : %d' %(n, sum)) # Output by the interpreter (required sum)
   print(range_list) # A.P

print(arithmetic_progression())

print(input('Press any key to exit:')) # to prevent the script from closing immediately after the program is executed
