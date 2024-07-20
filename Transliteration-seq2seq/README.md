# CS6910 : Assignment 3

## Files and Folders :

We have the following files and folders in the repository :

a) seq2seq_model.ipynb : the code for building and training the RNN based seq2seq model as per the mentioned specifications. This file also generates the required wandb plots for the seq2seq model.

b) seq2seq_model_testing.ipynb : the code for evaluating the perfomance of the seq2seq model on the test data.

c) seq2seq_model_with_attention.ipynb : the code for building and training the seq2seq model with attention mechanism. This file also generates the required wandb plots.

d) seq2seq_attention_testing.ipynb : the code for evaluating the perfomance of the attention based seq2seq model on the test data.

e) attention_visualization.ipynb : the code for visualizing attention heatmaps, executing one codeblock after another sequentially will generate attention heatmaps for some inputs from the test data,

f) atten_q6.ipynb : the code for "Connectivity" visualization.

g) GPT2_english_lyrics_generator.ipynb : the code for finetuning the GPT2 model to generate lyrics for English songs. Executing this notebook one code-block after another will generate song lyrics. Dataset link is already present in the code.

h) predictions_vanilla.tsv : a table containing the predictions of the vanilla seq2seq model on the test data.

i) predictions_attention.tsv : a table containing the predictions of the attention based seq2seq model on the test data.

j) attention_plots.png : attention heatmaps for some inputs from the test data, attention_visualization.ipynb generates this attention heatmap.


### Instructions for training and evaluating the models
All the relevant functions, wandb settings and configurattions are present within the notebooks. Running the code cells one after another will perform the tasks asked in the assignment. If one wishes to change the hyperparameter settings then he/she needs to update the "sweep_configuration" object. All the wandb log statements are already present in the code. In order to change the number of times wandb agent runs one needs to change the count parameter in wandb.agent('',train,count=).
