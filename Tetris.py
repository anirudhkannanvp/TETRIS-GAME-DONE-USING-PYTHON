import sys
from timeit import default_timer as timer
start=timer()
highscoretable=["NAME","MOVES","TIME"]
highscorearr=[["Anirudh","15","1"] for i in range(5)]
def printhigh():
        for i in range(5):
                for j in range(3):
                        print(highscorearr[i][j],sep="\t",end="\t")
                print()
print("Enter name to start")
name=str(input())
def updatehigh(score,timeu):
        for i in range(5):
                if(score>int(highscorearr[i][2])):
                        highscorearr[i][0]=name
                        highscorearr[i][1]=score
                        highscorearr[i][2]=timeu
                        break
#n=int(input())
#m=int(input())
n=10
m=6
values=[0]*17
for i in range(17):
    values[i]=i+1
couvalues=[0,0,0,0,0,0,0,0,0,2,1,7,1,1,1,1,7];
def print1(arr):
    for i in range(n-1,-1,-1):
        for j in range(m):
            if(arr[i][j]==-1):
                print(" ",end="\t",sep="\t")
            else:
                print(arr[i][j],end="\t",sep="\t")
            print(" | ",sep=" ",end=" ")
        print()
def func():
   i=0
   while(i<17):
        temp=i
        val=0
        for j in range(1,n):
            for k in range(m):
                if(arr[j][k]==i):
                    if(arr[j-1][k]==i or arr[j-1][k]==-1):
                        val+=1
        #print("val",val)
        if(couvalues[i-1]==val and val!=0):
            top=0
            for j in range(n):
                for k in range(m):
                    if(arr[j][k]==i):
                        top=max(top,j)   
                        arr[j-1][k]=i
            for u in range(m):
                if(arr[top][u]==i):
                    arr[top][u]=-1
            i=0
            continue
        i+=1           
arr=[[-1]*m for i in range(n)]
sum1=-1*n*m;
csum=0


arr[0][0]=17
arr[1][0]=17
arr[2][0]=17
arr[3][0]=17
arr[4][0]=17
arr[5][0]=17
arr[6][0]=17
arr[1][5]=16
arr[1][1]=15
arr[1][3]=14
arr[2][5]=13
arr[0][1]=12
arr[0][2]=12
arr[0][3]=12
arr[1][2]=12
arr[2][2]=12
arr[2][3]=12
arr[2][4]=12
arr[2][1]=11
arr[3][4]=10
arr[3][5]=10


for i in range(n):
    for j in range(m):
        csum+=arr[i][j]
moves=0
while(csum!=sum1):
    print1(arr)
    #print(arr)
    print("ENTER THE NUMBER TO BE REMOVED")
    te=int(input())
    if te not in values:
        print("WRONG INPUT !!! GIVE CORRECT INPUT")
        moves+=1
        continue
    for i in range(n):
        for j in range(m):
            if(arr[i][j]==te):
                arr[i][j]=-1
    func()
    couvalues[te-1]=0
    moves+=1
    csum=0
    for i in range(n):
        for j in range(m):
            csum+=arr[i][j]  
finaltime=timer()- start
print("----------------------------------")
print()
print("MOVES TAKEN BY YOU TO SOLVE ARE:-",moves)
print("----------------------------------")
print()
print("TIME TAKEN BY YOU ARE ",finaltime)
print("----------------------------------")
print()
print("GIVEN BELOW IS THE LEADERBOARD")
print("----------------------------------")
print()
print(*highscoretable)
updatehigh(moves,finaltime)
printhigh()
print("ENTER ANY KEY AND THEN ENTER TO EXIT")
op=str(input())
sys.exit()
