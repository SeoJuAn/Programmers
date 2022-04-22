def solution(priorities, location):
    answer = 0
    index = []

    for i in range(len(priorities)):
        index.append(i)

    i = 0
    while True:
        if(priorities[0]>=max(priorities)):
            priorities.pop(0)
            i = i+1
        else:
            priorities.append(priorities.pop(0))
            index.append(index.pop(i))

        if len(priorities)==0:
            break


    answer = index.index(location)+1

    return answer

priorities = [2,1,3,2]
location = 2
print(solution(priorities,location))