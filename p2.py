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
    _2nd_mark = marks[1]
    def getName(arr):
        if float(arr[1]) == _2nd_mark:
            return arr[0]
    res = list(filter(getName, finallist))
    
    res.sort() 
    for i in res:
        print(i[0])

except Exception as e:
     print('err', e)

