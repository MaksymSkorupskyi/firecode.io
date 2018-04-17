"""Insert Stars
Given a string, recursively compute a new string
where identical, adjacent characters
get separated with a "*".

Example:
insert_star_between_pairs("cac") ==> "cac"
insert_star_between_pairs("cc") ==> "c*c"
abba -> ab*ba
None -> None
abbba -> ab*b*ba
bbb -> b*b*b
"""

def insert_star_between_pairs(a_string):
    if type(a_string) != str:
        return None
    s = a_string[0]
    for i in range(1, len(a_string)):
        if a_string[i] == a_string[i-1]:
            s += ('*')
        s += (a_string[i])
    return s

print(insert_star_between_pairs("cac"))
print(insert_star_between_pairs("cc"))
print(insert_star_between_pairs("abba"))
print(insert_star_between_pairs("abbba"))
print(insert_star_between_pairs("None"))
print(insert_star_between_pairs(None))