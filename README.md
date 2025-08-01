# LangChain + Groq API Based Movie Search Agent

This project demonstrates how to build a conversational AI agent that can perform real-time web searches using LangChain, Groq API, and Tavily Search. The agent can fetch recent movie releases and provide summarized answers by leveraging external search tools.

---

## Features

- Integrates Groq's `ChatGroq` model for conversational AI.
- Uses `TavilySearchResults` tool to perform live web searches.
- Implements a React-style agent executor to orchestrate chat and search tools.
- Handles API key management with `.env` configuration.
- Gracefully falls back to direct search if agent tool usage fails.
- Provides clean, summarized responses combining multiple search results.

---

## Setup Instructions

### Prerequisites

- Python 3.10+  
- API keys for:
  - **Groq API**  
  - **Tavily API**

### Install Dependencies

```bash

1. conda create -n llmapp python=3.11 -y 

2. conda activate llmapp 

3. pip install -r requirements.txt



🚀 Make sure your requirements.txt contains:

langchain==0.3.7
langchain-groq==0.2.1
python-dotenv==1.0.1
langgraph>=0.2.0
langchain-community


🚀 Environment Variables

Create a .env file in your project root with the following:

GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here


😁 Error Handling & Fallback
If the agent fails due to model deprecation or tool call issues, the code falls back to performing a direct search using TavilySearchResults and prints raw search results.


🤞 Notes
-The Groq llama-3.1-70b-versatile model is deprecated. Use current supported models like gpt-4o-mini.
-Ensure your API keys are valid and have required permissions.
-Adjust max_results for the search tool to get more or fewer results.
-You can extend this agent for other search queries or integrate with UI apps.

🎊Contributing
Contributions to this project are welcome! Whether it's bug reports, feature requests, or improvements to the code or documentation, feel free to open an issue or submit a pull request.
🌀Please follow these guidelines:

-Fork the repository and create your branch from main.
-Write clear, concise commit messages.
-Test your changes before submitting.
-Respect the existing code style.
-Include documentation updates if relevant.


😎 Contact
Created by Susmay Das
susmoydas1000@gmail.com
