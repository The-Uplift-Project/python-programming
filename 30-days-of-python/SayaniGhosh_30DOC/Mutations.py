def mutate_string(string, position, character):
    c=0
    s=""
    for i in string:
        if(c==position):
            s=s+character
        else:
            s=s+i
        c+=1
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)