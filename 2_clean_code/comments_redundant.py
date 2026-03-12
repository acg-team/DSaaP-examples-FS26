# bad:
def calculate_gc_content_bad(sequence):
    gc_count = 0  # initialize gc count

    for base in sequence:  # loop over bases
        if base == "G" or base == "C":  # check if base is G or C
            gc_count += 1  # increment counter

    return gc_count / len(sequence)  # return gc content

# better:
def calculate_gc_content(sequence):
    gc_count = 0

    for base in sequence:
        if base == "G" or base == "C":
            gc_count += 1

    return gc_count / len(sequence)