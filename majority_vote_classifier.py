# ------------------------------------------------------------------------------------------------------------------------
# 10601 : HW1 
# AUTHOR: Niharika Patil (niharikp)
# DATE MODIFIED: 1/24/2024
#-------------------------------------------------------------------------------------------------------------------------
# PROGRAM: Majority Vote Classifier
# TERMINAL INPUT: python majority_vote.py train.tsv test.tsv train_labels.txt test_labels.txt metrics.txt
# INPUT: Seperated training and testing data in a .tsv file
# OUTPUT: Train prediction labels file, test prediction labels file, train and test error in an evaluation metrics file 
# Ex: python majority_vote.py heart_train.tsv heart_test.tsv 
#       \heart_train_labels.txt heart_test_labels.txt heart_metrics.txt
#
# ------------------------------------------------------------------------------------------------------------------------

#Import necessary libraries
import sys
import csv

# Function to read the contents of a .tsv file into a list of list
# Arguments: Name of the file
# Returns: The file in the form of a list of list of each row elements
def read_file_contents(filename):
    data = []
    with open(filename, 'r') as file:
        #Assuming all inputs to be in a .tsv format, using csv library's reader function
        lines = csv.reader(file, delimiter='\t')
        data = [line for line in lines]
    return data

# Function to extract all the true labels from a given data set (assuming that the label is in the last column of the input)
# Arguments: Dataset containing features and labels in the same row
# Returns: List of all the labels for the dataset
def get_true_labels(dataset):
    true_labels = [row[len(row) - 1] for row in dataset[1:]]
    return true_labels

# Function to find the most frequently occuring labels
# Arguments: Dataset containing features and labels in the same row
# Returns: "Mode" or the majority label, In case of a tie, returns the label with a higher value
def mode(dataset):
    #Obtain all the true labels of the dataset
    true_labels = get_true_labels(dataset)
    #Create a set of all the distinct true labels
    unique_values = set(true_labels)
    #Count the number of each label
    value_counts = {x:true_labels.count(x) for x in unique_values }
    #Find the maximum count of the frequencies
    max_count = max(value_counts.values())
    #identify all the labels with the highest number of occurances
    modes = [value for value, count in value_counts.items() if count == max_count]
    #return the maximum label
    return max(modes)

# Function to train the classification model
# Arguments: Training dataset containing features and labels in the same row
# Returns: Predictions on the features of the training dataset using the trained model
def train(train_data):
    global majority_value 
    majority_value = mode(train_data)
    train_pred = [majority_value for x in train_data[1:]]
    return train_pred

# Classification Model
# Arguments: Feature Vector
# Returns: Predicted Label
def hypothesis(x):
    return majority_value

# Function to predict on test dataset using the trained classification model
# Arguments: Testing dataset containing features and labels in the same row
# Returns: Predictions on the features of the training dataset using the trained model
def predict(test_data):
    test_pred = [ hypothesis(x) for x in test_data[1:]]
    return test_pred

# Function to evaluate error rate on a dattaset and model's predictions 
# Arguments: Dataset containing features and labels in the same row and the list of predictions
# Returns: error rate
def evaluate(true_labels, predicted_labels):
    error_count = 0
    for y, y_pred in zip(true_labels, predicted_labels): 
        if(y != y_pred):
            error_count += 1
    return error_count/len(true_labels)

# Read all the arguments from the terminal and store them in a list
if __name__ == "__main__":
    files = [x for x in sys.argv[1:]]

# Read the train and test data into variable
train_data, test_data = map(read_file_contents, files[:2])
# Assign output files to appropriate variables
_, _, train_out, test_out, metrics_out = files

#Globar variable to hold the value of the "mode"
majority_value = -1

# train model
train_pred = train(train_data)

# predict using model on test data
test_pred = predict(test_data)

# calculate the train and test error rate
error_train = evaluate(get_true_labels(train_data), train_pred)
error_test = evaluate(get_true_labels(test_data), test_pred)

# write error rates into the metrics file
with open(metrics_out, 'w') as f:
    f.write(f'error(train): {error_train:.6f}\n')
    f.write(f'error(test): {error_test:.6f}\n')

# write train labels into the output file
f = open(train_out, 'w')
f.writelines([f'{label}\n' for label in train_pred])

# write test labels into the ouput file
f = open(test_out, 'w')
f.writelines([f'{label}\n' for label in test_pred])