def valid_number(m):
    if m.startswith('+'):
        p = m.split(' ')
        if len(p) == 2 and p[0][1:].isdigit() and (len(p[0][1:]) == 2):
            c_code = p[0]
            number = p[1]
            if (len(number) == 10 and number.isdigit()) :
                d_sum = sum(int(d) for d in number)
                if d_sum > 0 :
                    return "Correct"
    elif (len(m) == 10 and m.isdigit()) :
        d_sum = sum(int(d) for d in m)
        if d_sum > 0 :
            return "Correct"
    return "Incorrect"

m = input().strip()
print(valid_number(m))
                
