def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people)-1

    count = 0
    while True:
        if people[start] + people[end] <= limit:
            start+=1
            end-=1
            count += 1
        else:
            end-=1
            count += 1
        if(start>end):
            break
    answer = count


    return answer

#50, 50, 70, 80
people = [70,80,50]
limit = 100

print(solution(people,limit))