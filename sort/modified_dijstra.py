import heapq


def main():

    '''
    input:

    5 7 0
    0 1 2
    0 2 6
    0 3 7
    1 3 3
    1 4 6
    2 4 1
    3 4 5


    :return: [0, 2, 6, 5, 7]
    '''


    V, E, s = map(int, input().split())
    AL = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        AL[u].append((v, w))


    dist = [float('+inf') for _ in range(V)]
    dist[s] = 0
    heap = []
    heapq.heappush(heap, [0, s])
    while heap:
        d, u = heapq.heappop(heap)
        for v, w in AL[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    print(dist)


main()