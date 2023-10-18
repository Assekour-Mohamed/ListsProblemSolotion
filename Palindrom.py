s = input("enter the string:")
Flag = True
for i in range(len(s)):
    if s[i] != s[len(s) -1 -i]:
        Flag = False
        break
if Flag :
    print("it is palindrom")
else :
    print("it is not a pailandrom")
