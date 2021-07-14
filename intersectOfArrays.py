'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Examples:

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted. '''

import time
start = time.process_time()
# your code here    
print("time taken : "+ str(time.process_time() - start))

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# # O(N^2)
# def returnIntersection(nums1,nums2):
#   count=0
#   returnArr =[]
#   for num in nums1:
#     if num in nums2:
#       returnArr.append(num)
#       count+=1
#   return returnArr

# print(returnIntersection(nums1,nums2))

# U

# M
# Using two pointer solution i and j

# P
# nums1.sort()
# nums2.sort()

# i and j = 0
# while(i< len(nums1) and j<len(nums2)):
#   #if nums1[i] == nums2[j]
#     #returnArr[count] = nums1[i]
#     #i+=1
#     #j+=1
#   #elif  nums1[i] < nums2[j]
#     #i++
#   #else 
#    #j++
# return returnArr

nums1 = [1,2,2,1]
nums2 = [2,2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

nums1.sort()
nums2.sort()


# O(N^2)
def returnIntersection(nums1,nums2):
  count=0
  returnArr =[]
  for num in nums1:
    if num in nums2:
      returnArr.append(num)
      count+=1
  return returnArr

# test def


# O(nlogn) + mlogn
def returnIntersection1(nums1,nums2):
  i =0 
  j = 0 
  count=0
  returnList=[]
  while(i< len(nums1) and j<len(nums2)):
    if nums1[i] == nums2[j] :
      returnList.append(nums1[i])
      count+=1
      i+=1
      j+=1
    elif  nums1[i] < nums2[j]:
      i+=1
    else :
      j+=1
  return returnList

print(returnIntersection1(nums1,nums2))
