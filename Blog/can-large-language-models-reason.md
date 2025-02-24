---
title: Can Large Language Models reason?
category: Technical
date: 2024-10-15
readTime: 6
description: We investigate the reasoning abilities of LLMs.
image: /assets/images/blog/can-large-language-models-reason.jpg
---
There are lots of speculations about the abilities of Large Language Models (LLMs) like ChatGPT to reason. Some researchers believed their LLM is sentient! Some LLMs received names (like Claude for Anthropic). We read in the news that LLMs pass the Bar exam. We observe that they speak like humans, with human voices. When we use them, we realize that they are really good at writing!

But can LLMs reason? And what does this mean for users of LLMs? Do we use them the right way? We are going to answer these questions in this article.

First, it is important to understand the context: the AI community is surfing on the Generative AI wave. The enterprises active in AI have very high valuations that can only be justified if LLMs continue to progress fast towards Artificial General Intelligence (AGI). AGI engines are systems that can solve problems they have never seen before and can learn on their own. The AI community is therefore pushing hard to convince people that we are on the path to AGI. All this creates unhealthy and distracting noise. So let’s see what LLMs can do and what are their limitations.

Let’s illustrate the weaknesses of LLMs with a simple example: the Monty Hall Problem. Please read carefully the chat below, that was done using ChatGPT 3.5.

