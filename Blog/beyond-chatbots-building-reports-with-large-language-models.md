---
title: "Beyond Chatbots: Building Reports with Large Language Models"
category: Business
date: 2024-11-29
readTime: 6
description: We present a framework for generating comprehensive reports with LLMs.
image: /assets/images/blog/beyond-chatbots-building-reports-with-large-language-models.jpg
---
## Beyond Chatbots: Building Reports with Large Language Models

## Introduction

As Large Language Models (LLMs) transform business processes, organizations are exploring applications beyond chatbots. This article examines STORM, a framework that automates comprehensive report generation.

Researchers at the Stanford University published two interesting articles [1] [2] this year, where they propose a framework for reports generation with LLMs, and explore this framework in detail, including automated and human evaluations. They focus on generating Wikipedia articles from scratch. But the concept can be applied to other domains. Let’s take a look.

Writing a Wiki page can be split into two phases:

* Prewriting: researching on the topic and defining an outline for the report

* Writing: writing the article using the information gathered during research, and following the outline

## How to proceed with LLMs?

The most simple approach would be to use LLMs without any external sources. After all, LLMs inherently possess a wealth of knowledge, embedded in the model. This approach is prone to hallucinations and lack of details.

To circumvent the hallucination problem, the LLMs can be connected to external sources. This is known as Retrieval-Augmented Generation, RAG. This approach still faces the issue of lacking depth.

## STORM

To go deeper, the researchers propose STORM (**S**ynthesis of **T**opic **O**utlines through **R**etrieval and **M**ulti-perspective Question-Asking), which:

* Generates relevant experts with various perspectives

* Makes an iterative question-answering process

![STORM set-up (from [1])](https://cdn-images-1.medium.com/max/2000/1*qaGkC_DAhYQnNr0UIlPEZQ.png)

![Schematic view of how STORM gets breadth and depth](https://cdn-images-1.medium.com/max/2240/1*P_Yq5EG0kjwTCKYoniz4kw.png)

In the STORM framework, starting from a topic t, the LLMs, based on similar articles, identify perspectives in form of experts (e.g. “A financial analyst”) that are relevant for the topic. Once the experts are identified, the LLMs simulate conversations in form of question-answering between a Wikipedia Writer and each expert. The experts have access to external documentation (in this case Internet). The conversations and the information collected are provided to the LLM, which uses it to define an outline for the article. Once the outline is done, the LLM writes the entire article section by section, following the outline, and grounded with the conversations and information collected in the prewriting stage.

## Results

How does this compare to the more basic approaches? To evaluate the quality of the outputs, the researchers have applied various approaches to generate Wikipedia articles, and have compared the results to the existing, human written Wikipedia article (considered as the “ground truth”). The analysis is entirely automated. For details about the method, we suggest reading the article [1].

![Evaluation of article outline (from [1])](https://cdn-images-1.medium.com/max/2000/1*DMRPFBdL5yKS7hREavX7AQ.png)

![Evaluation of article (from [1])](https://cdn-images-1.medium.com/max/2000/1*8DrDPT7X__p_ViWu7fHeYQ.png)

For the outline, we observe first that better models generate better outlines (as expected). The STORM framework is systematically better in identifying the relevant outline. It helps especially having a higher recall compared to more simple approaches.

For the entire article, STORM is the clear winner in all evaluation criteria.

What about human evaluation? Let’s look at the results:

![Human evaluation for 20 pairs of articles, scale from 1 to 7, 4 being of “good quality” (from [1])](https://cdn-images-1.medium.com/max/2000/1*--2zOsiojF_Albn8NM1OPg.png)

![Evaluation of usefulness of STORM, n=10 (from [1])](https://cdn-images-1.medium.com/max/2000/1*qI5uoiW0r2Xs497v-eaaRg.png)

Humans (which are human Wikipedia editors) evaluate articles generated with STORM as of higher interest, better organized, more relevant, having a higher coverage and better verifiability than articles written with more basic approaches (oRAG, which consists of using RAG for each section of the outline). But still, editors comment that the generated articles are “less informative than actual Wikipedia pages”, and that “the transfer of bias and tone from Internet sources to the generated article” are a major issue. The generated articles sound “emotional” and “unneutral”. Although the article does not provide a solution to this issue, we believe that enhanced prompting techniques could address these concerns to some degree, based on our experience.

To experiment with STORM, the researchers have made it available on-line ([link](https://storm.genie.stanford.edu/)). On this website, you can generate a report for your own topics (and provide feedback).

![User Interface of STORM](https://cdn-images-1.medium.com/max/2000/1*yFcjO7vnxqKn74gTzPswXA.png)

## Co-STORM

Building on STORM’s success, the same researchers have refined and extended their work into the Co-STORM framework [2], where the user can interact with the system during the question-asking phase by intervening any time in the conversation. In this set-up, instead of having N independent conversations between a Wiki writer and experts, there is a roundtable, with a moderator and experts that can ask or answer questions to the experts round. The user can also ask or answer anything anytime. This makes the framework more interactive and we understand this can be helpful when researching on a topic. Since this can be used as a “research assistant”, it has been compared to the use of a Search Engine and to the use of a RAG Chatbot. See results below.

![Evaluation of Co-STORM (from [2])](https://cdn-images-1.medium.com/max/2000/1*S8bEeJtZVcPTzTYTnJbV3g.png)

In general, users appreciate this set-up more than Search and RAG. It helps users find broader and deeper information, provides information with less mental effort.

## Open Source

The STORM framework proves to be a good candidate to automate report generation, going beyond the typical usage of LLMs as chatbots.

Can we apply the STORM framework to other domains than Wikipedia? The Stanford researchers have open-sourced their entire code ([link](https://github.com/stanford-oval/storm)) and made it available under a MIT License. This means that you are free to use the framework, adapt it to your use case, and commercialize it.

## Use Cases

How does it apply to other use cases? The researchers have focused on Wikipedia pages, but the potential extends far beyond. You can apply this in any settings where reports are produced based on information that is available digitally. Think of investment reports, or annual reports for companies, or other similar documents.

## Conclusion

LLMs have been very successful in augmenting productivity of office workers, with the use of chatbots. In this article we have presented a novel approach, STORM, where LLMs are used to create entire reports.

This framework can be customized to other topics, beyond Wikipedia pages. It can also make use of other knowledge sources than the Internet.

I hope this article has been helpful and enjoyable to read. For organizations looking to advance from chatbots to automated report generation, I am available to assist in implementing and customizing this framework to suit your specific requirements.

## References

[1] “Assisting in Writing Wikipedia-like Article From Scratch with Large Language Models”, Y. Shao et al., 22 Feb 2024.

[2] “Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations”, Y. Jian et al., 27 Aug 2024.