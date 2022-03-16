# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019218         
  
# Date: 2020/12/1


def User_Input(): #This function is to request inputs and find progression level
    ranges=[0,20,40,60,80,100,120] #Defining list to restrict input range
    modules_passed=0
    modules_deferred=0
    modules_failed=0
    #Variables defined
    print('-'*60)
    while (True and ( modules_passed, modules_deferred, modules_failed not in ranges)): #Using while loop to repeat until user input is valid
        try:
            modules_passed=int(input("Please enter your credits at pass: "))
            if(modules_passed not in ranges):  #Conditional statemetn to check if each input is within the range
                print("Out of range")
                print("")
                continue
            else:
                pass
                
            modules_deferred=int(input("Please enter your credits at defer: "))
            if(modules_deferred not in ranges): #Conditional statemetn to check if each input is within the range
                print("Out of range")
                print("")
                continue
            else:
                pass
                
            modules_failed=int(input("Please enter your credits at fail: "))
            if(modules_failed not in ranges):  #Conditional statemetn to check if each input is within the range
                print("Out of range")
                print("")
                continue
            else:
                pass
            total=modules_passed+modules_deferred+modules_failed
        except ValueError:   #If user input is not an integer 
            print("Integer required")
            print("")
            continue
        
        if(total!=120): #Conditional statement to check if total entered exceeds limit
            print("Total incorrect.")
            print("")
        else:
            pass
            break #to break out of loop
    if(modules_passed==120):     #Conditional statements to check which progression outcome
        print("Progress")
    elif(modules_passed==100):
        print("Progress (module trailer)")
    elif(modules_failed>=80):
        print("Exclude")
    else:
        print("Do not progress – module retriever")
   
    print('-'*60)
        
    return()
       
    
User_Input() #Calling the function for it to execute
