"""
Check out the resources on the page's right side to learn more about arrays. 
The video tutorial is by Gayle Laakmann McDowell, 
author of the best-selling interview book Cracking the Coding Interview.

Input:
n = the numbers of integers
k = the numbers of left rotations you must perfom
a = contains n space-separated integers describing the respective elements of the array's initial

Output:
Print the single line of n space-separeted integers denoting the final state of the array after
performing k left rotations


Challenge solving by @aisabellafontes

"""
def array_left_rotation_quickly(a,n,k):
    while  k > 0:
        a += [a.pop(0)]
        k -=1
    return a


def array_left_rotation(a, n, k):  
    while k > 0:
        for i, an in enumerate(a):
            if i < (n-1):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        k = k-1
    return a


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation_quickly(a, n, k);
print ' '.join(map(str,answer))

