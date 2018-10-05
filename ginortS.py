a = raw_input()
LWC = []
UPC = []
EVD = []
ODD = []
String = ''
for i in range(len(a)):
    if a[i] in 'abcdefghijklmnopqrstuvwxyz':
        LWC.append(a[i])
    elif a[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        UPC.append(a[i])
    elif a[i] in '13579':
        ODD.append(a[i])
    elif a[i] in '24680':
        EVD.append(a[i])
LWC = sorted(LWC)
UPC = sorted(UPC)
EVD = sorted(EVD)
ODD = sorted(ODD)
for i in range(len(LWC)):
    String = String + LWC[i]
for i in range(len(UPC)):
    String = String + UPC[i]
for i in range(len(ODD)):
    String = String + ODD[i]
for i in range(len(EVD)):
    String = String + EVD[i]
print String          
