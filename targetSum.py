class Solution:
  def search(self, arr, target_sum):
    for i in range(len(arr)):
      for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target_sum:
          lis1=[i,j]
    if(len(lis1)>0):
      print(lis1)
      return lis1
    else:
      return [-1, -1]
s=Solution()
s.search([1,2,3,4,5],5)

"""https://www.designgurus.io/course-play/
grokking-the-coding-interview/doc/638ca0aa5b41522e8a2e3395"""