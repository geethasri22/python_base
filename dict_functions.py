'''
Data = {1:"Raju", 2:"Ramu", 3:False}
'''

Data = {}

n = int(input('Enter total entires in Data : '))
for i in range(n):
    print(f"\n\nEnter pair - {i},\n ")
    key = input('Enter Key = ')
    value = input('Enter Value = ')
    Data[key] = value
    
print(f"Type : {type(Data)} ")

print(f"My Data : {Data} ")

x = input("\nEnter key to Update = ")
if x in Data:
    newVal = input("Enter new Val = ")
    Data[x] = newVal
else:
    print("\nKey not found")
    

print(f"My updated {x} Data : {Data} ")

Data['None'] = "Sameer"
Data[90] = "Wilson"
Data[2] = "Raju"

print(f"My updated Data : {Data} ")

#output:
Enter total entires in Data : 2


Enter pair - 0,
 
Enter Key = 1
Enter Value = lahari


Enter pair - 1,
 
Enter Key = 2
Enter Value = sneha
Type : <class 'dict'> 
My Data : {'1': 'lahari', '2': 'sneha'} 

Enter key to Update = 2
Enter new Val = neha
My updated 2 Data : {'1': 'lahari', '2': 'neha'} 
My updated Data : {'1': 'lahari', '2': 'neha', 'None': 'Sameer', 90: 'Wilson', 2: 'Raju'} 

