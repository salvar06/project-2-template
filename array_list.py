import unittest
# AnyList is either
# - None
# - List()

class List:
    def __init__ (self):
        self.length = 0 # an int
        self.array = [None] * self.length

    def __eq__(self, other):
        return (type(self) == type(other)
            and self.length == other.length
            and self.array == other.array
            )

    def __repr__(self):
        return ("List({!r})".format(self.array[:self.length]))

# -> AnyList
# returns an empty List
def empty_list():
    return List()

# AnyList -> int
# returns the length of the list
def length(any_list):
    return any_list.length

# AnyList int any -> AnyList
# returns an AnyList with the contents of the input list with the addition of the specified value at the given index
def add(any_list, index, val):
    if index < 0 or index > any_list.length:
        raise IndexError()

    output_list = empty_list()
    output_list.length = any_list.length + 1
    output_list.array = [None] * output_list.length

    for i in range(output_list.length):
        if i < index:
            output_list.array[i] = any_list.array[i]
        if i == index:
            output_list.array[i] = val
        if i > index:
            output_list.array[i] = any_list.array[i - 1]
    return output_list

# AnyList int -> any
# return value of AnyList at the specified index
def get(any_list, index):
    if index < 0 or index >= any_list.length:
        raise IndexError()

    for i in range(any_list.length):
        if i == index:
            return any_list.array[i]

# AnyList int any -> AnyList
# returns an AnyList with value at given index replaced with a new value
def set(any_list, index, value):
    if index < 0 or index >= any_list.length:
        raise IndexError()

    output_list = empty_list()
    output_list.length = any_list.length
    output_list.array = output_list.length * [None]

    for i in range(any_list.length):
        if i < index:
            output_list.array[i] = any_list.array[i]
        if i == index:
            output_list.array[i] = value
        if i > index:
            output_list.array[i] = any_list.array[i]
    return output_list

# AnyList int -> Anylist
# returns an AnyList is the value at the given index removed
def remove(any_list, index):
    if index < 0 or index >= any_list.length:
        raise IndexError()
    output_list = empty_list()
    output_list.length = any_list.length - 1
    output_list.array = output_list.length * [None]

    # if output_list.length == 0:
    #   output_list = empty_list()
    #   return output_list

    for i in range(output_list.length):
        if i < index:
            output_list.array[i] = any_list.array[i]
        if i == index:
            output_list.array[i] = any_list.array[i + 1]
        if i > index:
            output_list.array[i] = any_list.array[i + 1]
    return output_list

def foreach(List, f):
    for i in range(List.length):
        if List.array[i] == None:
            continue
        print (List.array[i])
    return None

def sort(List, comparator):
    for i in range(1, length(List)):
        temp = List.array[i]
        position = i

        while position > 0 and comparator(temp, List.array[position - 1]):
            List.array[position], List.array[position - 1] = List.array[position - 1], List.array[position]
            position = position - 1

            List.array[position] = temp

    return List

def comparator(a, b):
    return a < b

