def solution(citations):
    citations.sort(reverse=True)
    c_len = len(citations)
    for index in range(c_len):
        if (index+1 > citations[index]):
            return index
        
    return c_len