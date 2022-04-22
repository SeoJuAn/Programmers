
def solution(routes):
    answer = 0

    #진출시간 기준 정렬
    #진출시간 작은순서에서 차례대로 count ++
    #진출시간 하나가 선택될 때마다 해당 값이 진입보다 크고 진출보다 작다면 리스트에서 삭제

    routes.sort(key=lambda x:x[1])
    i=0
    while(len(routes)!=0):
        answer+=1
        outTime = routes[i][1]
        #print(routes)
        #print(outTime)
        i+=1

        j=0
        while j<len(routes):
            
            if routes[j][0]<=outTime<=routes[j][1]:
                routes.remove(routes[j])
                i=0
                j=0
            else:
                j+=1

    #print('----------')

    return answer


#print(solution([[-2,-1], [1,2],[-3,0]])) #2
#print(solution([[0,0],])) #1
#print(solution([[0,1], [0,1], [1,2]])) #1
#print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
#print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
#print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
#print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2