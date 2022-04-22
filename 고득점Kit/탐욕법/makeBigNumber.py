import itertools


def solution(number, k):
    answer = ''

    index = []
    for i in range(len(number)):
        index.append(i)

    permutaions = list(itertools.permutations(index,k))

    zeroNumberList = []
    for i in permutaions:
        tmp = number
        for j in i:
            tmp = list(tmp)
            tmp[j] = '0'
            tmp = ''.join(tmp)
        zeroNumberList.append(tmp)

    intList = []
    for i in zeroNumberList:
        tmp = []
        for j in range(len(i)):
            if i[j]!='0':
                tmp.append(i[j])
        intList.append(int(''.join(tmp)))
    answer = str(max(intList))
    return answer


number = "4177252841"
k = 4
print(solution(number,k))