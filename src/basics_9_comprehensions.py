# comprehensions are concise syntax to describe lists, sets and dictionaries

words = "egy kettő három télen nyáron".split()

lengths = [len(word) for word in words] # this results in [3, 5, 5, 5, 6]
# it's kinda like words.Select(x => x.Length).ToArray() in c#

# the general expression for lists is
# [ expression(item) for item in iterable]
# for sets it's the same just use {} braces
# for dictionaries we do
# { key_expression(item) : value_expression(item) for item in iterable}

# we don't have to do anything for the expression in the beginning, we can just say "item for item"

# a handy dict comprehension example is to flip a dictionary

country_to_capital_map = {
    "Germany": "Berlin",
    "Hungary": "Budapest",
    "France": "Paris"
}

capital_to_country_map = {capital : country for country, capital in country_to_capital_map.items()}

# if a dict comprehension produces duplicate keys, later keys will override earlier keys


# all comprehensions support a filter, that we can define

def is_even(x):
    return x % 2 == 0

even_numbers = [x for x in range(100) if is_even(x)] # this is like Enumerable.Range(100).Where(x => x % 2 == 0).ToArray() in c#

# comprehensions should have no side effects