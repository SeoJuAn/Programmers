def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x:x[2])
    #print(costs)

    bridge = set([costs[0][0]])
    while len(bridge)!=n:
        for cost in costs:
            #정점이 두개다 포함돼 있으면 패스
            if cost[0] in bridge and cost[1] in bridge:
                continue
            #정점 중 둘 중 하나는 포함돼 있으면 추가
            elif cost[0] in bridge or cost[1] in bridge:
                bridge.add(cost[0])
                bridge.add(cost[1])
                answer += cost[2]
                break


    return answer


n = 5
costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
print(solution(n,costs))