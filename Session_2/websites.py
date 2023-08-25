
import firelink
import webbrowser 

def firefox(url):
    webbrowser.open(url)


ls=['https://ar-ar.facebook.com/','https://www.youtube.com/','https://www.w3schools.com/python/python_functions.asp']
print("1. facebook \n 2. youtube \n 3. w3school ")
choice=int(input("enter your choice : "))

if choice==1:
    firefox(ls[0])
elif choice==2:
    firefox(ls[1])
elif choice==3:
    firefox(ls[2])
else:
    print("try again !")