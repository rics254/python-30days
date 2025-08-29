cubes = []
for value in range(1, 11):
    cube = value**3
    print(cube)
    cubes.append(cube)

print(cubes)

cubes = [number**3 for number in range(1, 11)]
print(cubes)

for cube in cubes:
    print(cube)
