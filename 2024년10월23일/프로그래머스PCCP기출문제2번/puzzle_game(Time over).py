def solution(diffs, times:list, limit):
    level=0

    while True:
        answer=0
        for i in range(len(diffs)):
            if diffs[i]<=level:
                answer+=times[i]
            else:
                answer+=(((times[i-1]+times[i])*(diffs[i]-level))+times[i])
            if answer>limit:
                continue
        if answer<=limit:
            break
        else:
            level+=1
            continue
    if level==0:
        level=1
    return level
