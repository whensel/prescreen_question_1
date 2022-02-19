from src.sequence_solver import sequence_processor

def test_sequence_test_1():
    sample_sequence = [1,2,3,4,5]
    sample_sub_sequence = [[1,2],[3,4],[5]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == True

def test_sequence_test_2():
    sample_sequence = [1,4,7,5,2]
    sample_sub_sequence = [[1,4],[7,5],[3]]

    response = sequence_processor(sample_sequence, sample_sub_sequence)
    assert response == False