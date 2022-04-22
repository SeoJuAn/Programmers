def solution(m, n, puddles):
    answer = 0

    route = []

    for i in range(n+1):
        layer = []
        for j in range(m+1):
            layer.append(0)
        route.append(layer)
    route[0][1] = 1
    
    for i in route:
        print(i)
    
    print('---------------')

    for i in range(1,len(route)):
        location = [1,1]
        for j in range(1,len(route[i])):
            #문제에서 puddles의 좌표값이 반대로 나와있음
            location[0] = j
            location[1] = i
            if location in puddles:
                route[i][j] = 0
            else:
                route[i][j] = route[i][j-1] + route[i-1][j]

    for i in route:
        print(i)

    answer = route[len(route)-1][len(route[0])-1]
    answer = answer%1000000007
    return answer


m = 4
n = 3
puddles = [[2,2]]
print(solution(m,n,puddles))