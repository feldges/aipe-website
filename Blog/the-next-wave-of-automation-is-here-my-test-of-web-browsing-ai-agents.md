
---
title: "The Next Wave of Automation is Here: My Test of Web-Browsing AI Agents"
category: Business
date: 2025-03-10
readTime: 4
description: With a concrete use case we explore new techniques to automate web browsing.
image: /assets/images/blog/the-next-wave-of-automation-is-here-my-test-of-web-browsing-ai-agents.jpg
---

A lot is written about AI agents. They are supposed to be the future of AI. They will kill millions of jobs. They will kill SaaS business models. So I wanted to test out a specific use case: AI agents that can browse the web to execute actions or extract information.

## The Challenge: Complex Navigation on the Web

My use case comes from a personal frustration: ski resorts in Switzerland have introduced dynamic pricing. If you buy a ski ticket early you get rebates. If you buy ski tickets late you typically pay full price (or more). This is all good. But the problem is that as a customer, it is difficult to compare prices. This lack of transparency was already criticized by the authorities responsible for price monitoring in Switzerland. If you try to find the price for a ski pass on the ski resorts’ website, you will realize that it is complicated, which is probably intentional. In some cases you see the price only once you have put your ticket in your shopping cart!

It would be very useful to have a website that compares all the prices in real-time. But is an automated price extraction even possible, given the complexity of the websites?

## AI Agents: A New Approach

Traditional methods to extract data from websites, called web scraping, typically fail because of the complexity of finding this information. Two years ago, it would probably not have been possible to solve it.

But technological progress make things possible! For this use case I have spent a few hours programming, using a tool called playwright (a framework to automate testing of web applications) and a framework called [Browser-Use](https://browser-use.com/).

And it worked! While extracting the price you can follow in real-time what the AI agent is doing. It typically starts with a Google search to find the right web site. Then it navigates through the website. If needed it also adds a ski ticket to its shopping cart in order to see the price. As soon as it finds the price, it interrupts its exercise and returns the answer. Below we show a few screenshots.

![](/assets/images/blog/screenshots-web-browsing.jpg)

## A Real Example: Navigating Complex Pricing

One complex case was for the ski resort Davos Klosters: it is really necessary to enter each parameter (number of adults, date, …) and add the ticket to the shopping cart. You only see the price if you access your shopping cart. And the AI agent was successful in finding it!

## Current Limitations

While it works, the technology is in my view not yet mature. Many times, the AI agent gets lost by clicking on some Cookies policy that is irrelevant for its mission. But the results are very impressive: it was able to find the current price for all the ski resorts, but in some cases I had to run the exercise more than once.

For this use case we have used the model GPT-4o from OpenAI. It cost a few dollars (less than USD 5). The reason we did not use the cheapest model is that the agents work much better if they can “see” the website, i.e. these have to be multimodal models.

## Conclusion: The Future is Here, Almost

While the technology is not yet fully mature, AI agents that browse the web open exciting new opportunities and have the potential to disrupt many processes that seemed impossible to automate just two years ago. The pricing is also reasonable enough to justify replacing certain manual tasks, even in regions where labor costs are traditionally low.

What would make these technologies truly mature? Better handling of pop-ups, more reliable navigation through complex interfaces, and less distraction by irrelevant elements would be significant improvements we’ll likely see in the coming months.

I believe in testing new technologies hands-on rather than just reading about them. What started as my attempt to solve a personal frustration with ski ticket prices quickly showed me how powerful these AI agents could be for all kinds of business problems. So many use cases are possible — from tracking competitor prices to automating tedious research tasks that previously required human attention. The AI agent can also interact with the website, entering information, clicking on buttons — I have seen demos where the AI agent selected job openings and applied in the name of candidates! The potential use cases are almost infinite.

If you’re curious about how similar automation might benefit your organization, I’d be happy to share insights from my experience or discuss potential implementations. Feel free to reach out at [info@aipetech.com](mailto:info@aipetech.com).

## References

* Browser-Use website: [https://browser-use.com/](https://browser-use.com/)

* The code I used for my experiment is available on GitHub ([Link](https://github.com/feldges/price_tracker))
