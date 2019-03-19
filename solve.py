import datetime

from itertools import permutations

MAX = 10**10

def tsp(cur,visited,src):
    if visited == (1 << n)-1: # 모든지점을 방문했다.
        return dis[cur][src]
    
    if cache[cur][visited]:
        return cache[cur][visited]
    
    ret = MAX
    minn_nxt = MAX
    for nxt in range(n):
        if visited & (1<<nxt):
            continue
        result = tsp(nxt, visited | 1 << nxt, src) + dis[cur][nxt]
        if result < ret:
            minn_nxt = nxt
            ret = result
            
    path[cur][visited] = minn_nxt
    cache[cur][visited] = ret
    return ret

# src로부터 출발해서 모두 순회하는 거리
def get_dis(src):
    return tsp(src,1<<src,src)

# cur로 시작했을 때의 최소거리 경로 반
def get_path(cur, visited):
    result = []
    while path[cur][visited] != -1:
        result.append(cur)
        cur = path[cur][visited]
        visited |= 1<<cur
    result.append(cur)
    return result


if __name__ == "__main__":
    
    import sys

    at_start = datetime.datetime.now()

    file_name = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
    
    with open(file_name) as file:
        n = int(file.readline())
        pos = [list(map(int,file.readline().split())) for _ in range(n)]

    dis = [[0] * n for _ in range(n)]
    for p1 in range(n):
        for p2 in range(n):
            x1,y1 = pos[p1]
            x2,y2 = pos[p2]
            dis[p1][p2] = dis[p2][p1] = ((x1-x2)**2 + (y1-y2)**2)**0.5

    cache = [[0] * (1<<n) for _ in range(n)] # 거리
    path = [[-1] * (1<<n) for _ in range(n)] # 경로

    print()
    print('0부터 시작')
    print('거리 :', get_dis(0))
    print('경로 :', get_path(0,1<<0))

    minn = min((get_dis(i),i) for i in range(n))[1]
    if minn:
        print()
        print('%d부터 시작'%(minn))
        print(get_dis(minn))
        print(get_path(minn,1<<minn))

    print()
    elapsed_time = (datetime.datetime.now()-at_start).total_seconds()
    print('경과시간 : %f초'%elapsed_time)
    
