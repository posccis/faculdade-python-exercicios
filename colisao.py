Xa0, Ya0, Xa1, Ya1 = input().split()
Xb0, Yb0, Xb1, Yb1 = input().split()

if Xb0 > Xa1 or Xb1 < Xa0:
    print("0")
elif Yb0 > Ya1 or Yb1 < Ya0:
    print("0")
else: 
    print("1")