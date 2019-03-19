from mypackage import myFunction

def recursion():
    """
    make sure recursion works correctly
    """
    assert myFunction.sum_array(np.array([5,5,5,3]))==18
    assert myFunction.fibonacci(4)==3
    assert myFunction.factorial(5)==120
    assert myFunction.reverse("komape")=='epamok'


def sorting():


    assert myFunction.bubble_sort([1,5,3,6])==[1, 3, 5, 6]
    assert myFunction.merge_sort([1,5,3,10])==[1, 3, 5, 10]
    assert myFunction.quick_sort([1,5,4,3])==[1, 3, 4, 5]
