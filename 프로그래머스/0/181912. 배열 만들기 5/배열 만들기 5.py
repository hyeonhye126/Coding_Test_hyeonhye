def solution(intStrs, k, s, l):
    answer = []
    for ints in intStrs:
        tmp = ints[s:s+l]
        if int(tmp) > k:
            answer.append(int(tmp))
    return answer