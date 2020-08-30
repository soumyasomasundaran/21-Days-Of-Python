def set_union(s1, s2):
    return s1.union(s2)


def set_intersection(s1, s2):
    return s1.intersection(s2)


def set_difference(s1, s2):
    return s1.difference(s2)


s_one = {1, 2, 3, 4, 5, 6}
s_two = (5, 6, 7, 8, 9, 10)
print(set_union(s_one, s_two))
print(set_intersection(s_one, s_two))
print(set_difference(s_one, s_two))
