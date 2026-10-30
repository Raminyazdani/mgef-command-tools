import os
all_data = []
for file in os.listdir():
    try:
        if not file.endswith(".txt"):
            continue
        with open(file, 'r') as f:
            data = f.readlines()
            for line in data:
                if line.strip().startswith('MGEF'):
                    all_data.append(line.strip())
    except:
        pass
set_mgef = set()
for line in all_data:
    s= line.split("(")[1].split(")")[0]
    set_mgef.add(s)
print(set_mgef)

from itertools import combinations


# singles + doubles
result = list(combinations(set_mgef, 1)) + list(combinations(set_mgef, 2))

for r in result:
    string = "playerenchantobject 0006B46B "
    for s in r:
        string += f"{s} "
    print(string.strip())
with open("ench_robe.txt", 'w') as f:
    for r in result:
        string = "playerenchantobject 0006B46B "
        for s in r:
            string += f"{s} "
        f.write(string.strip() + "\n")