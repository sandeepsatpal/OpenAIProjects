# AI/OpenAI/Azure OpenAI Sample codebase

In an era defined by intelligent systems and data-driven decisions, OpenAI's technologies offer a transformative lens. This project explores sample code for the most required methods to integrate AI models for your websites. In this projects, you can find sample modules on, how to integrate your code with OpenAI APIs. 
Apart from itnegration, you can also explore fine tuning and RAG approach to customize AI for your own requirements and data. 
This projects gives you glimpse of all the state of the art and latest methodologies utilizing OpenAI (like openAI, Azure AI foundary, open source Langchain).

<h2>🤖 Quick Comparison: OpenAI API vs Azure OpenAI vs LangChain Framework</h2>
<table border="1" cellpadding="10" cellspacing="0">
  <thead>
    <tr>
      <th>Feature</th>
      <th>OpenAI API</th>
      <th>Azure OpenAI</th>
      <th>LangChain Framework</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Access</strong></td>
      <td>Direct access via OpenAI's REST API</td>
      <td>Access via Azure portal with enterprise integration</td>
      <td>Uses OpenAI or other LLMs via wrappers</td>
    </tr>
    <tr>
      <td><strong>Cost</strong></td>
      <td>Pay-per-token pricing from OpenAI</td>
      <td>Azure pricing + OpenAI usage</td>
      <td>LangChain is free; costs depend on underlying LLM (e.g., OpenAI)</td>
    </tr>
    <tr>
      <td><strong>Security & Compliance</strong></td>
      <td>Standard API key security</td>
      <td>Enterprise-grade security (AAD, GDPR, HIPAA)</td>
      <td>Depends on hosting and LLM provider; less built-in compliance</td>
    </tr>
    <tr>
      <td><strong>Ease of Use</strong></td>
      <td>Simple and direct for basic tasks</td>
      <td>Requires Azure setup; Azure AI Foundary is simple to use</td>
      <td>Higher-level abstractions for chaining, memory, agents</td>
    </tr>
    <tr>
      <td><strong>Best For</strong></td>
      <td>Simple apps, direct API usage</td>
      <td>Enterprise apps with compliance needs</td>
      <td>Complex workflows, multi-step reasoning, RAG pipelines</td>
    </tr>
  </tbody>
</table>

<h2> Below few python and javascript modules are sample demostration of the use case of OpenAI as per different requirements</h2>

<ul>
  <li> <b> Access OpenAI model in Javascript </b> </li>
  <table>
    <tr>
      <td>
One of the most common uses of OpenAI is powering chat assistants on websites. Many platforms rely on OpenAI models to deliver intelligent, conversational support to users. The sample JavaScript code below can be easily integrated into your custom chat interface to enable seamless OpenAI-powered interactions.
      </td>
      </tr>
    <tr>
      <td>
        <i>AzureOpenAIInJavascript.html</i>
      </td>
    </tr>
  </table>
  <li> <b> Access OpenAI model in Python </b> </li>
  <table>
    <tr>
      <td>
Python offers one of the most seamless ways to interact with OpenAI’s powerful language models. With the official OpenAI Python library, developers can easily integrate capabilities like text generation, summarization, and code assistance into their applications. The SDK handles authentication, request formatting, and response parsing, making it ideal for rapid prototyping and production-ready AI features. Whether you're building a chatbot, automating content creation, or enhancing data workflows, Python provides the flexibility and simplicity to unlock OpenAI’s full potential.
        Below Python code demostrate how to integrate OpenAI model for Chat scenario
      </td>
      </tr>
    <tr>
      <td>
        <i>AzureOpenAISamplecode.py</i>
      </td>
    </tr>
  </table>
  <li> <b> Access Azure OpenAI model using LangChain framework in Python </b> </li>
  <table>
    <tr>
      <td>
