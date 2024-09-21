# [Amazon-Bedrock](https://aws.amazon.com/bedrock/?gclid=Cj0KCQjwurS3BhCGARIsADdUH52l-GFoELH10j-5-VEpktvqBdINMoVr_LTWsyX_4m-f9uMYCLNNVIkaAgLjEALw_wcB&trk=33b5edcf-0d26-4e1d-b868-603c42c06eaf&sc_channel=ps&ef_id=Cj0KCQjwurS3BhCGARIsADdUH52l-GFoELH10j-5-VEpktvqBdINMoVr_LTWsyX_4m-f9uMYCLNNVIkaAgLjEALw_wcB:G:s&s_kwcid=AL!4422!3!692062173500!e!!g!!aws%20bedrock!21054971903!164977109691)
aws-bedrock to use foundational models for specific usage

![image](https://github.com/user-attachments/assets/6369708f-9784-40fb-a1e2-0683b456a30e)

# What is Amazon Bedrock?
source: [aws](https://aws.amazon.com/bedrock/?gclid=Cj0KCQjwurS3BhCGARIsADdUH521Yg02MqROuLB7V6ChxRKOEIzDdBYDhlK_mp7IPLYvIdFvGfYotQAaAkEvEALw_wcB&trk=33b5edcf-0d26-4e1d-b868-603c42c06eaf&sc_channel=ps&ef_id=Cj0KCQjwurS3BhCGARIsADdUH521Yg02MqROuLB7V6ChxRKOEIzDdBYDhlK_mp7IPLYvIdFvGfYotQAaAkEvEALw_wcB:G:s&s_kwcid=AL!4422!3!692062173500!e!!g!!amazon%20bedrock!21054971903!164977109691)

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon through a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top FMs for your use case, privately customize them with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise systems and data sources. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with.

# How Amazon Bedrock works?
source: [TechTarget](https://www.techtarget.com/searchenterpriseai/definition/Amazon-Bedrock-AWS-Bedrock)

Amazon Bedrock gives software developers access to a wide range of foundation models from AI startups, such as AI21 Labs, Anthropic, Cohere and Stability AI through a serverless application programming interface (API). For example, large language models such as Claude 2 and open source, text-to-image models such as Stable Diffusion XL 1.0 -- released by Anthropic and Stability AI, respectively -- can be used with Bedrock to simplify the delivery of generative AI apps. 

On their own, foundation models are adept at comprehending natural language inputs and processing them to produce text or images as responses or outputs. However, they can't perform complex tasks or actions without direction. AWS released Agents for Amazon Bedrock to designate and automate complex tasks for a model without requiring a developer to manually write the code needed to do so. Specifically, developers can use agents to connect foundation models to their proprietary data sources so the apps they build will produce up-to-date answers based on their own data. When a user employs a generative AI app built with Bedrock, an agent makes API calls that retrieve the data needed from proprietary sources to answer the user's requests or queries. In addition to third-party foundation models, Amazon allows access to its own Titan foundation models, which include Titan Text to generate text and Titan Embeddings to translate textual inputs into numerical representations.

# Applications developers can make with Amazon Bedrock
### Amazon Bedrock can be used to build the following apps that are useful when applied to real-world use cases and workloads:

1. Text generation: Apps built with Amazon Bedrock can generate original written text in various forms, such as short stories, blog posts, news articles and social media posts.
2. Conversational AI: Customized chatbots or virtual assistants built using Bedrock are based on foundation models having access to proprietary data owned by a developer or software vendor. This provides good conversational AI responses to users' queries.
3. Text summarization: A simple Bedrock app offers the capability to summarize text without forcing a user to pore over lengthy documents or materials.
4. Image generation: Bedrock's API can interface with various types of foundation models, including those with text-to-speech AI capabilities. Given that, an app built on Bedrock can take a request or prompt for a specific image from a user and generate that image.
