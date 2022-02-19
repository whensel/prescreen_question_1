## takes two different lists and checks to see if one can build the other
def sequence_processor(expected_sequence, example_sub_sequence):
    deconstructed_sub_list = deconstruct_sub_sequence(example_sub_sequence)
    deconstructed_sub_list = sorted(deconstructed_sub_list)

    ## catch-all for length mismatches
    if len(expected_sequence) != len(deconstructed_sub_list):
        return False

    ## see if they match up, sorting to make sure they are in the same order
    total = 0
    idx = 0
    for item in sorted(expected_sequence):
        deconstructed_list_value = deconstructed_sub_list[idx]
        print(deconstructed_list_value)
        if str(item) == str(deconstructed_list_value):
            total = total + 1
        else:
            pass
        idx += 1

    ## check to see if data matches
    if total == len(expected_sequence):
        return True
    else:
        return False


## converts list to string, to quickly 'remove' sub-sequences from list, checks for strs or ints
def deconstruct_sub_sequence(example_sub_sequence):
    result = (
        str(example_sub_sequence)
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .split(", ")
    )
    try:
        result = list(map(int, result))
    except:
        result = list(map(str, result))

    return result


## for speed testing
# if __name__ == "__main__":
#     sample_sequence = ['a', 'b', 'q', 'd', 'e']
#     sample_sub_sequence = [['a', 'b'], ['c'], ['e']]
#     result = sequence_processor(sample_sequence, sample_sub_sequence)
#     print(result)
