def freqMap(values):
    map = {}
    for v in values:
        if not map.get(v):
            map[v] = 1
        else:
            map[v] += 1
    return map


def mode_func(values):
    map = freqMap(values)
    if map.values(): # if the dictionary is non-empty
        maximumValue = max(map.values())
        mode = [(key, value) for key, value in map.items() if value == maximumValue]
        return mode
    return []


x = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 6]
y = [1]
z = []

print(freqMap(x))
print(mode_func(x))

print(freqMap(y))
print(mode_func(y))

print(freqMap(z))
print(mode_func(z))
