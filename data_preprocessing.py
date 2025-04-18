from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


# pandas_data: features data
# label_columns: labels data
# transform features into one hot encoded, labels to binaries encoded, split them into training and testing data.
def data_preprocessing_learning(pandas_data, label_columns):
    # turns feattures into one-hot encoded values
    one_hot = OneHotEncoder()
    data_array = np.array(pandas_data)
    fit_array = one_hot.fit(data_array)

    # create dict input_neuron_list : (feature name : list of unique feature values)
    count = 0
    input_neuron_list = {}
    for category in fit_array.categories_:
        n_list = []
        for item in category:
            n_list.append(item)
        input_neuron_list[pandas_data.columns[count]] = n_list
        count += 1

    # still one hot encoded but now array type
    data_one_hot = one_hot.fit_transform(data_array).toarray()
    print(data_one_hot)

    # encode the labels into binary format
    label_one_hot = []
    output_neuron_list = {}     # (label name : list of unique label values)
    label_binarizer = LabelBinarizer()
    for column in label_columns:
        column_array = np.array(column)
        label_fit_array = label_binarizer.fit(column_array)
        for label in label_fit_array.classes_:
            if column.name in output_neuron_list:
                output_neuron_list[column.name].append(label)
            else:
                output_neuron_list[column.name] = [label]
        label_one_hot.append(label_binarizer.fit_transform(column_array))
    print(label_one_hot)

    # setting up the training and testing data by splitting the data into 80% training and 20% testing
    # Since we have multiple labels, we have to do a separate training for each label , hence separate training data
    train_labels = []
    test_labels = []
    for label in label_one_hot:
        split = train_test_split(data_one_hot, label, shuffle=False)
        (train_x, test_x, trainLabel_y, testLabel_y) = split
        test_labels.append(testLabel_y)
        train_labels.append(trainLabel_y)
    print(test_x)
    return train_x, test_x, train_labels, test_labels, input_neuron_list, output_neuron_list


def data_preprocessing_predicting(pandas_data, features_data):
    concat_data = pandas_data.append(features_data, ignore_index=True)
    data_array = np.array(concat_data)
    # data_Array = np.array(features_data)
    one_hot = OneHotEncoder()
    data_one_hot = one_hot.fit_transform(data_array).toarray()

    return data_one_hot

