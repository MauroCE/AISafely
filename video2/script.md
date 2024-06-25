# Black-Box access is insufficient for rigorous AI audits
Paper: https://arxiv.org/pdf/2401.14446

## Script
A research team led by MIT and Harvard have put out a paper showing that black-box access
to AI models is insufficient for rigorous audits. 

Black-box access means that auditors can design the input and then analyse the output of the 
model but have no access to the model's internal workings. This approach is unreliable 
for detecting adversarial inputs, and it is biased by how auditors design the prompts.

Grey-box access gives the additional flexibility of studying the embedding layers 
and activations, whereas white box access means that weights, gradients and even fine-tuning 
are available.

The authors argue that white-box access allows auditors to design better adversarial attacks 
by using gradient-based optimization. Also, access to internal representations means 
that it is possible to check the presence of certain capabilities, such as fairness or 
memorization.

However, the most thorough type of access, is out-of-the-box meaning that the auditors can 
examine the code, documentation and even training data, which can be helpful in detecting 
harmful and biased content used to train the model. 

Companies tend to dislike white-box or out-of-the-box access because it can lead to data leaks.
The authors suggest three strategies to minimize this risk. From a technical point of view,
APIs can be a satisfactory tool for auditing. From a physical perspective, a secure research 
location is essential and hosting auditing on site is not uncommon in other industries, such 
as nuclear energy. Finally, from a legal point of view, the authors suggest mimicking 
what is already done in the financial sector in terms of confidentiality and non-disclosure
clauses.

If you've enjoyed this video, click follow, for more AI Safety content.
