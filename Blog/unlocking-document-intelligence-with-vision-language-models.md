---
title: Unlocking Document Intelligence with Vision Language Models
category: Technical
date: 2024-09-19
readTime: 5
description: We explore the use of Vision Language Models for document analysis.
image: /assets/images/blog/unlocking-document-intelligence-with-vision-language-models.jpg
---
A very successful Generative AI use case for enterprises has been the so-called RAG, or Retrieval-Augmented Generation. A Large Language Models (LLM) like ChatGPT gets access to a set of documents and returns answers based on these documents. This is done by combining a retriever (that retrieves relevant information from documents) and an LLM. Once the retriever has found the relevant passages, those are injected into the LLM, which is instructed to use this information to generate an answer. This works rather well in practice and is the reason why it has been successful so far.

While this use case is successful, it only works with text! In enterprises, documents are very often more than just a collection of texts. The layout itself already contains information. For example, it is not rare to see diagrams or workflows in slides, or just isolated keywords without any text associated to it, or companies represented with their logos instead of their name. How to find it with a text-only system?

To provide a concrete example, asset managers often receive pitch decks from companies wanting to raise money. These documents are created to “sell” the company and therefore they focus heavily on visual effects. These are typically not just texts. “Understanding” these documents with LLMs could trigger interesting use cases.

Is there any possibility to solve these limitations?

In the last few months, some LLMs have received “eyes” to become multimodal. They have been renamed to VLM, **Vision Language Models**. They can interpret documents not only based on texts, but also based on visual properties like layouts, tables, images. The leaders in the Generative AI space (OpenAI, Anthropic, Google) have all deployed such models, which can handle several pages at the same time (loaded as images).

Does it entirely solve the problem? Not yet, because the models do not scale to hundreds or thousands of pages. The missing piece to achieve this is a retriever that would identify which pages are relevant for a given question or a topic.

The missing piece has been created recently with the model ColPali, developed by Faysse et al [1]. The model directly finds the pages (as images) that are relevant to answer a given question. These pages can then be provided to a VLM to generate an answer. To be more concrete, you can see below how the model performs compared to traditional (non-visual) approaches, on standard “document understanding” benchmarks:

![Benchmarking of ColPali on standard tasks (from [1])](https://cdn-images-1.medium.com/max/2000/1*c6piuygP2P8XykXs2qv9Uw.png)

It is a huge step in performance. We are convinced that this new model will unlock many new use cases that were just not possible before.

The good news is that this model is open source, meaning that everybody can use it! But since it is very new, it requires some technical skills to implement. It also requires a powerful set-up that includes GPUs (special processors). You can check my technical article if you are interested in the implementation: [link](https://medium.com/gopenai/fe133667d2f9).

Let’s look at two concrete examples in finance: find information from the pitch deck of airbnb and wise (formerly transferwise). You can find these slide decks easily on the web.

For airbnb, there is a slide that compares airbnb with its competitors. Let’s look if ColPali will find this slide.

The slide we expect ColPali to pick is this one:

![airbnb competitors’ slide](https://cdn-images-1.medium.com/max/2000/1*-slVXzDHhflBNaC02nPDdA.png)

And this is what ColPali finds, and what the VLM (in this case Claude Sonnet 3.5) answers when fed with this slide:

![](https://cdn-images-1.medium.com/max/2264/1*7XAvdHrlkyFDYs-Ny_jpkA.png)

It gets it right!

For transferwise, there is a slide showing the roadmap.

![](https://cdn-images-1.medium.com/max/2972/1*tLLg7J3j104EIfe1OjbbNw.png)

The roadmap shows the current status in black text, while the future is light gray. This is obvious to human readers, but not at all to an engine that has only access to text. Vision is necessary to get to the right result. Let’s look at what ColPali combined with a VLM (in this case GPT-4o) gets:

![](https://cdn-images-1.medium.com/max/2000/1*DNxe2-xuULdc_DIdBEZCKw.png)

It gets it right! This result is impossible to get with traditional text analysis, the reason being that visual effects (black versus grey) are part of the analysis.

In general we experience the model from Anthropic (Claude Sonnet 3.5) as performing slightly better than GPT-4o on such tasks.

Note that these examples are simplified (on purpose). To generate the results we used only one slide. In practice it works well, however we would rather take the five or ten most relevant slides, and also take the slide just before and just after the retrieved ones (to make sure to have the entire context). This comes at the risk that information gets diluted and the answer less accurate.

I hope these examples have convinced you of the importance of VLMs. To conclude this article, I would recommend that whenever you have a use case that involves documents, ask yourself early whether you need vision on top of text. Now you know that this is possible!

If these models had come out earlier, my life as a data scientist would have been easier. What about you, do you know of use cases where VLMs would help?

Reference:

[1]: ColPali: Efficient Document Retrieval with Vision Language Models, m. Faysse et al., 2024 ([link](https://arxiv.org/abs/2407.01449))
