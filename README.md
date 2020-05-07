# Ion Switching
---
**Data Source: https://www.kaggle.com/c/liverpool-ion-switching/data**

## Goal
---
This project seeks to be able to predict the number of ion channels open in a patch clamp recording. Being able to do this would be extreemly useful for the study of ion channels which are implicated in a lot of diseases. This would allow scientists to use patch clamp data with multiple channels rather than having to throw it out. Throwing out data with multiple channels in a patch leads to a lot of wasted time and resources. The idea is to make a model that is very optimized for predicting on the testing set.

## Table of Contents
---
- [Goal](#Goal)
- [Navigating the Repo](#Navigating-the-Repo)
- [Process](#Process)
    - [Data Preparation](#Data-Preparation)
    - [Modeling](#Modeling)
    - [Evaluation](#Evaluation)
- [Future Improvements](#Future-Improvements)


## Navigating the Repo
---
- enviroment.yml - file for creating the conda enviroment following the instructions at https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file for creating a conda envitoment from a .yml file
- presentation.pdf
- README.md
- src - this folder holds the python scripts with code for running the notebooks in the repo
- data - holds the data files downloaded from kaggle (train and test data)
    - models - trained models for easy acces in notebooks
    - train_data - this is the train data after processing
    - test_data - this is the test data after processing
- notebooks
    - exploratory - contains all the notebooks of the process. Each notebook is a development cycle of working with the data and creating a model and ending with submiting the predictions of the test set to Kaggle.
    - report - This contains the final notebook outlining the whole process of this project.

## Process
---
#### Data Preparation
- Inspect the data to see what is going on
- Find where the signal is being drifted
- Transform the data so the drift is no longer present
    - First transforming by a rolling mean was used
    - Then functions were used to transform the data (This was more succesfull)
- Break data into different waveforms
    1. 1 slow ion channel
    2. 1 fast ion channel
    3. 3 ion channels
    4. 5 ion channels
    5. 10 ion channels
- Perform the same steps for the testing data

#### Modeling
- 5 of the same model was made but each was trained on a unique waveform.
- The first succesfull model was a random forest and got a score of up to 0.927 when fully optimized.
- Using Neural networks and tuning them a macro F1 Score of 0.938
- The hope is to find better more optimal models for getting a high macro F1 Score
- There are many differnt models that were tested as well as attempting different ways of training the neural networks.
- Cross validation was used to make the models perform better when applied to the testing set.


#### Evaluation
- The model was evaluated on a Macro F1 score by submiting it to Kaggle. The score before final submission is on 30% of the test data.

## Future Improvements
---
With a project such as this there are always ways to improve the model in order to get the best 

