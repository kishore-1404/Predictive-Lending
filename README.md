# Predictive Lending - Piramal Finance


## Challenge Overview

Piramal Finance caters to the diverse lending needs of the people of Bharat with a portfolio of products ranging from Secured loans to Unsecured loans. The task is to train a binary classification model that predicts the probability of a loan going bad.

## Dataset Description
### Train Data

* `train_1.csv`: Primary data with loan performance over a period of time.
* `train_2_1.csv`: Secondary data with bureau data for time period 1.
* `train_2_2.csv`: Secondary data with bureau data for time period 2.

### Test Data

* `test_1.csv`: Primary data to make predictions.
* `test_2_1.csv`: Secondary data for test (analogous to `train_2_1.csv`).
* `test_2_2.csv`: Secondary data for test (analogous to `train_2_2.csv`).

### Sample Submission

* `sample_submission.csv`: Illustrates the final submission format.

### Train Data

* `train_1.csv`: Primary data with loan performance over a period of time.
* `train_2_1.csv`: Secondary data with bureau data for time period 1.
* `train_2_2.csv`: Secondary data with bureau data for time period 2.

### Test Data

* `test_1.csv`: Primary data to make predictions.
* `test_2_1.csv`: Secondary data for test (analogous to `train_2_1.csv`).
* `test_2_2.csv`: Secondary data for test (analogous to `train_2_2.csv`).

### Sample Submission

* `sample_submission.csv`: Illustrates the final submission format.

## Columns Description

* `loan_id`: Primary key (loan ID)
* `id`: Secondary key (customer ID)
* `prod`: Product categorization (masked)
* `col_1` to `col_164`: Features in train and test data
* `add_1` to `add_677`: Additional features in bureau data
* `label`: Ground truth in the train data
* `prob`: Predicted probability for final submission

## Evaluation Metrics

The evaluation metric is the Area Under the Receiver Operating Characteristic Curve (ROC-AUC).

## Submission Guidelines

* Submit a CSV file with `loan_id` as index and `prob` as predicted probability.
* Ensure correct index values and column names as per `test_1.csv` and `sample_submission.csv`.
* File size should be 100000 x 2.

## Notes

* Handle outliers, missing values, and data-related issues carefully.
* Consider feature engineering and feature selection.
* Use any ML/DL technique for model development.

## Getting Started

1. Explore the dataset.
2. Clean and preprocess the data.
3. Develop and train a model.
4. Evaluate the model.
5. Submit the predicted probabilities.

## File Structure

dataset/
train_1.csv
train_2_1.csv
train_2_2.csv
test_1.csv
test_2_1.csv
test_2_2.csv
sample_submission.csv
README.md


## Dataset Description
### Train Data

* `train_1.csv`: Primary data with loan performance over a period of time.
* `train_2_1.csv`: Secondary data with bureau data for time period 1.
* `train_2_2.csv`: Secondary data with bureau data for time period 2.

### Test Data

* `test_1.csv`: Primary data to make predictions.
* `test_2_1.csv`: Secondary data for test (analogous to `train_2_1.csv`).
* `test_2_2.csv`: Secondary data for test (analogous to `train_2_2.csv`).

### Sample Submission

* `sample_submission.csv`: Illustrates the final submission format.

### Train Data

* `train_1.csv`: Primary data with loan performance over a period of time.
* `train_2_1.csv`: Secondary data with bureau data for time period 1.
* `train_2_2.csv`: Secondary data with bureau data for time period 2.

### Test Data

* `test_1.csv`: Primary data to make predictions.
* `test_2_1.csv`: Secondary data for test (analogous to `train_2_1.csv`).
* `test_2_2.csv`: Secondary data for test (analogous to `train_2_2.csv`).

### Sample Submission

* `sample_submission.csv`: Illustrates the final submission format.


## Columns Description
----------------------

* `loan_id`: Primary key (loan ID)
* `id`: Secondary key (customer ID)
* `prod`: Product categorization (masked)
* `col_1` to `col_164`: Features in train and test data
* `add_1` to `add_677`: Additional features in bureau data
* `label`: Ground truth in the train data
* `prob`: Predicted probability for final submission


## Evaluation Metrics
---------------------

The evaluation metric is the Area Under the Receiver Operating Characteristic Curve (ROC-AUC).


## Submission Guidelines
-----------------------

* Submit a CSV file with `loan_id` as index and `prob` as predicted probability.
* Ensure correct index values and column names as per `test_1.csv` and `sample_submission.csv`.
* File size should be 100000 x 2.


## Notes
--------

* Handle outliers, missing values, and data-related issues carefully.
* Consider feature engineering and feature selection.
* Use any ML/DL technique for model development.


## Getting Started
------------------

1. Explore the dataset.
2. Clean and preprocess the data.
3. Develop and train a model.
4. Evaluate the model.
5. Submit the predicted probabilities.


## File Structure
-----------------
dataset/
train_1.csv
train_2_1.csv
train_2_2.csv
test_1.csv
test_2_1.csv
test_2_2.csv
sample_submission.csv
README.md