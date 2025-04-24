####Write a function to remove duplicates from an array and
#return the new array.
def duplicates_v1(arr):
    return list(set(arr))

list2 = [32,78,54,232,5,4,22,12,42,5,32]
print("-----With Set-----")
print("Original list: ",list2)
updated_version = duplicates_v1(list2)
print("Without Duplicates: ",updated_version)
print("-------------")
# Bonus: Try solving it without using set() to practice more.

def duplicate_v2(arr):
    arr1 = []
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    return arr1

list2 = [32,78,54,232,5,4,22,12,42,5,32]
print("-----Without Set-----")
print("Original list: ",list2)
updated_version2 = duplicate_v2(list2)
print("Without Duplicates: ",updated_version2)

print("-------------")