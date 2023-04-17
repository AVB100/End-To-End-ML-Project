import os
import sys
from sklearn.metrics import r2_score
from src.exception import CustomException
import dill
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(file_path)
        # Create the directory if not exists
        os.makedirs(dir_path, exist_ok=True)
        # Open the file in binary write mode
        with open(file_path, "wb") as file_obj:
            # Serialize and save the object to the file
            dill.dump(obj, file_obj)
    except Exception as e:
        # Raise a custom exception with error details
        raise CustomException(e, sys)

def evaluate_model(x_train, y_train, x_test, y_test, models, params):
    try:
        # Create an empty dictionary to store the model evaluation report
        report = {}
        # Loop through the models
        for i in range(len(list(models))):
            # Get the current model
            model = list(models.values())[i]
            # Get the hyperparameters for the current model
            para = params[list(models.keys())[i]]

            # Create a GridSearchCV object with the current model and hyperparameters
            gs = GridSearchCV(model, para, cv=3)
            # Fit the GridSearchCV object to the training data
            gs.fit(x_train, y_train)

            # Set the best hyperparameters to the model
            model.set_params(**gs.best_params_)
            # Fit the model with the best hyperparameters to the training data
            model.fit(x_train, y_train)

            # Predict the target variable on the training data
            y_train_pred = model.predict(x_train)
            # Predict the target variable on the test data
            y_test_pred = model.predict(x_test)
            # Calculate R-squared score for training data
            train_model_score = r2_score(y_train, y_train_pred)
            # Calculate R-squared score for test data
            test_model_score = r2_score(y_test, y_test_pred)
            # Store the test data R-squared score in the report dictionary with the model name as key
            report[list(models.keys())[i]] = test_model_score
        # Return the model evaluation report
        return report
    except Exception as e:
        # Raise a custom exception with error details
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        # Open the file in binary read mode
        with open(file_path, "rb") as file_obj:
            # Load and deserialize the object from the file
            return dill.load(file_obj)
    except Exception as e:
        # Raise a custom exception with error details
        raise CustomException(e, sys)