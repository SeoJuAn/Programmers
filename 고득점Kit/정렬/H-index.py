def solution(citations):
    answer = 0

    citations.sort(reverse = True)

    for i in range(len(citations)):
        if citations[i]<=i:
            answer = i
            return answer

    return len(citations)

#[6,5,3,1,0]
citations = [22,42]
print(solution(citations))