class Solution:
    def minmaxGasDist(self, stations, K):
        d = (stations[len(stations)-1] - stations[0]) / float(K)
        heap = []
        for i in range(len(stations)-1):
            n = max(1, int((stations[i+1]-stations[i]) / d))
            K -= (n-1)
            heapq.heappush(heap, (float(stations[i]-stations[i+1]) / n, stations[i], stations[i+1], n))

        for i in range(K):
            (d, a, b, n) = heap[0]
            heapq.heapreplace(heap, ((a-b)/(n+1.0), a, b, n+1))
        return -heap[0][0]    
