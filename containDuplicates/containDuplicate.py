from typing import List

#Uses insertion in set to check for duplicates
def has_duplicates(nums: List[int]) -> bool:
    unique_set = set()
    
    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)
    
    return False

#Alternative method using set conversion
def has_duplicates_alternative(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(has_duplicates(nums))
    print(has_duplicates_alternative(nums))
