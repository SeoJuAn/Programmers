import heapq

def solution(jobs):
    answer = 0
    first = heapq.heappop(jobs)
    time = first[0]+first[1]

    jobs.sort()
    i=0
    while i<len(jobs):
        usetimeHeap = []
        for j in range(len(jobs)):
            if time>jobs[j][0] and time<jobs[j][0]+jobs[j][1]:
                heapq.heappush(usetimeHeap,[jobs[j][1],jobs[j][0]])

        if len(usetimeHeap)!=0:
            time = time + heapq.heappop(usetimeHeap)[0]
            i = i+1
        else:
            time = time+1


    print(time)
    return answer


jobs = [[0,3],[1,9],[2,6]]
solution(jobs)