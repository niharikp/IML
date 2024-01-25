# IML
Some algorithms for 10601-Introduction to Machine Learning class

1. majority_vote_classifier

    The Majority Vote Classifier is a straightforward and robust machine learning model that predicts the class of an instance based on the most frequent label from a set of classifiers. It excels in ensemble methods, enhancing prediction stability and reducing noise by aggregating and democratically selecting the majority class from multiple models. Ideal for both binary and multi-class problems, this classifier offers simplicity, versatility, and robustness, especially in diverse and ensemble model settings.

    ## Input
    - Training and testing datasets in .tsv format.
    - File names for output predictions and metrics.

    ## Output
    - Training prediction labels file.
    - Testing prediction labels file.
    - Training and testing error rates in an evaluation metrics file.

    ## Functions
    - `read_file_contents(filename)`: Reads .tsv file contents into a list of lists.
    - `get_true_labels(dataset)`: Extracts labels from the dataset.
    - `mode(dataset)`: Finds the majority label in the dataset.
    - `train(train_data)`: Trains the model on the training dataset.
    - `hypothesis(x)`: Model to predict the label.
    - `predict(test_data)`: Predicts labels on the testing dataset.
    - `evaluate(true_labels, predicted_labels)`: Calculates the error rate.

    ## Implementation Details
    - Global variable `majority_value` stores the mode of the training dataset.
    - Training and testing datasets are read from specified .tsv files.
    - Predictions and error rates are written to specified output files.

    ## Requirements
    - Python 3.x
    - sys
    - csv


 
