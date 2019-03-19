def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out
bubble_sort([1,5,3,6,1,8,9,15,2,7,100])


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    items.sort()
    return items
merge_sort([1,5,3,6,1,8,9,15,2,7,100,50,60,20,90])




def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)

    if len_i <= 1:
        # Logic Error
        # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
        # len <= 1
        return items

    pivot = items[-1]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
quick_sort([1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1,100,50])
