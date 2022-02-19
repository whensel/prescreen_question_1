from src.sequence_solver import sequence_processor


def test_sequence_test_1():
    sample_sequence = [1, 2, 3, 4, 5]
    sample_sub_sequence = [[1, 2], [3, 4], [5]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_2():
    sample_sequence = [-1, -4, -7, -5, -2]
    sample_sub_sequence = [[-1, -4], [-7, -5], [-2]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_3():
    sample_sequence = [23, 67, 2, 98, 1038]
    sample_sub_sequence = [[23], [67, 2], [98, 1038]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_4():
    sample_sequence = [0, 583, 7463, -5, 42]
    sample_sub_sequence = [[0], [583], [7463], [-5], [42]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_5():
    sample_sequence = [1, 2, 3]
    sample_sub_sequence = [[1, 2], 3, [4, 5]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == False


def test_sequence_test_6():
    sample_sequence = [1, 1, 1, 1, 1]
    sample_sub_sequence = [[1, 1], [1, 1, 1]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_7():
    sample_sequence = [-1, 1, 1, -1, 1]
    sample_sub_sequence = [[-1, 1], [1, -1, 1]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_8():
    sample_sequence = [-1, 1, 1, -1, 1]
    sample_sub_sequence = [[-1, 1], [1, 1, 1]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == False


## maybe add functionality to process text strings
def test_sequence_test_strings_1():
    sample_sequence = ["a", "b", "c", "d", "e"]
    sample_sub_sequence = [["a", "b"], ["c", "d"], ["e"]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True


def test_sequence_test_strings_2():
    sample_sequence = ["a", "b", "q", "d", "e"]
    sample_sub_sequence = [["a", "b"], ["c", "d"], ["e"]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == False


def test_sequence_test_strings_3():
    sample_sequence = ["a", "b", "q", "d", "e"]
    sample_sub_sequence = [["a", "b"], ["c"], ["e"]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == False
