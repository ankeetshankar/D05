#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    print("Please enter a non-word numeral only")
    z = input("")
    #Trying to keep the try block to a minimal after the last homework. 
    try:
    	z = int (z)
    except:
    	print("\n Please enter only non word integer values")
    	print("Program will quit now. Thanks !!")
    	return None
    if z % 2 ==0:
    	print("The input number is even ")
    else:
    	print("The input was odd")
    return None

   


def ten_by_ten():

	""" Prints integers 1 through 100 sequentially in a ten by ten grid."""
    #In this function counter is the main varibale which will be increamented and printed. 
	#This will be used in conjunction with the for loop to keep track when to do a new line print.
	counter = 1
	line_counter = 0
	
	for x in range(1,101):
		print(counter, "", end="")
		counter = counter + 1
		line_counter = line_counter +1

		if line_counter == 10:
			print ("\n")
			line_counter = 0
			continue
		continue


    


def find_average():
    user_input = 0
    counter =0
    average = 0
    
    while user_input!= "done":
        user_input = input("Please enter non word numeral for the average calculator")
        counter = counter + 1
        if counter==1 and user_input =="done":
            print ("The average of the entered numbers is Zero ")
            return average
        elif counter==1 and user_input !="done":
            average = float(user_input)
            continue
        elif counter > 1 and user_input !="done":
            average = ((average + float(user_input))/2)
            continue
        elif counter > 1 and user_input =="done":
            return average
                   
     
        return average


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    print ("even_odd")
    even_odd()
    print("Ten by 10")
    ten_by_ten()
    print ("find_average")

if __name__ == '__main__':
    main()
