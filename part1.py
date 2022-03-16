# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019218         
  
# Date: 2020/12/1


def User_Input(): #This function is to request inputs and find progression level
    print("-"*50)
    modules_passed=int(input("Please enter your credits at pass: "))
    modules_deferred=int(input("Please enter your credits at defer: "))
    modules_failed=int(input("Please enter your credits at fail: "))
    #variables requesting credit input

    if(modules_passed==120):
        print("Progress")
    elif(modules_passed==100):
        print("Progress (module trailer)")
    elif(modules_failed>=80):
        print("Exclude")
    else:
        print("Do not progress – module retriever")
    #Conditional statements to check which progression outcome
    print("-"*50)
        
    return()
       
    
User_Input() #Calling the function for it to execute

