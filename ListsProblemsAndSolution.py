### all perfect numbers less then a number
n = int(input("enter a number:"))
flag=True
PerfectNumbersList = []
print("the perfect numbers less than ",n,"are:")
for i in range(3,n):
    for j in range(2,i):
        if  i%j ==0:
            flag=False
            break
    if flag ==True:
        PerfectNumbersList.append(i)
    else:
        flag = True
print(PerfectNumbersList)

###################################
### All dividor of a number

n = int(input("enter anumber l"))
DevidorList= []
for i in range(1,n):
    if n % i == 0 :
        DevidorList.append(i)

print("ther are ",len(DevidorList),"devidor of number ",n,DevidorList)

###############################
### Number friends

n = int(input("enter anumber l"))
m = int(input("enter anumber l"))

sumDivsOfn= 0
sumDivsOfm=0
for i in range(1,max(n,m)):
    if n % i == 0 :
        sumDivsOfn = sumDivsOfn +1
    if m % i == 0 :
        sumDivsOfm = sumDivsOfm + i        
if sumDivsOfn == m and sumDivsOfm == n :
    print(m ,"and",n,"are friends")

#################################
### Password check
Password = input("enter the password : ")

for i in range (4):
    if(i <3):
        if Password != "DEV102":
            print("Not valid..")
            Password = input("enter the password : ")
    else :
        SecretQuestion= input("What is your favorit movie?")

###################################
### sum of tow lists 
N = input("enter the length of the list::")
T1 =[]
T2 = []
sum =[]
for i in range(N):
    T1.append(int(input("enter the ",i,"element of the first list:")))
    T1.append(int(input("enter the ",i,"element of the second list:")))
    sum.append(T1[i]+T2[i])
print(sum)

###################################
### notes greater then average
Notes = []
sumOfNotes = 0
for i in range(20):
    Notes.append(int(input("enter the ",i,"Note : ")))
    sumOfNotes = sumOfNotes + Notes[i]
avg = sumOfNotes / 20
for i in range(20) :
    if sumOfNotes[i]> avg:
        print(sumOfNotes[i])

