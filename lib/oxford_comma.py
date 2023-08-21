""" If the list has only 1 element, return that element as a string.
    If the list has 2 elements, join them with "and" and return the result.
    If the list has 3 or more elements:
    a. Join all elements except the last one with commas.
    b. Add "and" before the last element.
    c. Return the formatted string.
"""


def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    elif len(items) >= 3:
        formatted_items = ", ".join(items[:-1])  # joining the elements except the last one with a comma (,)
        formatted_items += f", and {items[-1]}"  # add ("and") before the last item in the list
        return formatted_items


# Test cases
print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))  # Output: "fiddleheads, okra, and kohlrabi"
