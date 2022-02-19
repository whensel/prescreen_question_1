def sequence_processor(example_sequence, example_sub_sequence):
    return True


if __name__ == "__main__":
    sample_sequence = [1, 2, 3, 4, 5]
    sample_sub_sequence = [[1, 2], [3, 4], [5]]
    result = sequence_processor(sample_sequence, sample_sub_sequence)
    print(result)
