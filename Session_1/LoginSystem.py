print("                        welcome                          ")

user={
    "Ahmed" : 1394,
    "Ali" : 6078,
    "Amr" : 9345
}

name=input("username : ")
Pass=int(input("password : "))



if name in user and user[name] == Pass:
    print("Login successfully !")
else:
    print("Failed !")
