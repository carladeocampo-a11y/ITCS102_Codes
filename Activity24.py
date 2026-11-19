fruits = ["Apple", "Mango", "Banana", "Santol", "Lansones"]

#Dictionary
#Key and Value

fruits_c = {"Red" : "Apple", "Moon" : "Mango", "Yellow" : "Banana", "Ulam" : "Santol", "Maliit" : "Lansones"}
print(fruits[0])
print(fruits_c["Red"])

for x,y in fruits_c.items():
    print("Key is ",x,"-- Value is ",y)