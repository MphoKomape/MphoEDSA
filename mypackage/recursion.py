def sum_array(array):

    '''Return sum of all items in array'''
    if len(array)==0:
        return 0
    else:
        return array[0]+ sum_array(array[1:])
sum_array([5,5,5,3])


def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)
fibonacci(4)


def factorial(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(5)


def reverse(word):

    '''Return word in reverse'''
    if word=="":
        return word
    else:
        return word[-1]+ reverse(word[:-1])
reverse("komape")
