def c(a):
    count=1
    string=''
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            count += 1
        else:
            string += a[i-1] + str(count)
            count = 1
    string += a[-1]+str(count)
    return string
a=input()
print(c(a))
