import re
n = int(input().strip())
print(len(max(re.findall('(1*)',str(bin(n))[2:]))))