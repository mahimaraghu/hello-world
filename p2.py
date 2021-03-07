finallist = []
marks = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    finallist.append([name, score])
    marks.append(score)

marks = list(set(marks))
marks.sort()

try:
    second_min = marks[1]
    def getName(arr):
        if float(arr[1]) == second_min:
            return arr[0]
    res = list(filter(getName, finallist))
    
    res.sort() 
    for i in res:
        print(i[0])

except Exception as e:
     print('err', e)

