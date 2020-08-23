#Day 26 Code


#NESTED
#LOGIC

ret_day,ret_month,ret_year=[int(e) for e in input().strip().split(' ')]
due_day,due_month,due_year=[int(e) for e in input().strip().split(' ')]

#check year
if ret_year<due_year:
    print(0)
elif ret_year==due_year:
    #check month
    if ret_month<due_month:
        print(0)
    elif ret_month==due_month:
        #check day
        if ret_day<=due_day:
            print(0)
        else: 
            print(15*(ret_day-due_day))
    else:
        print(500*(ret_month-due_month))
else:
    print(10000)
