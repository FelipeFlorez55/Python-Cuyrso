dict ={}

for i in range(1, 6):
    dict[i] = i**2
print(dict)

dict2= {i: i**2 for i in range(1, 6) if i % 2 == 0}
print(dict2)
name = ["Juan", "Luis", "Pedro"]
ages = [25, 30, 35]
dict3 = {name: ages for name, ages in zip(name, ages)}
print(dict3)