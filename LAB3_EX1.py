def square_odds(nums):
    return [x**2 for x in nums if x % 2 != 0]
print(square_odds([2, 4, 3]))    
print(square_odds([0, 0, 1, 1])) 
