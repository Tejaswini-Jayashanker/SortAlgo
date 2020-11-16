''' This is an approach to solve :
Write a function selection_sort(mylist) that takes a list of numbers and sorts it using the selection
sort algorithm. You can read about the selection sort algorithm online - here is one resource
(https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/). Its basic idea is to find
the minimum and put it at the front.
'''

def selection_sort(mylist):
    for i in range(len(mylist)): 
        minimum = i
        
        for j in range(i+1, len(mylist)): 
            if mylist[minimum] > mylist[j]: 
                minimum = j        
        
        mylist[i], mylist[minimum] = mylist[minimum], mylist[i]  #Swap
    
    print ("Sorted list is: ") 
    for i in range(len(mylist)): 
        print(mylist[i])

inp_list = []
int_list = []
inp_list = list(input("Enter the List"))
for i in inp_list:
    if( i == ' '):
        pass
    else:
        int_list.append(int(i))
print(int_list)
selection_sort(int_list)