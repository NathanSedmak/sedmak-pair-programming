def offset_array_mean(array, new_mean):
    """
    Function Purpose:
    This function allows you to offset the mean of an array to an inputted value
    This function requires the Numpy library
    _____________________________________________________________________________________________
    Input: array
    Type: np.ndarray
    This input is the array of values which you wish to rescale
    _____________________________________________________________________________________________
    Input: new_avg
    Type: float or integer
    This input is the new mean which you wish the set of numbers to have
    ______________________________________________________________________________________________
    Output: new_array
    Type: np.ndarray
    This output is an array made of values offset such that the mean is equal to the inputted mean
    """
    assert type(array) == np.ndarray, 'Incorrect type for array'
    assert type(new_mean) == int or type(new_mean) == float, 'Incorrect type for new average input'
    new_array = array + (new_avg - array.avg())
    assert new_array.mean() == new_mean, 'The function encountered an error in creating the new array'
    return new_array