LangChain provides robust support for integrating Azure-hosted GPT models, enabling developers to harness the power of OpenAI’s language models within Microsoft’s secure cloud infrastructure. By leveraging the langchain-azure-ai extension, users can seamlessly connect to Azure OpenAI endpoints and deploy models like GPT-3.5 and GPT-4 for chat completions, embeddings, and more.
        Below Python code demostrate how to use Azure GPT model using Langchain APIs
      </td>
      </tr>
    <tr>
      <td>
        <i>AzureOpenAIThroughLangChainSample.py</i>
      </td>
    </tr>
  </table>
  <li> <b> Customize Chat GPT model on your Private data/websites using RAG approach </b> </li>
  <table>
    <tr>
      <td>
        Cutomizing Chat GPT model for your private data/websites is one of the most popular requirements many companies are looking for. </br>
        You can unlock the full potential of conversational AI by customizing ChatGPT with your private data and website content using the Retrieval-Augmented Generation (RAG) approach. </br>  
        Retrieval-Augmented Generation (RAG) is a powerful framework that enhances the capabilities of language models by integrating external knowledge retrieval into the generation process. Instead of relying solely on pre-trained data, RAG dynamically fetches relevant documents from internal or external sources and incorporates them into the model’s prompt. This approach enables more accurate, context-aware, and up-to-date responses. </br>
        To build end to end chat solution on your private data in Azure infrastructure, you need to follow two major steps
      </td>
      </tr>
    <tr>
      <td>
        <b> Step 1: Design and Build Azure AI Search Index </b>
      </td>
    </tr>
    <tr>
      <td>
        In Azure AI Foundary, you can add the data source using different methods. One of the easiest method is to create a storage blob container, upload all the files and connect it with Azure search service. </br>
        Once search service is ready, you can create search index on top of it and add it as a data source in the GPT model.
      </td>
    </tr>
    <tr>
      <td>
        <b> Step 2: Integrate with Chat Model </b>
      </td>
    </tr>
    <tr>
      <td>
        Below python module demostrate how to integrate chat GPT model which uses azure search index to customize the response on your content. </br>
        Major difference in standard approach and this approach is, you need to provide search_endpoint, search_key and search_index as well.
      </td>
    </tr>
    <tr>
      <td>
        <i> AzureOpenAIRAGForPrivateData.py </i>
      </td>
    </tr>
  </table>
  <li> <b> Miscellaneous Python modules related to GPT models </b> </li>
  <table>
    <tr>
      <td>
        <b> Create JSONL chunks data from big files </b> </br>
        To user your private data either for RAG or for fine-tuning GPT model, you need to divide your entire data into chunks. </br>
        Although, Azure AI index can automatically chunks your data, sometimes you would like to divide on your own. </br>
        Below python modules can take a file and split it into chunks and convert them into JSONL format which is needed by GPT models.
      </td>
      </tr>
    <tr>
      <td>
        <i>CreateJsonLFromDocument.py</i>
      </td>
    </tr>
  </table>
  <table>
    <tr>
      <td>
        <b> Upload Training and Validataion JSONL files to Azure AI Foundary </b> </br>
        Once your training and validation JSONL files are ready, you can either upload them via Azure AI foundary portal, or use below python module to upload them. 
      </td>
      </tr>
    <tr>
      <td>
        <i>UploadJsonLForFineTuning.py</i>
      </td>
    </tr>
  </table>
    <table>
    <tr>
      <td>
        <b> Fine tune GPT models on your data </b> </br>
        Although, RAG is the most suited method to create chat assistant on your own data, fine tuning is another method where you update the GPT model itself on your data. </br>
        Below python module can train and fine-tune existing GPT models on you training and validation set. </br>
        Fine-tuning is a longer process. Same module can also be used to check the status of fine-tuning. 
      </td>
      </tr>
    <tr>
      <td>
        <i>FineTuningAzureOpenAI.py</i>
      </td>
    </tr>
  </table>
</ul>
