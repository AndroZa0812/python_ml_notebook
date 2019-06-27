def power_set(s):
    if len(s) == 0:
        yield set(set())
        return

    item = s.pop()
    subsets_without_item = power_set(s)
    for subset in subsets_without_item:
        yield subset
        new_subset = set(subset)
        new_subset.add(item)
        yield new_subset


my_set = {1, 3, 6}
for s in power_set(my_set):
    print(s)
