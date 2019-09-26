def flatten(input_list: list):
    """
        This simple recursive algorithm flattens a nested list of integers by
        starting with an empty return_list and iterating over the provided list. If
        the next item in the list is an integer, it adds it to the return_list.
        Otherwise, the next item is a list, so the function calls itself on the
        item, and adds the returned list to the end of return_list.

        Arguments:
            input_list: nested list of integers (items are integers, or list of integers)

        Returns:
            flattened list of integers

    """
    # initialize empty list to store the list we're going to return at the end
    return_list = []
    # iterate over the provided list
    for item in input_list:
        # if the item is an int,
        if isinstance(item, int):
            # append the int to our return_list
            return_list.append(item)
        # if the item is a list,
        elif isinstance(item, list):
            # make a recursive function call and add the returned list to the end of the return list
            return_list += flatten(item)
        # if the item is not an int or list,
        else:
            # raise a TypeError
            raise TypeError('List items must be integers, or list of integers')
    # after iterating over the entire list, return the flattened list
    return return_list
