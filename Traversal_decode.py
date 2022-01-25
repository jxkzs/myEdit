import base64
import os

str = "QWIHBL GZZXJS XZNVBZW"
Dict = [["Q","q","9"],["W","w"],["I","i","1"],["H","h"],["B","b","6"],["L","l"],
        ["G","g","9"],["Z","z","2"],["Z","z","2"],["X","x"],["J","j"],["S","s","5"],
        ["X","x"],["Z","z","2"],["N","n"],["V","v"],["B","b","6"],["Z","z","2"],["W","w"]]

max_Dict = [3,2,3,2,3,2,
            3,3,3,2,2,3,
            2,3,2,2,3,3,2]
map_Dict = [1]*len(Dict)

max_count = 1
for k in max_Dict:
    max_count = max_count*k
print(max_count)

def strDict(map_D,D):
    s = ""
    for i,j in zip(range(len(D)),map_D):
        s = s + D[i][j-1]
    return s

f = open("result.txt","w")

def decideStr(String):
    key="~!@#$%^&*()_+-={}[]|\\:;\"\',./? \n\t\r\b\v"
    for i in list(String):
        if not (i.isalnum() or i in key):
            return False
    return True

if len(map_Dict) == len(map_Dict):
        count = 0
        while not (map_Dict == max_Dict):
            for i in range(len(map_Dict)):
                if map_Dict[i] == max_Dict[i]:
                    map_Dict[i] = 1
                elif map_Dict[i] < max_Dict[i]:
                    map_Dict[i] = map_Dict[i] + 1
                    break
                else:
                    print("ERROR OverFlow")
            s = strDict(map_Dict,Dict)
            d = base64.b64decode(s+"=")
            try:
                d_str = d.decode()
                if decideStr(d_str):
                    re = s+"=="+"\t\t\t"+d_str+"\n"
                    f.write(re)
            except:
                pass
            count += 1
            print(count,"---",max_count)
            if max_count < count:
                os.abort()
            #f.write(s+"\t"+d)


