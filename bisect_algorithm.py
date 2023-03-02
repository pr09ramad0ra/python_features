import bisect

# example with integers:

list_to_be_changed = [10, 1, 20, 3, 40, 5]
element_to_be_inserted_into_list = 20

# insert element 20 to the list [10, 1, 20, 3, 40, 5] and print the index of inserted element
print(bisect.bisect(list_to_be_changed, element_to_be_inserted_into_list)) # the index of inserted element is 6 - the last one cause the list is not sorted
print(bisect.bisect(sorted(list_to_be_changed), element_to_be_inserted_into_list)) # the index of inserted element is 5 - the index of existed element 20 is 4, the next one is inserted one is 5
print(bisect.bisect_left(sorted(list_to_be_changed), element_to_be_inserted_into_list)) # the index of inserted element is 4 - the index of existed element 20 is 4, replaced with inserted one 4
print(bisect.bisect_right(sorted(list_to_be_changed), element_to_be_inserted_into_list)) # the same as for bisect - 5

https://docs.python.org/3/library/bisect.html#module-bisect
