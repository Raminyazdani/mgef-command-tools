import os
all_data = []
for file in os.listdir():
    try:
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

maani = []

for line in all_data:
    if line.split("(")[1].split(")")[0] in set_mgef and line not in maani:
        maani.append(line)
with open("maani_add.txt", 'w') as f:
    for s in maani:
        f.write(s + "\n")

with open("mgef_add.txt", 'w') as f:
    for s in set_mgef:
        f.write(f"playerenchantobject 000139A3 {s}\n")
