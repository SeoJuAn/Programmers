import itertools

def solution(numbers):
    answer = 0

    numbers_list = []
    for i in range(len(numbers)):
        numbers_list.append(numbers[i])

    permutaions = []
    for i in range(1,len(numbers_list)+1):
        permutaions.append(list(itertools.permutations(numbers_list,i)))
        
    int_list = []
    for i in permutaions:
        for j in i:
            int_list.append((int(''.join(j))))
    
    int_set = set(int_list)
    int_list = list(int_set)

    count = 0

    for i in int_list:
         if is_prime_number(i):
             count = count + 1

    answer = count


    return answer

def is_prime_number(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    if x!=0 and x!=1:
        return True
    else:
        return False

numbers = "17"
print(solution(numbers))