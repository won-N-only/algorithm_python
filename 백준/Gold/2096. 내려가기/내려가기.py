import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


n = int(input())  
max_dp = [0] * 3  
min_dp = [0] * 3  

first_row = list(map(int, input().split()))
max_dp = first_row[:]  
min_dp = first_row[:]  

for _ in range(1, n):
    a, b, c = map(int, input().split())
    
    new_max_dp = [
        max(max_dp[0], max_dp[1]) + a, 
        max(max_dp[0], max_dp[1], max_dp[2]) + b,  
        max(max_dp[1], max_dp[2]) + c 
    ]
    
    new_min_dp = [
        min(min_dp[0], min_dp[1]) + a,  
        min(min_dp[0], min_dp[1], min_dp[2]) + b,  
        min(min_dp[1], min_dp[2]) + c  
    ]
    
    max_dp = new_max_dp
    min_dp = new_min_dp

print(max(max_dp), min(min_dp))
