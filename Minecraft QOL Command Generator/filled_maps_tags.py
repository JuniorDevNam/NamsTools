#barrel{BlockEntityTag:{Items:[{Slot:0,id:filled_map,Count:1,tag:{map:57}},{Slot:1,id:filled_map,Count:1,tag:{map:58}}]}}

def run_1_20_4_to_below(fr, to):
    o = "{"
    t = "}"
    c = 0
    r = ""
    i = 'barrel{BlockEntityTag:{Items:['
    m = f']{t}{t}'
    end = to - 1
    for x in range(fr,to):
        b = f'{o}Slot:{c},id:filled_map,Count:1,tag:{o}map:{x}{t}{t}'
        if x < end:
            r = r + b + ','
        else:
            r = r + b
        c += 1
    print(i+r+m)
    print("__________________________")
x = int(input("from: "))
y = int(input("to: "))
old = input("Old Command Format? (1.20.4 and below) (y/n): ")
print("__________________________")
z = y - x
a = 0
if z > 27:
    count = 1
    while z > 27:
        count += 1
        z -= 27
    for _ in range(count):
        a += 27
        if a < y:
            run_1_20_4_to_below(x,x+27)
        else:
            run_1_20_4_to_below(x+27,y)
elif z == 27:
    if old == "y":
        run_1_20_4_to_below(x,x+z)
else:
    if old == "y":
        run_1_20_4_to_below(x,y)