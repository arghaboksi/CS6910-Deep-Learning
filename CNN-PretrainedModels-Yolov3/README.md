# Deep Learning CS6910 : Assignment 2
We have organized the assignment into three folders :
1) Part A : Training a CNN from scratch 
2) Part B : Fine-tuning pretrained models
3) Part C : Using a pre-trained model for some application

We used Keras for implementation purpose. 
1) [Problem Statement](https://wandb.ai/miteshk/assignments/reports/Assignment-2--Vmlldzo0NjA1MTU)
2) [Report](https://wandb.ai/shubham-argha/Assignment%202/reports/Assignment-2--VmlldzoxNzI3OTc5)

## Part A folder : 
### CS6910_Assignment_2_part_A.ipynb

This file contains the implementation of all the questions asked in part A using Keras. 

We created a "sweep_configuration" object which contains different hyperparameter values we tried during our experimentation.

Hyperparameters and their corresponding values:

filter_shape : [(3, 3),(3, 3),(3, 3),(3, 3),(3, 3)], [(3, 3),(5, 5),(3, 3),(3, 3),(3, 3)], [(5, 5),(5, 5),(5, 5),(5, 5),(5, 5)], [(5, 5), (5, 5),(3, 3),(3, 3),(3, 3)], [(3, 3),(5, 5),(5, 5),(3, 3),(3, 3)]

dropout_probability : [0, 0.25, 0.20, 0.30]

learning_rate : [1e-3, 1e-4]

activation_function : ['relu']

batch_normalization : ['true', 'false']

filter_organization : [64, 64, 128, 512, 512], [32, 64, 128, 512, 512], [32, 32, 64, 64, 128], [32, 64, 64, 128, 128], [32, 64, 128, 128, 512], [64, 64, 64, 64, 64], [512, 128, 128, 64, 32]

data_augmentation : ['true', 'false']

FC_layer_size : [32, 64, 128, 256, 512]

num_of_epochs : [5, 10, 20]

### best_model
Contains the best model we found during experimentation.

### Guided_backprop.png
We have randomly selected 10 neurons from the  5th convolutional layer, applied guided backpropagation, and visualied them for all the 10 available classes. We have also plotted the gradients so that we can see which pixels are more influential according to the model while training.

### filters.png
Visualises all the filters in the first layer of our best model

### test_grid.png
Contains a 10 x 3 grid containing sample images from the test data and predictions made by our best model.

### Instructions for training and evaluating the model
All the relevant functions, wandb settings and configurattions are present within the notebook. Running the code cells one after another will perform the tasks asked in the assignment. If one wishes to change the hyperparameter settings then he/she needs to update the "sweep_configuration" object. All the wandb log statements are already present in the code. In order to change the number of times wandb agent runs one needs to change the count parameter in wandb.agent('',train,count=).


## Part B folder : 
### CS6910_Assignment_2_Part_B.ipynb

This file contains the implementation of all the questions asked in part B using Keras. 

We created a "sweep_configuration" object which contains different hyperparameter values we tried during our experimentation.

Hyperparameters and their corresponding values:

freeze_before : [50, 60, 70]
  
pretrained_models : ['InceptionV3','InceptionResNetV2', 'ResNet50V2', 'Xception']
            
FC_layer_size : [32, 64, 128, 256, 512]
      
num_of_epochs': [5]

### Instructions for training and evaluating the model
All the relevant functions, wandb settings and configurattions are present within the notebook. Running the code cells one after another will perform the tasks asked in the assignment. If one wishes to change the hyperparameter settings then he/she needs to update the "sweep_configuration" object. All the wandb log statements are already present in the code. In order to change the number of times wandb agent runs one needs to change the count parameter in wandb.agent('',train,count=).
