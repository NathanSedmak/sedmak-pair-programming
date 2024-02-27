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

### Feedback - Peyton Chandler ###
# There are a couple of errors in line 21, new_avg should be new_mean and np does not have a attribute .avg
# I appreciate there being assertions throughout the definition. They help clarify what could go wrong in the code.

"""
    ___________________________________________
    General Info
    This function serves only as a test for the offset array mean created by Nathan Sedmak
    This function requires the numpy module
    ___________________________________________
    Inputs
    None
    ___________________________________________
    Returns
    Nothing
    ___________________________________________
    Prints
    If both tests are sucessful, a message indicating that the function has passed all tests will be printed
    An error message will be printed if any of the tests are failed
    ___________________________________________
    Tests
    Test 1: Determines whether the Offset Array Mean function works for a range of integers from 0 to 1.
    Test 2: Determines whether the normalize function works with negative values.  
    ___________________________________________
    """
    test_1_array = np.arange(0.1,0.5,0.2)
    assert np.mean(new_array) != new_mean, 'Offset Array Mean function failed test 1. Function does not work for a range of integers from 0 to 1.'
    test_2_array = np.arange([-100, -6, -47])
    assert np.mean(new_array) != new_mean, 'Offset Array Mean function failed test 2. Function does not work for negative input values.'
    print('All tests passed')