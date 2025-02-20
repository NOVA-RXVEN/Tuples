print("\033c")
print("\033[3m")
print("\033[1m")
print("Multiplication of Tuple\n")

tup1 = (3, 6, 7, 8, -3, 22, 9, 10, 32, 11, 12, 17, 34, 21, 32)
tup2 = (7, 22, 3, 6, 10, 7, 9, 18, 39, 90, 21, 4, 35, 32, 21)
tup3 = (6, 42, 32, 14, 50, 12, 21, 65, 29, 40, 2, 4, 51, 23, 8,)

tup = ()

for i in range(0,15):
    a = tup1[i] * tup2[i] * tup3[i]
    tup = tup + (a,)
    
print(f"The Multiplication 3 Tuples: {tup}")