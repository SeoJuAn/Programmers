def solution(name):
    answer = 0

    # 0 1 2 3 4 5 6 7 8 9 10 11 12    13 14 15 16 17 18 19 20 21 22 23 24 25
    # a b c d e f g h i j k  l  m     n  o  p  q  r  s  t  u  v  w  x  y  z    
    # 26개

    count = 0
    min_move = len(name)-1
    for i in range(len(name)):
        index = ord(name[i])-65
        if index <= 12:
            count = count + index
        else:
            count = count + (25-index)+1

        next = i+1
        while next < len(name) and name[next]=="A":
            next +=1
        min_move = min(min_move,i+i+len(name)-next)

    count += min_move
        

    answer = count
    return answer

name = "JAZ"
print(solution(name))