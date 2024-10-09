def create_tuples(list1, list2):
    return [(x, y) for x, y in zip(list1, list2)]
list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]
result = create_tuples(list1, list2)
print(result)
