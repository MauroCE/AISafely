# LLMs (PART I)

## Script
Welcome to the first video of my series on LLMs. 

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