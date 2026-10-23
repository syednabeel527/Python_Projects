vehicle = (input("Enter vehicle type "))
distance = int(input("Enter distance travelled (kn) "))
base_price = 0
if vehicle == "bike":
    base_price = 5
elif vehicle == "car":
    base_price = 10
elif vehicle == "truck":
    base_price =20
else :
    print("Invalid vehicle type")

if distance > 100 :
    final_price = base_price * 0.90
    print("You have travelled more than 100 km so you get 10% discount")
else :
    final_price = base_price 
    print("You distance is 100 km or less so no discount.")

for i in range(1,4):
    print("processing item",i,"....")

print("Final tool fee: $", final_price)