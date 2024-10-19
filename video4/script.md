# LLMs (PART II)

## Script
Reinforcement Learning from Human Feedback is perhaps the most common way of performing alignment.
Let's review the three phases for training an LLM:

- Pre-training: This is where it is trained on lots data scraped from the internet, think of Wikipedia
  or Redding. During this phase it learns general world knowledge and grammar.
- Fine-tuning: the second phase is where the model specialises on one or multiple tasks. The model is
  trained on human-curated datasets about answering questions, summarising text, or generating code. 
- Alignment: the final phase is where the model is trained to align with human values and preferences.
  This is where RLHF comes in.

We first create a copy of our fine-tuned LLM. This will be our baseline model. Here pi theta is the fine-tuned 
model, and pi-zero is the copy. We will never change the parameters of pi-zero. 
The second step is to create a second copy, except that we replace the last linear layer with a new one
that outputs a scalar value, known as reward. This will be our reward model that we use in RL.

Recall that in RL, there is an agent in an environment with state s_t. The agent then picks an action
conditional on the state, according to a probability distribution, known as policy. In turn, the environment
returns a new state and a reward for the action. The aim of reinforcement learning is to learn a policy
that maximises the expected reward.

RLHF requires two steps. The first one is training the reward model on human preferences data.
The second step is to use this reward model in a RL setting, to learn an optimal policy. The policy
in our case is the fine-tuned LLM.

Stay tuned for the next video, where we will see how to train the reward model.
If you've enjoyed this video, click follow, for more AI Safety content.




## Script
Welcome to the second video of my series on LLMs. 

In the previous video, we saw that an LLM is just a function that maps token indices to 
probabilities for the next token. But how do we make sure that these probabilities
are high for good tokens and low for bad ones?

To produce an output LLMs use billions or trillions of numbers. These are called parameters.  

Well, the LLM is a parametrized function. Parameters are just numbers that are used internally by the function 
to map an input to an output. For instance, think of the slope and intercept of a line, these are two 




At its core, an LLM is just a function and like all functions it takes an input
and returns an output. So what's the input to an LLM?

Ideally, we would like the LLM to take as input letters or words, because that's 
how we communicate. But computers work with numbers. The first thing to do, is to
build a vocabulary. A vocabulary is just a set of objects, that we call tokens. 

Tokens should be able to represent anything that could be written in text. For instance
letters, numbers, words, pieces of words, and all symbols on your keyboard.

We then sort the vocabulary, just like in a dictionary, and put the tokens in order.
This is called an indexing. Each token has an associated index, which is just an integer.

This means that we can encode everything as a sequence of integers, rather than characters.
The LLM will then process this sequence of integers
and will output a vector of floating point numbers. One number for each token in the vocabulary.

Think of this vector as a histogram over the vocabulary. Each number tells us the probability
of that token to be the next in the sequence. When you write to ChatGPT, the model chooses
the next token based on this histogram and repeats this many times. 

But how does it know how to make a good histogram? Well, stay tuned for the next video
where we will look at what it means to train a language model.

If you've enjoyed this video, click follow, for more AI Safety content.






1. Vocabulary
2. Token Indices
3. Embeddings
4. LLM
5. Training data
6. Training dynamics
7. Loss function
8. Text generation