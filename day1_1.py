text_file=open("inputday1_1.txt", "r")
lines = text_file.readlines()
floor = 0

for line in lines[0]:
    if line == "(": floor+=1
    elif line == ")": floor-=1

print floor