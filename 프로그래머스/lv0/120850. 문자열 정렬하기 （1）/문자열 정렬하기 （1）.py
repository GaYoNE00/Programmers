def solution(my_string):
    
    return sorted(map(int,"".join([i for i in my_string if (i in "0123456789")])))