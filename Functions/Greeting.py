# creating a function
def function(name=None):
    if name==None:
        print("Hi! I am a Murrad Bin Amir")
    elif name:
        print(f"Hello {name}")
    
    
# function 5
def concatinate(f_Name,m_Name=None,l_Name=None):
    if m_Name:
        return f_Name+" "+m_Name+" "+l_Name
    elif l_Name:
        return f_Name+" "+l_Name
    elif f_Name:
        return f_Name
               
     

# calling a function
function()

first_Name = input("what is your first name : ")
midle_Name = input("what is your midle name : ")
last_Name  = input("what is your last name  : ")
function(concatinate(first_Name,l_Name=last_Name,m_Name=midle_Name))

