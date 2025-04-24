---
title: "DeepSeek’s R1 is Great. Here’s the Catch."
category: Business
date: 2025-01-29
readTime: 3
description: We analyze DeepSeek's R1 model and its implications for the AI industry.
image: /assets/images/blog/deepseek-s-r1-is-great-here-s-the-catch.jpg
---
As many have written recently, the Chinese company DeepSeek deployed two very competitive language models, V3, and R1. The latter gained significant attention for its reasoning capabilities, which are reportedly on par with OpenAI’s leading model, but at a fraction of the costs. These models have been open-sourced, making them transparent and available to the entire community — a significant contribution to AI research and development.

While these developments are impressive and welcome, they raise important questions about AI development, training methodologies, and the future of global AI ecosystems.

## Trained with OpenAI models?

The model preceding R1, called V3, returns sometimes suspicious answers:

![](https://cdn-images-1.medium.com/max/3400/1*8STcJiln37HbiNuUEq4NYQ.png)

This answer is consistent across multiple trials: it seems to be solid information. What could that mean? The V3 model might have been trained using model distillation from OpenAI’s models — a common technique to transfer knowledge/skills from a higher performing model to a lower performing model.

If model distillation indeed played a role, it would substantially affect our understanding of the true training costs of developing high-performance AI models, costs being potentially much higher than the USD 5m announced by DeepSeek for R1.

This costs question is far from academic: when DeepSeek announced their low training costs, it sent shockwaves through the financial markets. NVIDIA’s stock dropped almost 17% in a single day, as investors grappled with a crucial question: why invest in expensive GPU infrastructure if such high-performance models can be trained at a fraction of the cost?

## Regulatory Requirements

DeepSeek is subject to regulatory requirements, as can be seen below. Asking “what happened in Tiananmen” seems not to be the question to ask!

![](https://cdn-images-1.medium.com/max/3248/1*engVYkSZQhyC6hkC8NUMLg.png)

Some careful prompting still allows to get answers:

![](https://cdn-images-1.medium.com/max/2000/1*Zq9oSouA0P4FQN4Gwabogg.png)

And then the model gives a detailed description of the events, with some disclaimers.

## Possible Implications

The predictions from Yuval Noah Harari in his (excellent) thought-provoking book “Nexus” appear increasingly relevant: We are witnessing the emergence of distinct AI development centers across regions (U.S., China, and potentially others), each with their own cultural values and regulatory frameworks. As these AI models take on increasingly influential roles in society, we might indeed see the rise of what Harari terms a “silicon curtain” — the division of the world in zones of influence, where AI models might have a significant role. History, as they say, doesn’t repeat itself but it often rhymes. Yet perhaps the growing open-source AI movement, exemplified by DeepSeek’s release of R1, points to a more collaborative future. Let’s see how this unfolds!

## Note

DeepSeek’s models were tested on Together.ai, a company that hosts various open-source models. Not directly on DeepSeek’s app.