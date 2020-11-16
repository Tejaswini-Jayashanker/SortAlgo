''' This is a solution to the given problem statement:
Write a function merge_sort(mylist) that takes a list of numbers and sorts it using the merge sort
algorithm. Merge sort is a recursive algorithm. The crucial step is taking two recursively sorted subarrays
and "merge" them together by "interleaving" them. Read more about it online - here is one resource
(https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/)
'''

def mergeSort(mylist):
    if len(mylist) > 1:
        mid = len(mylist)//2 
        L = mylist[:mid] # Dividing the list elements 
        R = mylist[mid:] 

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        while ( i < len(L) and j < len(R) ):
            if L[i] < R[j]:
                mylist[k] = L[i]
                i+= 1
            else:
                mylist[k] = R[j]
                j+= 1
            k+= 1

        while ( i < len(L) ):
            mylist[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            mylist[k] = R[j]
            j+= 1
            k+= 1
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
mergeSort(int_list)