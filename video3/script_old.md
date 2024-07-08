# REINFORCEMENT LEARNING FROM HUMAN FEEDBACK (PART I)
Paper: (Loosely) Training Language Models to Follow Instructions with Human Feedback

## Script
Welcome to my series on Reinforcement Learning from Human Feedback, where I go through
how OpenAI trained ChatGPT-3 to follow instructions and be a helpful assistant.

If you have pre-trained your own Language Model you will know just how painful it is to get it 
to reply to a prompt in a helpful way. The first stage is perhaps the most boring one, but necessary.

OpenAI started from a GPT-3 model pre-trained on a subset of the internet. It then hired 40 contractors 
from Upwork and ScaleAI based on how similar to the researchers they were at flagging sensitive content, 
ranking the quality of responses and a bunch of other metrics. zj

The contractors then wrote prompts following the researchers guidelines. 


In a 2022 paper they described how they used a technique from robotics to align ChatGPT3.




1. Start from GPT-3 model pre-trained on a subset of the internet.
2. Hire 40 contractors from Upwork and ScaleAI based on how similar they were to researchers:
    - flagging sensitive speech
    - ranking quality of responses
    - reply sensibly to sensitive prompts
    - ability to identify sensitive speech for different groups
3. Supervised Fine-Tuning (SFT):
    - *Contracted labelers write 3 kinds of prompts*:
      - Plain: arbitrary task, maximising diversity.
      - Few-shot: E.g. "give the sentiment for a tweet" and then (tweet, sentiment) pairs
      - User-based: based on waiting list of applications mentioned in OpenAI API.
    - *API User Prompts*
      - Collected prompts from users using InstructGPT beta version (with informed consent).
      - Train/test/split made so that prompts from the same user are in the same set

