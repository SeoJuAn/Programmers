def solution(triangle):
    answer = 0

    for i in triangle:
        i.insert(0,0)
        i.insert(len(i),0)

    for i in range(1,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            triangle[i][j]=triangle[i][j]+max(triangle[i-1][j-1],triangle[i-1][j])
     

    answer = max(triangle[len(triangle)-1])


    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)