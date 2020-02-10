# Automated Discourse: HW2 -- ParlAI
## Aaron Mueller, Alexandra DeLucia

### Guide to Repository
This repository contains our code and chatlogs used for [homework 2](https://dialog-systems-class.github.io/assignment2.html). The code (including our modified `world_logging.py` script) is available in the `modified_parlai` folder.

Our chat logs are available in the `model_chats` folder. We used similar stimuli to Vinyals & Le (2015) to get a diverse array of chat topics. The json files prefixed by 's2s' were from our seq2seq model, and those prefixed by 'kvmemnn' are from the ConvAI2 Kvmemnn model in ParlAI's model zoo. The chats are saved in [Forever Chat JSON format](https://github.com/jkeen/forever-chat-format).

### Model Details
Our seq2seq model was trained using the following hyperparameters (anything not specified was left as the [default settings](https://parl.ai/docs/agent_refs/seq2seq.html)):

- 2-layer encoder-decoder architecture
- LSTM cells
- Embedding dimensionality 256
- Hidden size 1024
- Optimized w/ SGD (i.e., batch size 1)

The validation perplexity was 600.71, and test perplexity was 647.28.

Our model is very large (1.2G), so we could not upload it or any of its checkpoints to this repository. Please see the following directory on the CLSP grid for our model (incl. dictionary):

`/export/b02/amueller/parlai-hw2`

### Code
We also include the modified ParlAI files, located in `modified_parlai`. The full modified codebase is located in a different GitHub repo [here](https://github.com/AADeLucia/ParlAI). The full repo is a fork of the original [ParlAI codebase](https://parl.ai/). We made the following modifications to the code:

* Option to save model checkpoints individually while training, instead of overwriting the same file
* Option to save chats from the interactive task (`interactive.py`)
* Added Forever Chat JSON format export for world logging

The code is installed and setup the same way to setup ParlAI

```bash
git clone https://github.com/AADeLucia/ParlAI.git
cd ParlAI; python setup.py develop
```

Saving model checkpoints individually

```bash
python -m parlai.scripts.train_model -m seq2seq -t twitter -mf models/twitter_s2s.model --overwrite-checkpoints False --save-every-n-secs 3600
```

Saving chat logs during interactive mode

```bash
python -m parlai.scripts.interactive -mf <your model> --save-world-logs True --report-filename <output file>.jsonl --world-logs-format forever
```
