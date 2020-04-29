# Ion Switching
---
**Data Source: https://www.kaggle.com/c/liverpool-ion-switching/data**

This data set was downloaded from Kaggle and placed in the data folder. There are 3 files, a training set, a testing set to predict and submit to kaggle with and an example submission.

## Goal
---
This project seeks to be able to predict the number of ion channels open in a patch clamp recording. Being able to do this would be extreemly useful for the study of ion channels which are implicated in a lot of diseases. This would allow scientists to use patch clamp data with multiple channels rather than having to throw it out. Throwing out data with multiple channels in a patch leads to a lot of wasted time and resources. The idea is to make a model that is very optimized for predicting on the testing set.

## Process
---
### Data Preparation
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

### Modeling
- 5 of the same model was made but each was trained on a unique waveform.
- The first succesfull model was a random forest and got a score of up to 0.927 when fully optimized.
- Using Neural networks and tuning them a macro F1 Score of 0.938
- The hope is to find better more optimal models for getting a high macro F1 Score
- There are many differnt models that were tested as well as attempting different ways of training the neural networks.
- Cross validation was used to make the models perform better when applied to the testing set.


### Evaluation
- The model was evaluated on a Macro F1 score by submiting it to Kaggle. The score before final submission is on 30% of the test data.

## Future Improvements
---
TODO

