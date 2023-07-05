class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        heapq.heapify(l)
        for i in points:
            distance=math.sqrt(i[0]*i[0]+i[1]*i[1])
            heapq.heappush(l,[distance,i[0],i[1]])
        result=[]
        for i in range(k):
            dis,x1,y1=heapq.heappop(l)
            result.append([x1,y1])
        return result

"""K nearest points to the origin, can be done with dict method
but the duplicate values are removed and some test cases are getting 
failed, so used heapq.... heappush(l,[dist,x[0],x[1]]) dist is compared first 
for every point to maintain heap property ---> same like key in sorted function
when it has multiple values passed"""