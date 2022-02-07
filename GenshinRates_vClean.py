from math import *
answer=""

def isnum(st):
    dig=["0","1","2","3","4","5","6","7","8","9"]
    if len(st)==0:
        return False
    for i in range(len(st)):
        c=0
        for ii in range(len(dig)):
            if st[i]==dig[ii]:
                c=1
        if c==0:
            return False
    return True
        

while answer!="y" and answer!="n":
    answer=input("Is your next 5* guaranteed to be the on-banner ? (y/n)     ")
input_pity=""
while True:
    input_pity=input("What pity are you currently on ? (counting last wish 5* as 0, give a number)      ")
    if isnum(input_pity)==True:
        if int(input_pity)<=89:
            break
input_wishes=""
while True:
    input_wishes=input("How many wishes are you using ? (give a number)    ")
    if isnum(input_wishes)==True:
        if int(input_wishes)>1:
            break

chances=1
pity=[]
rate=[]
got=[]
didntget=1

for i in range(90):
    pity.append(i)
    if i<=73:
        rate.append(0.006)
    elif i<=88:
        a=0.006+(i-73)*(0.994/16)
        rate.append(a)
    else:
        rate.append(1)

for i in range(len(rate)):
    a=rate[i]*didntget
    got.append(a)
    didntget-=a


if answer=="y":
    currentpity=int(input_pity)
    wishes=int(input_wishes)
    if currentpity+wishes>=90:
        print("At pity "+str(currentpity)+", the probability of pulling the desired 5* with "+str(wishes)+" wishes if you're on guaranteed are 100.0%")
    else:
        for i in range(wishes):
            chances=chances*(1-(rate[currentpity+i]))
        chances=100-100*chances
        chances=floor(100*chances)
        chances=chances/100
        print("At pity "+str(currentpity)+", the probability of pulling the desired 5* with "+str(wishes)+" wishes if you're on guaranteed should be : "+str(chances)+"%")




if answer=="n":
    starting_pity=int(input_pity)
    n_wishes=int(input_wishes)

    get_chances=0
    if n_wishes-2<90-starting_pity:
        pity1_i=n_wishes-2
    else:
        pity1_i=90-starting_pity

    equi=0
    for i in range(90-starting_pity):
        equi+=got[starting_pity+i]

    for pity1 in range(pity1_i):
        get_chances+=got[starting_pity+pity1]*0.5/equi
        if n_wishes-2-pity1<90:
            pity2_i=n_wishes-2-pity1
        else:
            pity2_i=90
        for pity2 in range(pity2_i):
            get_chances+=0.5*got[starting_pity+pity1]*got[pity2]/equi
    get_chances=floor(10000*get_chances)
    get_chances=get_chances/100
    print("At pity "+str(starting_pity)+", the probability of pulling the desired 5* with "+str(n_wishes)+" wishes if you're on 50/50 should be : "+str(get_chances)+"%")


exit=input("Press Enter to exit.")