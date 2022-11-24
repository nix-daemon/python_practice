cubes = []
pre_cubes = list(range(1, 11))
for cube in pre_cubes:
	cubes.append(cube ** 3)
print(cubes)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)