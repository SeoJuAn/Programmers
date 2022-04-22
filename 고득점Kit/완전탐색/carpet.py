import math

def solution(brown, yellow):
    answer = []

    aMb = brown + yellow
    aPb = (aMb + 4 - yellow)/2


    for i in range(int(math.ceil(aPb/2.0)),int(aPb)):

        if(i*(int(aPb)-i)==aMb):
            answer.append(i)
            answer.append(int(aPb)-i)
        

    return answer

brown = 8
yellow = 1
print(solution(brown,yellow))