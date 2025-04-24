# ## replaceing all even numbers to zero in a list
# my_list = [32,33,7,54,88,75,9,8,98]
# list2 = my_list.copy()
# for i in range(len(my_list)):
#     if my_list[i] % 2 == 0:
#         my_list[i] = 0


# print("Original list: ",my_list)
# print("Modified list: ",list2)

#### Write a Python program to input elements in a list 
# and print all the prime numbers in it.
# A prime number is a number that is only divisible by 1 and itself.
def is_prime(i):
    """
    Check if a number is prime.
    
    Parameters:
    i (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if i < 2:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

print(is_prime(23))  # Example usage

normal_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_list = []
for i in normal_list:
    if is_prime(i):
        prime_list.append(i)
print("Original list:", normal_list)
print("Prime numbers in the list:", prime_list)