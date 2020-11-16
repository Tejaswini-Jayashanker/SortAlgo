''' This is an approach to solve :
Write a function bubble_sort(mylist) that takes a list of numbers and sorts it using the bubble sort
algorithm. You can read about the bubble sort algorithm online - here is one resource
(https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/tutorial/). Its basic idea is to keep
pushing large elements to the back in each inner loop iteration.
'''
def bubbleSort(mylist): 
    n = len(mylist) 
    for i in range(n-1):  
        for j in range(0, n-i-1): 
            if mylist[j] > mylist[j+1] : 
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
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
bubbleSort(int_list)