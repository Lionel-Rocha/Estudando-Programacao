import math
import os
import random
import re
import sys

# Ao invés de calcular um por um, calcula uma vez e tira o maior/menor elemento para obter a soma mínima e a soma máxima
def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
