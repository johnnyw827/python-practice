# John Williams
# CSCI 236
# 23 Jan 2021
# Program 00 - Warmup
# approximate number of hours you invested
# description of any major problems you ran into
# status of the program - does it compile, does it run perfectly, does it have bugs, any limitations, etc


#Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
def is_curzon(number):                          
    if ((2 ** number + 1) % (2 * number + 1) == 0):
        return True
    else:
        return False       


sum = 0
number = 23
#Make sure the integer is positive   
if number < 0:                                            
    print("Input not Valid") 
else: #If it is then output the sum of the Curzon numbers that exist between 0 and the number
    for number in range(0, number):
        if is_curzon(number) == True:
            sum += number #or number if you wanted the curzon numbers added together?
    print(sum)

 
   
    



    
    








