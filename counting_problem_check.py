#A 5-digit number is formed according to the rules:
#Rule 1: The number contains only the digits 1,2,3,4 and these digits may be repeated or unused.
#Rule 2: The first digit is 1 
#Rule 3: If D1D2 are consecutive digits and D1imageimageimageimage4 then D1 < D2
#Rule 4: If D1D2 are consecutive digits and D1=4 then D2=1
#How many of the 5 digit numbers of this type are there?  

#Generate a master list of all numbers from 11111 to 14444
master = []
for a in range(11111, 14445):
    master.append(a)
    
next1 = master

next2=[]
#Convert numbers into lists of integers
for b in next1:
    d = [int(c) for c in str(b)]
    next2.append(d)

next3 = []
#Remove every list that contains numbers outside of our assigned range(1 through 4)
for e in next2:
    if 0<e[1]<5 and 0<e[2]<5 and 0<e[3]<5 and 0<e[4]<5:
        next3.append(e)
#Generate final answer list
final_list=[]
#Iterate over each digit in each sublist to check against our rules
for m in next3:
    if m[1] > m[0] or (m[1] ==1 and m[0] == 4):
        if m[2] > m[1] or (m[2] ==1 and m[1] == 4):
            if m[3] > m[2] or (m[3] ==1 and m[2] == 4):
                if m[4] > m[3] or (m[4] ==1 and m[3] == 4):
                    final_list.append(m)
#Print Final List    
print('Final list of valid numbers:')
print(final_list)
print('Answer to problem:' + str(len(final_list)))
