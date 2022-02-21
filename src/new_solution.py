def sequence_solver(example_sequence, example_sub_sequence):
    try:
        flat_list = [item for sublist in example_sub_sequence for item in sublist]
        if example_sequence == flat_list:
            return True
        else:
            return False
    except:
        return False



if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    sample_sub_sequence = [[1, 2], [3, 4], [5]]
    response = sequence_solver(sample_sequence, sample_sub_sequence)
    print(response)

