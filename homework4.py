# Read file and find word

def count_lines(word_to_search, filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if word_to_search.lower() in line.lower():
                count += 1
    return count

# This function takes list object and flattens in case there are iterables inside

def flatten(iterable):
    for item in iterable:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item