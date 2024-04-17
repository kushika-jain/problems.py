def arrange(ilist):
    count1 = 0
    count2 = 0

    for i in ilist:
        if i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1  

    ar = []
    for i in range(0, count1):
        ar.append(1)
    for i in range(0, count2):  
        ar.append(2)
    return ar

T = int(input(""))

output = []

for _ in range(T):
    M = int(input("")) 
    ele12 = input("").split() 
    list12 = [int(x) for x in ele12] 

    sorted_list = arrange(list12)
    test_case_output = ' '.join(map(str, sorted_list[:M]))
    output.append(test_case_output)

for test_output in output:
    print(test_output)

