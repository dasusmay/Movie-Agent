import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

# Environment setup
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

# Use a better model that handles tools properly
# chatModel = ChatGroq(
#     model="llama-3.1-70b-versatile",
#     temperature=0
# )

chatModel = ChatGroq(
    model="llama3-8b-8192",
    temperature=0
)


# Create search tool 
search = TavilySearchResults(max_results=3)

tools = [search]

# Create agent
agent_executor = create_react_agent(chatModel, tools)

# Simple and direct approach
try:
    print("Searching for recent movies in 2025...")
    response = agent_executor.invoke({
        "messages": [HumanMessage(content="Search for recent movies released in 2025")]
    })
    
    print("\n" + "="*60)
    print("AGENT RESPONSE:")
    print("="*60)
    
    # Print the final response
    for message in response['messages']:
        if hasattr(message, 'content') and message.content:
            print(f"\n{message.__class__.__name__}:")
            print(message.content)
    
except Exception as e:
    print(f"Agent failed with error: {e}")
    print("\nUsing direct search instead...")
    
    # Fallback to direct search
    try:
        results = search.invoke("2025 new movies recent releases")
        print("\nDirect Search Results:")
        print("-" * 40)
        
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result.get('title', 'No Title')}")
            print(f"Content: {result.get('content', 'No content')[:200]}...")
            print(f"URL: {result.get('url', 'No URL')}")
            
    except Exception as search_error:
        print(f"Direct search also failed: {search_error}")
        print("Please check your TAVILY_API_KEY")