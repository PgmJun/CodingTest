def solution(my_string, overwrite_string, s):
    answer = ''
    my_string = list(my_string)
    print(my_string)
    
    for i in range(s, s+len(overwrite_string)):
        print(my_string[i] + " => " + overwrite_string[i-s])
        my_string[i] = overwrite_string[i-s]
        
    answer = ''.join(my_string)
    return answer