# Deep Learning for Automated Discourse Homework 2
### Aaron Mueller and Alexandra DeLucia

This repo is the completed the assignment outlined on the course website [here](https://dialog-systems-class.github.io/assignment2.html).

## Model
Model Parameters 

* 2-layer LSTM-based seq2seq
* 256-dimension embeddings
* 1024 hidden size
* optimized with true SGD (batch size is 1)
* ParlAI seq2seq defaults for the remaining settings, specified [here](https://parl.ai/docs/agent_refs/seq2seq.html)
* Trained for 24 hours

Due to the size of the model we were not able to include it in this repo. It is located on the CLSP grid in `/export/b02/amueller/parlai-hw2`

## Chats
We include 5 chats with our model (`s2s`) and 5 chats with a model in the ParlAI zoo (`kvmemnn`). The chat logs are in [Forever Chat JSON format](https://github.com/jkeen/forever-chat-format) and are located in `model_chats`. 

## Code
We also include our modified ParlAI codebase, located in `parlai`. This is just a local copy of the code, the full modified codebase is located in a different GitHub repo [here](https://github.com/AADeLucia/ParlAI). The full repo is a fork of the original [ParlAI codebase](https://parl.ai/). We made the following modifications to the code:

* Added ability to save model checkpoints individually while training, instead of overwriting the same file



### Installation

### Examples