![](https://cdn-images-1.medium.com/max/2000/1*P_mLZfPbQ8H24YmOk4vyJw.png)

The answer is obviously totally wrong, but expressed with such assurance that we might believe it, would we not think on our own! Think about it next time you ask ChatGPT about a topic you do not know at all: is the answer really correct?

Why does it give such a wrong answer? The reason is to be found in how the LLMs work, and how they are trained. LLMs do not have internal models of the world that help them interpreting situations. They simply generate the next word of a sentence, one at a time, based on the previous words. And how does the next word prediction work? It finds it thanks to how it was trained. Training is done in three steps: first pre-training is done by learning to predict the next word using huge datasets covering almost the entire internet, and even more. Second, fine-tuning is done on existing datasets which have a question and a (correct) answer, and the model learns to provide the right answer, given the question. Third, optionally there is the Reinforcement Learning with Human Feedback (RLHF), where human annotators (or simply users) assess the best answers provided by the LLMs among typically three possible answers.

This training approach teaches us valuable insights: the LLMs learn from the web (pre-training); it is especially good at use cases it was specifically trained on (fine-tuning); it adapts to human preference (RLHF). At no time the LLMs learn any model of the world during their training.

Now we have seen one specific example. Are there any studies that focus on the reasoning abilities of LLMs?

Recently, researchers at Apple have analyzed the mathematical reasoning abilities of LLMs and have come to the conclusion that “…current LLMs are not capable of genuine logical reasoning; instead, they attempt to replicate the reasoning steps observed in their training data” [1]. To come to this conclusion they have modified the benchmark GSM8K, a dataset of questions-answers used to assess the mathematical reasoning abilities of LLMs. They have modified it in two ways: (i) Replace names and/or numbers in the problem formulation (example: Sophie -> Alfred, nephew -> cousin, …), called the new method GSM-Symbolic, and (ii) Add information that is not needed to solve the problem, called the new method GSM-NoOp. See examples below.

![Example of question from the GSM8K benchmark. The elements highlighted have been changed in the new benchmark GSM-Symbolic. From [1].](https://cdn-images-1.medium.com/max/2000/1*TADwVq9CSDZA5QRTG_9PqA.png)

![Example of question from the GSM8K benchmark. The element highlighted has been added in the new benchmark GSM-NoOp. From [1].](https://cdn-images-1.medium.com/max/2528/1*nINzg43TrZq8kq3i0xG69g.png)

You can see the results below. Replacing names and numbers brings the accuracy of these models down. Adding unnecessary information brings the accuracy significantly down! How is that possible? It is very likely that models have been trained on these specific datasets, which is why they perform better on the original datasets than on modified ones. This phenomenon is known as data contamination: the evaluation datasets have been used for training.

![Accuracy decrease for (i) names and numbers changes (GSM-Symbolic) on the left, and (ii) adding unnecessary information (GSM-NoOp). From [1].](https://cdn-images-1.medium.com/max/3016/1*whnLeu04-xkvjH2rQQhcYg.png)

Another example that purely focuses on the reasoning and planning abilities of LLMs was analyzed by Subbarao Kambhampat’s team [2,3]. It is a benchmark called PlanBench, that has two parts: (i) benchmark using Blocks world, and (ii) benchmark using Mystery Blocks world. The Blocks world consist of blocks of different colors sitting on a table, some of them stacked. The LLMs are asked to reach a given state, starting from another state. See an example of instruction below and detailed description of the method on [Wikipedia](https://en.wikipedia.org/wiki/Blocks_world). The Mystery Blocks world consist of the same logical problems, but formulated in a different domain that no LLMs have seen before.

![Example of instructions for the Blocks world game. From [3].](https://cdn-images-1.medium.com/max/2828/1*uMB4n7YBQXOFnNUVM1MqCQ.png)

![Detailed instructions for the Blocks world game (left) and an example of the Mystery Blocks world game instruction (right). From [3].](https://cdn-images-1.medium.com/max/3936/1*Z5t8HHaIIe66KDgcIeQ1XQ.png)

The results are disappointing: while for the Blocks world problem, the best models achieve around 60% accuracy, for the Mystery Blocks world, none of the state-of-the-art models achieve more than 1% accuracy!!!

![Blocks world and Mystery Blocks world results for state-of-the-art LLMs. One shot means that one example is provided to the LLM. Zero shot means no examples are provided to the LLM, only the instructions. From [2].](https://cdn-images-1.medium.com/max/4112/1*NN3YJazN0V1bFpjb37gsAA.png)

Let’s look at the newest models from OpenAI, o1, that is reasoning according to OpenAI. We observe a significant progress. There, the planning and reasoning abilities of the model however go down with the number of steps the planning requires, as shown below. It is hard to interpret these results, because the functioning of this new model is kept secret.

![Results on Blocks world and Mystery Blocks world for OpenAI’s models o1. Well performing, with performance decreasing with the length of the plan (which is the number of operations needed to solve the problem). From [2].](https://cdn-images-1.medium.com/max/2864/1*y0Ykjo3407MIrvfMunozmQ.png)

To conclude, we showed in this article that LLMs are far from reasoning, and the apparent reasoning abilities we observe come from patterns the models learn from their training data. This has deep implications as it means that LLMs can only work on problems they have seen during training, or very similar.

What does it mean for us LLMs users? It means that we need to be careful when using them! Here are my recommendations:

* Do not trust blindly LLMs, especially on specific domains that are not widely spread

* All applications using LLMs should have a “human in the loop” approach, with a human always verifying the results

* Challenge vendors who pretend that their AI-based product if fully automated

* Define AI Principles for your firm stating among others that users of LLMs are entirely responsible for the output

I want to mention that I use LLMs daily and find them extremely helpful, especially for:

* Extracting Data

* Summarizing

* Writing

* Programming

* Brainstorming

For all these use cases, the models have been extensively fine-tuned. For programming there is abundant high-quality data available on the internet.

Thank you for reading! I hope this article has provided valuable insights into the world of AI. If you have any questions or would like to explore how AI might benefit your projects (or not), feel free to reach out to me on Medium or [LinkedIn](https://www.linkedin.com/in/claude-feldges-plocek-78090a1/). I’d be happy to share more of my experience in this rapidly evolving field.

**References**

[1] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models, Iman Mirzadeh et al., 2024

[2] LLMs still can’t plan; Can LRMs? A preliminary evaluation of OpenAI’s o1 on PlanBench, K. Valmeekam et al., 2024

[3] On the planning abilities of Large Language Models (a critical investigation with a proposed benchmark), K. Valmeekam et al., 2023
