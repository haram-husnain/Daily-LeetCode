#0<(natural numbers)<10 that are /3 or /5
#{3,5,6,9} = 23 when added
# if negative = 0
# if divisible by both then count it once

def solution(number):
    
    mult_list=[]
    
    if (number > 0):
        num_list = list(range(1,number))
        print(f"all natural numbers below {number}: \n {num_list}")
        
        for item in num_list:
            if (item % 3 == 0 or item % 5 == 0):
                mult_list.append(item)
        
        print(mult_list)
        
        print(sum(mult_list))
        
    else: 
        print("0")
        return 0
  
solution(10)

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0.Note: If a number is a multiple of both 3 and 5, only count it once.