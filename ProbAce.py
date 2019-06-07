s = 0
tries = 0
for prob in range(1,53):
    if prob < 17:
        s += 1
    tries += 1
print(float(s)/tries)