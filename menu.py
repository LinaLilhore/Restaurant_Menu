menu={
    'Pizza':60,
    'Pasta':50,
    'Burger':80,
    'Coffee':35,
    'Salad':50,
}
print("Welcome to PYTHON Restaurant")
print(" Pizza: RS 60 \n Pasta: RS 50 \n Burger: Rs 80 \n Coffee: RS 35 \n Salad: RS 50")
oredr_total=0
n=1
while(n==1):
    item=input("Enter the name of item you want to order =")
    if item in menu:
        oredr_total+=menu[item]
    else:
        print(f"Ordered item {item} is not avaialable yet!") 
    item=input("Do you want to add another item ? (yes/no) ")    
    if item=='yes':  
       n==1 
    else:
        break
print("Your total oder amount is: ",oredr_total)            
