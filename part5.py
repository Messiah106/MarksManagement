# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019218         
  
# Date: 2020/12/1

alldetails=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]] #List of lists with all the given credits


def progression():   #This function is to print progression levels
    global p    #defined as global variable to allow the variable be used out of the function
    global t
    global r
    global e
    p=0
    t=0
    r=0
    e=0
    #Variables defined
    for i in range(10): #Loop to read the variable "alldetails" and print progression accurately
        if(alldetails[i][0]==120):
            print("Progress")
            p=p+1  #Total calculated to print hisogram accurately
        elif(alldetails[i][0]==100):
            print("Progress (module trailer)")
            t=t+1
        elif(alldetails[i][2]>=80):
            print("Exclude")
            e=e+1
        else:
            print("Do not progress – module retriever")
            r=r+1


def histogram(): #This function is to print the histogram 
    global p #defined as global variable to allow the variable be used out of the function
    global t
    global r
    global e
    total=p+t+r+e #Total caculated to print total number of outcomes
    print("\nProgress ",p,':',p*'*') #printing the horizontal histogram
    print("Trailing ",t,':',t*'*')
    print("Retriever",r,':',r*'*')
    print("Excluded ",e,':',e*'*')
    print("")
    print(total,"outcomes in total.") #Total outomes printed

progression() #executing the progression function
histogram() #executing the histogram function
