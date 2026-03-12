# bad:
def gc_bad(s):
    c = 0

    for l in s:
        if l == "G" or l == "C":
            c += 1

    return c / len(s)

# still bad:
def gc(s):
    c = 0  # initialize gc count

    for l in s:  # loop over bases
        if l == "G" or l == "C":  # check if base is G or C
            c += 1  # increment counter

    return c / len(s)  # return gc content

# better:
def calculate_gc_content(sequence):
    gc_count = sum(1 for base in sequence if base == "G" or base == "C")
    return gc_count / len(sequence)