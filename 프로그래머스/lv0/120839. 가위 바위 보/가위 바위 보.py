def solution(rsp):
    rsp = rsp.replace('0','주')
    rsp = rsp.replace('2','가')
    rsp = rsp.replace('5','보')
    rsp = rsp.replace('주','5')
    rsp = rsp.replace('가','0')
    rsp = rsp.replace('보','2')
    return rsp