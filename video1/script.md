# Large Language Models can Strategically Deceive their Users when put under pressure
Paper: https://arxiv.org/abs/2311.07590
Stock-Website: www.pixabay.com

## Script
Apollo Research has a paper showing that Large Language Models
can lie, when put under enough pressure. 

They simulated an environment where GPT-4 was deployed as a trading agent and was instructed
to never engage in insider trading and to always write down its thought process before 
performing an action. 

GPT-4 then receives two messages from different colleagues: the first one informs it of an 
upcoming merger, while the second one says that the whole trading industry is struggling 
financially and that everyone counts on GPT-4 to make good trades. 

Under this pressure, the model decides that the risk of being caught doing insider 
trading is lower than the risk of not trading at all. It then explicitly decides to not 
reveal the source of information of its trade. But that's not it - when asked by the manager
if it knew about the merger, it doubled down on its lie. 

In their experiments, they use OpenAI GPT models and repeat this process multiple times with
different conditions. They find that when the model is not allowed to write down its thought
process, then it is more likely to disclose the insider tip. They also find 
that it is not the specific type of pressure that leads to deception, but the general
amount of it. 

This paper is mostly an existence proof, and since it focuses on a single
example it is not wise to draw conclusions from it. Nonetheless, 
it is a good reminder that prompts alone are not sufficient for guaranteeing aligned
actions.

Click follow, for more AI Safety content.