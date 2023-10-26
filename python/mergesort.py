def merge(list_one, list_two):
    working = []
    list_one_pos = 0
    list_two_pos = 0

    while list_one_pos < len(list_one) and list_two_pos < len(list_two):
        if list_one[list_one_pos] <= list_two[list_two_pos]:
            working.append(list_one[list_one_pos])
            list_one_pos += 1
        else:
            working.append(list_two[list_two_pos])
            list_two_pos += 1

    while list_one_pos < len(list_one):
        working.append(list_one[list_one_pos])
        list_one_pos += 1

    while list_two_pos < len(list_two):
        working.append(list_two[list_two_pos])
        list_two_pos += 1

    return working


def merge_sort(collection_to_sort):
    collection_to_sort[:] = _merge_sort(collection_to_sort)
    
def _merge_sort(collection_to_sort):
    size = len(collection_to_sort)
    if size == 1:
        return collection_to_sort
    else:       
        list_one = _merge_sort(collection_to_sort[0 : size//2])
        list_two = _merge_sort(collection_to_sort[size//2 : ])
        return merge(list_one, list_two)
    
    
    