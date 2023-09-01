

GPIO_reg=8
ls=[]
ls2=[]
for count in range(GPIO_reg):
    In=str(input(f"please enter bit {count} mode ' in or out '  : "))
    if In in['in','out']:
         ls.insert(count,In)
    # else :
    #     count -=1
    #     print("Error , Try again !")

for i, value in enumerate(ls):
    if value == 'in':
        ls2.insert(i, 0)
    elif value == 'out':
        ls2.insert(i, 1)

# print(ls)

# print(ls2)
binary_string = ''.join(str(bit) for bit in ls2)
print(binary_string)

f=open("text.txt","w")
f.write("void Init_PORTA_DIR (void)\n{\n")
f.write(f"   DDRA=0b{binary_string};")
f.write("\n}")

