''' This is an approach to solve the following:
Write a function that takes a number k and a list of sorted numbers L, and returns True if k is in L or False
otherwise. You cannot use the membership operator. You have to search using the Binary Search
algorithm. Write two versions - first using recursion - binary_search_recurse(mylist,value) and
then using loops binary_search_loop(mylist,value) .

A binary search or half-interval search algorithm finds the position of a target value within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and executes in logarithmic time.
'''

def binary_search_loop(mylist, value):
    low = 0
    high = len(mylist) - 1
    flag_found_iter = False

    while(low <= high and not flag_found_iter):
        mid = (high + low)//2 #floor division. eg: 2.5 ==> 2 as we are using this for indices.
        if ( mylist[mid] == value ):
            flag_found_iter = True
        else:
            if( mylist[mid] > value):
                high = mid -1
            else:
                low = mid + 1
    return flag_found_iter

inp_list = []
int_list = []
inp_list = list(input("Enter the List"))
for i in inp_list:
    if( i == ' '):
        pass
    else:
        int_list.append(int(i))
int_list.sort()
print(int_list)


search_element = int(input("Enter the Element to search"))
print("Loops:",binary_search_loop(int_list, search_element) )

def binary_search_recurse(int_list, value, low, high):
    if( low <= high ):
        mid = (high + low)//2 #floor division. eg: 2.5 ==> 2 as we are using this for indices.
        if ( int_list[mid] == value ):
            return True
        else:
            if( int_list[mid] > value):
                return binary_search_recurse(int_list, value, low, mid -1)
            else:
                return binary_search_recurse(int_list, value, mid + 1, high)
    else:
        return False

low = 0 
high = len(int_list) - 1
inp_list = []
int_list = []
inp_list = list(input("Enter the List"))
for i in inp_list:
    if( i == ' '):
        pass
    else:
        int_list.append(int(i))
int_list.sort()
print(int_list)
search_element = int(input("Enter the Element to search"))
print("Recur:", binary_search_recurse(int_list,search_element,low,high) )