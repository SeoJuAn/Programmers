def solution(money):
    answer = 0

    sum_not_first = [0]*len(money)
    sum_yes_first = [0]*len(money)

    #첫번째 집 무조건 털기 - 마지막 집은 못 텀
    sum_yes_first[0]= money[0]
    for i in range(1,len(money)-1):
        sum_yes_first[i] = max(sum_yes_first[i-1],money[i]+sum_yes_first[i-2])

    sum_not_first[0] = 0
    for i in range(1,len(money)):
        sum_not_first[i] = max(sum_not_first[i-1],money[i]+sum_not_first[i-2])

    answer = max(sum_yes_first[len(sum_yes_first)-2],sum_not_first[len(sum_not_first)-1])
    return answer


money = [1,2,3,4,5,6]
print(solution(money))