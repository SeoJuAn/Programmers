def solution(numbers):
    answer = ''
    strList = []

    for i in numbers:
        strList.append(str(i))
    strList.sort(key=lambda x:x*3,reverse=True)

    answer = "".join(strList)

    if answer[0]=="0" and len(answer)>1:
        answer = "0"

    return answer

numbers = [0,0,0]
print(solution(numbers))