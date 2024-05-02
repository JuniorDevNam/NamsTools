#barrel{BlockEntityTag:{Items:[{Slot:0,id:filled_map,Count:1,tag:{map:57}},{Slot:1,id:filled_map,Count:1,tag:{map:58}}]}}

def run(fr, to):
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
x = int(input("from: "))
run(x,x+27)