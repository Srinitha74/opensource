def is_isomorphic_or_not(n,s,t):
    s_t={}
    t_s={}
    for i in range(n):
        char_s = s[i]
        char_t = t[i]
        if char_s in s_t:
            if s_t[char_s] != char_t :
                return "false"
        else:
            s_t[char_s] = char_t
        if char_t in t_s:
            if t_s[char_t] != char_s:
                return "false"
        else:
            t_s[char_t] = char_s 
    return "true"
n = int(input())
s = input()
t = input()
print(is_isomorphic_or_not(n,s,t))
