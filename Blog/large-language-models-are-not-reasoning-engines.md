---
title: Large Language Models are not reasoning engines
category: Technical
date: 2024-07-08
readTime: 5
description: We show that Large Language Models are not reasoning engines.
image: /assets/images/blog/large-language-models-are-not-reasoning-engines.jpg
---
The rise or Generative AI, post-ChatGPT, has had a huge impact on the collective imagination. Many people speak about intelligence, in some extreme cases people have mentioned that some LLMs are sentient! The LLMs providers (like OpenAI or Anthropic) have not helped fighting against these thoughts, since they also talk about their models in almost a human way, Anthropic calling its Language Model Claude (thanks for making my name popular :-)), and OpenAI giving a personal touch to the LLM via a human voice.

But can Large Language Models think? And if not, what are they good at?

In this post I will guide you through two examples that clearly show the limits of LLMs in terms of reasoning. If you want to reproduce the first example yourself, please check my Jupyter Notebook in GitHub ([link](https://github.com/feldges/llm-and-reasoning)). The second example is obvious to reproduce.

I will also explain why these examples do not work, which will give us hints on when we can trust the “reasoning abilities” of Language Models, and when we cannot.

In the end I will also mention where we believe the LLMs can be best used, in data extraction and in writing, and why I think this is the case.

But first, let’s introduce two examples where we can clearly observe the limitations of the reasoning capabilities of LLMs.

## Caesar Cipher

This example was provided by Subbarao Kambhampati, a renowned AI Researcher.

An interesting method to encrypt a message is the Caesar Cipher. This consists of replacing each letter with another letter of the alphabet, by shifting everything by a given number of letters.

For example, using n=3, the letter “a” is replaced by the letter “d”, which is three letters further than “a” in the alphabet.

This is pretty easy and we can trust that anyone who has some reasoning abilities would be able to decrypt such a text. Let’s test a Language Model on this exercise.

In order to do this we introduce a function to encrypt a text, and we ask ChatGPT to decrypt it. Since we do it for each n (from 0 to 25), we use a program to execute it. But doing it with the Chatbot would give very similar results.

An example of it is, with a shift of n=5: the text “ The sun rises in the east and sets in the west.” becomes “Wkh vxq ulvhv lq wkh hdvw dqg vhwv lq wkh zhvw.” Not easy to interpret, but if you know the rule, you can easily solve it.

Using the model gpt-3.5-turbo, run on 8 July 2024, we get the following results. n is the shift, meaning that if n=5, we encrypt the text by moving all the letters by 5 units in the alphabet. The result we show is the decryption done by ChatGPT. The original text was “ The sun rises in the east and sets in the west.”.

![](https://cdn-images-1.medium.com/max/2000/1*9-xBAbZaG1uFxXRAteg15g.png)

The result is fascinating and very enlightning: it works only in very special cases: if the shift is very small (0, meaning no encryption, and 1) or if the shift is 13, exactly in the middle.

How can we interpret this? The interpretation is that the Language Models do not reason. They imitate what they see in the training data they have been trained on. In this case, we can assume that there are many cipher examples on the web (the training data) where the letters are shifted by one or by 13, which seem to emerge as standard cases.

This example shows us that (i) the Language Models are good at repeating what they see in the training data, and (ii) the Language Models do not reason like humans do: they just mimic what they have seen at training time.

What does this teach us about the use of Language Models? It teaches us that we have to be extremely careful and need to ask ourselves the following: is my use case a repetition of what we can find on the web, or is it totally new? If it is totally new, you cannot use it as such but you would have to either fine-tune your model by providing many similar examples or apply a different algorithm that is not typically based on Language Models.

That’s a very interesting illustration of the limitations of Language Models. But you might argue: ok, this is a very specific example which requires the analysis of single letters, while Language Models are defined at word level (or more precisely at token level, which are words or parts of words), not at letter level.

Let’s look at another example, which was given by François Chollet, a famous AI Researcher.

## The Monty Hall Problem

Please read carefully the following chat:

![](https://cdn-images-1.medium.com/max/2000/1*j9UBJ8_lcsjy-4XnF5n_zQ.png)

This example was generated in July 2024 with ChatGPT 3.5. It is obviously totally wrong. If you blindly follow this advice you might simply lose a car that you have virtually already won! The reason for this wrong answer is that this problem, called “The Monty Hall Problem”, is a famous one and is typically formulated slightly differently. The answer to this famous problem is “yes”, switching is the best strategy.

The Language Model, which has been trained on the web (that contains many times this “slightly different” example), provides the standard answer: “yes”, switching is the best strategy.

## Conclusion

In conclusion, I want to highlight the fact that I am not at all saying the Language Models are useless. Language Models are extremely useful for many tasks, and they excel especially at tasks they have been trained on, like information extraction, summarization, writing, and to a certain extent, reasoning (but only on “standard problems”).

But it is extremely important to be aware of the (serious) limitations of Language Models, and that you cannot trust blindly their reasoning abilities.

You can only trust their “reasoning abilities” for use cases which are repeated many times on the web, which is the natural training data the Language Models are trained on. You cannot assume that Language Models reason on any type of problem.
