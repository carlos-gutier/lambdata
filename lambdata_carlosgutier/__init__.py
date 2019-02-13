#!/usr/bin/env python
"""
Python module for splitting data into train, validation, and train datasets.
"""

from sklearn.model_selection import train_test_split

class DataSplitter(object):
    """
    Python module for splitting data into train, validation, and train datasets.
    It uses scikitlearn's 'train_test_split' to create additional validation
    dataset for additional data testingself.

    Parameters:
    X = independent features
    y = dependent feature (as Pandas Series)
    train_size = float, int, or None, (default=0.8)
    val_size = float, int or None, optional (default=0.1)
    test_size = float, int or None, optional (default=0.1)
    random state = boolean, optional (default=True)
    shuffle = boolean, optional (default=True)

    Returns:
    splitting : list, length=2 * len(arrays) and prints shape of each dataset
    List containing train-test split of inputs (X_train, X_validate,
    y_train, y_validate).
    """

    def __init__(
        self, X, y, train_size=0.8, val_size=0.1, test_size=0.1,
        random_state=None, shuffle=True):
        self.X = X,
        self.y = y,
        self.train_size = train_size,
        self.val_size = val_size,
        self.test_size = test_size,
        self.random_state = random_state,
        self.shuffle = suffle


    def train_test_splitter(self):

        # Ensure set sizes add up to 1
        assert (train_size + val_size + test_size == 1)

        # Divide data into 'test' and leftovers
        X_leftovers, X_test, y_leftovers, y_test = train_test_split(
        X, y, test_size=test_size,
        random_state=random_state, shuffle=shuffle)

    def train_val_test_splitter(self, X_leftovers, y_leftovers):

        # Divide leftovers into 'train' and 'validate'
        X_train, X_validate, y_train, y_validate = train_test_split(
        X_leftovers, y_leftovers, train_size=(train_size / (train_size + val_size)),
        random_state=random_state, shuffle=shuffle)

        # Print out the shapes of the datasets, to confirm that they're
        # what we expect
        print(f'X_train   : {X_train.shape}')
        print(f'X_validate: {X_validate.shape}')
        print(f'X_test    : {X_test.shape}')
        print()
        print(f'y_train   : {y_train.shape}')
        print(f'y_validate: {y_validate.shape}')
        print(f'y_test    : {y_test.shape}')
