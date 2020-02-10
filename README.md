# Automated Discourse: HW2 -- ParlAI
## Aaron Mueller, Alexandra DeLucia

### Guide to Repository
This repository contains our code and chatlogs used for homework 2. The code (including our modified `world_logging.py` script) is available in the `parlai` folder.

Our chat logs are available in the `model_chats` folder. We used similar stimuli to Vinyals & Le (2015) to get a diverse array of chat topics. The json files prefixed by 's2s' were from our seq2seq model, and those prefixed by 'kvmemnn' are from the ConvAI2 Kvmemnn model in ParlAI's model zoo.

### Model Details
Our seq2seq model was trained using the following hyperparameters (anything not specified was left as default):

- 2-layer encoder-decoder architecture
- LSTM cells
- Embedding dimensionality 256
- Hidden size 1024
- Optimized w/ SGD (i.e., batch size 1)

The validation perplexity was 600.71, and test perplexity was 647.28.

Our model is very large (1.2G), so we could not upload it or any of its checkpoints to this repository. Please see the following directory on the CLSP grid for our model (incl. dictionary):

`/export/b02/amueller/parlai-hw2`
