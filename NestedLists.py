NS = []
S = []
Names = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    NS.append([name,score])
for i in range(len(NS)):
    x = NS[i][1]
    S.append(x)
sortedS = sorted(list(set(S)))
SecondHighest = sortedS[1]
count = S.count(SecondHighest)
for i in range(count):
    Names.append(NS[S.index(SecondHighest)][0])
    S[S.index(SecondHighest)] = 0
Names = sorted(Names)
for i in range(len(Names)):
    print Names[i]
    
