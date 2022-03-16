# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#VERTICAL HISTOGRAM :-https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops

# Student ID: 2019218         
  
# Date: 2020/12/1


progress=0
trailer=0
retriever=0
excluded=0
#Variables defined
print('-'*60)
print("Staff Version with Horizontal & Vertical Histogram ")

def User_Input():  #This function is to request inputs and find progression level
    ranges=[0,20,40,60,80,100,120]  #Defining list to restrict input range
    global modules_passed  #defined as global variable to allow the variable be used out of the function
    global modules_deferred
    global modules_failed
    global progress
    global trailer
    global retriever
    global excluded
    modules_passed=0
    modules_deferred=0
    modules_failed=0
    #Variables defined
    while (True and ( modules_passed, modules_deferred, modules_failed not in ranges)): #Using while loop to repeat until user input
        try:
            modules_passed=int(input("\nEnter your total PASS credits: "))
            if(modules_passed not in ranges):#Conditional statemetn to check if each input is within the range
                print("Out of range")
                continue
            else:
                pass
                
            modules_deferred=int(input("Enter your total DEFER credits: "))
            if(modules_deferred not in ranges):#Conditional statemetn to check if each input is within the range
                print("Out of range")
                continue
            else:
                pass
                
            modules_failed=int(input("Enter your total FAIL credits: "))
            if(modules_failed not in ranges):#Conditional statemetn to check if each input is within the range
                print("Out of range")
                continue
            else:
                pass
            total=modules_passed+modules_deferred+modules_failed
           
            
        except ValueError:  #If user input is not an integer
            print("Integer required")
            print("")
            continue
        
        
        if(total!=120):  #Conditional statement to check if total entered exceeds limit
            print("Total incorrect")
            print("")
        else:
            pass
            break   #to break out and continue to the line of code
         

    if(modules_passed==120):  #Conditional statements to check which progression outcome
        print("Progress")
        progress=progress+1  #Total calculated to print hisogram accurately
    elif(modules_passed==100):
        print("Progress (module trailer)")
        trailer=trailer+1
    elif(modules_failed>=80):
        print("Exclude")
        excluded=excluded+1
    else:
        print("Do not progress – module retriever")
        retriever=retriever+1

        
    return()


def menu():  #This function is to request user if he wants enter more detailss to end program
    count=1
    global progress  #defined as global variable to allow the variable be used out of the function
    global trailer
    global retriever
    global excluded
    response=("")
    while True:  #to loop and request if user wants to enter more details
        print("")
        print("\nWould you like to enter another set of data?")
        response=input("\nEnter 'y' for yes or 'q' to quit and view results: ")
        if(response.lower()=="yes" or response.lower()=="y"):  #allowing multiple inputs
            count=count+1
            User_Input()   
        elif(response.lower()=="quit" or response.lower()=="q"): #allowing multiple inputs
            print("-"*60)
            print("Horizontal Histogram")
            print("Progress",progress,'    :','*'*progress)  #printing the horizontal histogram
            print("Trailer",trailer,'     :','*'*trailer)
            print("Retriever",retriever,'   :','*'*retriever)
            print("Excluded",excluded,'    :','*'*excluded)
            print("")
            print(count,"outcomes in total")  #Total outomes printed
            print("-"*60)
            break  #to break out of the loop
        else:
            print("")

def vertical():  #This function to print the vertical histogram
    global progress #defined as global variable to allow the variable be used out of the function
    global trailer
    global retriever
    global excluded
    print("Vertical Histogram")
    print('Progress', "Trailer", "Retriever", "Excluded")  #Headers printed for the vertical histogram
    for x in range(max(progress, trailer, retriever, excluded)):
        print("   {0}        {1}        {2}        {3}".format(  #Format condition to format the specified value and insert asterik or space in placeholder 
        '*' if x < progress else ' ',
        '*' if x < trailer else ' ',      #if statement used to decide if either a asterik should be printed or a space should be printed
        '*' if x < retriever else ' ',
        '*' if x < excluded else ' '))
    print("-"*60)
    
    
    
User_Input() #executing the User_input function 
menu()  #executing the menu function 
vertical()  #executing the vertical function 
