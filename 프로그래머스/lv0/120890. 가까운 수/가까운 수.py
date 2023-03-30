def solution(array, n):
    min_diff = float('inf')
    result = None
    for i in array:
        diff = abs(i - n)
        if diff < min_diff:
            min_diff = diff
            result = i
        elif diff == min_diff:
            result = min(result, i)
    return result
