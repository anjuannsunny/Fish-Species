# Fish Species pediction Flask App

#### This Flask application predicts the species of a fish based on its physical dimensions using a machine learning model trained with scikit-learn.

## Overview
#### This application allows users to input the measurements of a fish—Length1, Length2, Length3, Height, Width, and Weight—through a web server. Upon submitting the form, the application predicts the species of the fish using a pre-trained machine learning model.

## Prerequisites
#### Python 3.7 or higher
#### Flask
#### scikit-learn

## Files
#### app.py: Contains the Flask application code, including routes for home and prediction.
#### index.html: HTML template for the user interface where users input fish measurements.
#### result.html: HTML template for displaying the prediction result.
#### fish_species_model.pkl: Trained machine learning model file.
#### label_encoder.pkl: Pickled label encoder used to transform species labels.

## App URL
#### https://fish-species-1-fh3s.onrender.com