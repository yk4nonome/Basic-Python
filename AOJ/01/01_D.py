S=input()
S=int(S)
h=S//3600
M=S%3600
m=M//60
s=S-h*3600-m*60
print(f'{h}:{m}:{s}')
