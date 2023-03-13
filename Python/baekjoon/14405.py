import re
def solution():
    if re.compile("(pi|ka|chu)+").match(str(input())):
        print("YES")
    else:
        print("NO")

def sol2():
    try:
        if not int(str(input()).replace("pi",'0').replace("ka",'0').replace('chu','0')):
            print("YES")
    except:
        print("NO")
sol2()
solution()