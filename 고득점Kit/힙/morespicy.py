import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    i = 0
    while True:
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        i=i+1
        if scoville[0]>=K:
            answer = i
            break
        if len(scoville)<= 1 and scoville[0]<K:
            answer = -1
            break

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))