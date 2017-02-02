from collections import defaultdict


# Making a dictionary that maps keys to more than one value.
if __name__ == '__main__':
    # A defaultdict automatically initializes the first value so you can simply
    # focus on adding items.
    # Using a list if you want to preserve the insertion order of the items.
    d_list = defaultdict(list)
    d_list['a'].append(1)
    d_list['a'].append(2)
    d_list['a'].append(2)
    d_list['b'].append(4)
    print(d_list)

    # Using a set if you want to eliminate duplicates (and don't care about
    # the order).
    d_set = defaultdict(set)
    d_set['a'].add(1)
    d_set['a'].add(2)
    d_set['a'].add(2)
    d_set['b'].add(4)
    print(d_set)
