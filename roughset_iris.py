import itertools
from itertools import combinations, chain
import csv


    
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def subsets(s):
    return list(powerset(s))



def POS(my_set,next_set,l):
    value=[]
    for now in my_set:
        for next_now in next_set:
            if tuple(now) in set(itertools.combinations(next_now,len(now))):
                value.extend(now)
    value=list(set(value))
    #print("POS VALue",value)
    return(len(value)/l)       

def SUB(set1,set2,fin):
    value=[]
    jk=[]
    for now in set1:
        for next_now in set2:
            temporary=[]
            for sub1 in subsets(now):
                for sub2 in subsets(next_now):
                    if sub1==sub2:
                        temporary.append(sub1)
            temporary.sort(key=lambda x:len(x))
            value.append(temporary[-1])
            jk.extend(temporary[-1])
    for now in set2:
        for next_now in set1:
            temporary=[]
            for sub1 in subsets(now):
                for sub2 in subsets(next_now):
                    if sub1==sub2:
                        temporary.append(sub1)
            temporary.sort(key=lambda x:len(x))
            #print(temporary[-1])
            value.append(temporary[-1])
            jk.extend(temporary[-1])
    jk=list(set(jk))
    
    
    for i in fin:
        if i not in jk:
            value.append([i])

    value=list(filter(None,value))
    fin1=list(set(value))
    return list(map(list,fin1))




with open('C:\\Users\\Aswin Nagarajan\\Desktop\\kdd.csv', 'r') as f:
    reader = csv.reader(f)
    data_as_list = list(reader)

dataset_new=list(map(list, zip(*data_as_list)))
print(dataset_new)
dataset=dataset_new[:len(dataset_new)-1]
print(dataset)
red_final_set=list(range(1,len(dataset)+1))
final_set=list(range(1,len(dataset[0])))
#final_set=[1,2,3,4,5,6,7]
#red_final_set=[1,2,3,4]
#dataset=[[1,1,1,1,2,2,2],[0,0,2,2,1,1,1],[2,2,0,2,0,1,2],[1,0,0,1,0,0,1]]
final=[]
number=len(red_final_set)
for i in dataset:
    visited=[]
    for j in i:
        if j not in visited:
            visited.append(j)
    mat=[]
    for k in visited:
        temp=[]
        for j in range(len(i)):
            if i[j]==k :
                temp.append(j+1)
        mat.append(temp)

    final.append(mat)

#print("Final",final)
seq=[]
start=final
count=0
for count in range(len(red_final_set)-1):
    #print("Start is",start)
    value_final=[]
    for my_set in start:
        temp=[]
        for next_set in final:
            if my_set==next_set:
                temp.append(1)
                continue
            else:
                value=POS(my_set,next_set,len(final_set))
                temp.append(value)
            
        value_final.append(temp)
       
    #print(value_final)
    t=[]
    for j in range(len(value_final)):
        s=0
        for jk in value_final[j]:
            s= s+jk
        t.append((j,s))
    t.sort(key=lambda x: x[1])
    #print(t[-1])
    
    #print("Reduced",red_final_set)
    for i in t:
        if i[1]==t[-1][1]:
            opt=i[0]
            seq.append(red_final_set[opt])
            red_final_set.remove(red_final_set[opt])
            opt_value=t[len(t)-1][1]
            break
    if (t[-1][1]>=number):
        print("Reduct found at iteration: ",count+1)
        print(seq.sort())
        print(t[-1][1]/number)
        #break
    #print(opt)       
    #print("Reduced After",red_final_set)
    new_temp=start
    start=[]
    print("Sequence:",seq)
    #print("New Temp:",new_temp)
    for my_set in range(len(new_temp)):
        if my_set!=opt:
            tr=SUB(new_temp[my_set],new_temp[opt],final_set)
            start.append(tr)
            #print("Doing",tr) 
     
    

        
    

        
