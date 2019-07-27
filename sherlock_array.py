#!/usr/bin/py
def arraySherlock(a):   
    
    left_idx = 0
    right_idx = len(a) - 1
     
    left_sum = a[left_idx]
    right_sum = a[right_idx]
     
    while left_idx != right_idx:
        if left_sum < right_sum:
            left_idx += 1
            left_sum += a[left_idx]
        else:
            right_idx -= 1
            right_sum += a[right_idx]
     
    return left_sum == right_sum
     
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        if arraySherlock(a):
            print ("YES")
        else:
            print ("NO")