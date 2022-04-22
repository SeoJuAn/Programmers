def solution(operations):
    answer = []
    list= []
    for i in operations:
        if i[0]=="I":
            list.append(int(i[2:]))
        elif len(list)!=0:
            if i[2]=="1":
                list.remove(max(list))
            else:
                list.remove(min(list))

    if len(list) == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(list))
        answer.append(min(list))


    return answer

operations = ["D 1"]
print(solution(operations))