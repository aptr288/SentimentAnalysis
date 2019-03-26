def intersect(nums1, nums2):
    intersectList = []
    for i in nums1:
        for j in nums2:
            print("present element")
            print(i)
            print("Updated List")
            print(nums2)
            if (i == j):
                intersectList.append(i)
                nums2.remove(j)
                break
        print("Intersection List")
        print(intersectList)
    return intersectList

a = [4,9,5,4]
b = [9,4,9,8,4]

c = intersect(a,b)
print(c)