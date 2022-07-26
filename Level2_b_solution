def solution(src, dest):
    #Your code here
    if src == dest:
        return 0
    
    if src == dest:
        return 0
        
    d = [-17, -15, -10, -6, 6, 10, 15, 17]
    visited = [False] * 64
    count = 0
    currentp = [src]
    nextp = []
    flag = False
    
    def available(src, flag):
        for i in range(8):
            if src + d[i] > -1 and src + d[i] < 64 and abs(src % 8 - (d[i] + src) % 8) < 3 and visited[d[i]+ src] == False:
                nextp.append(src + d[i])
                visited[d[i] + src] = True
                if src + d[i] == dest:
                    flag = True
                    return flag
        return flag
                
    while flag == False:
        count += 1
        for j in currentp:
            flag = available(j, flag)
        currentp = nextp
        nextp = []
        if flag == True:
            return count
