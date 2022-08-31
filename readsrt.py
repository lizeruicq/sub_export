

result = []

filename = "文本.txt"
f = open(filename,'r',encoding='utf-8')
lines = f.readlines()
for i in range(2,len(lines),4):
    print(lines[i],end="")

input("结束")



