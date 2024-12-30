import os
from langchain.agents import Tool
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
import streamlit as st

# Set API Keys
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "52a6da1d0c9d966c1e2f1dc8fd6d4846d6ffe591d9efe33e40cee0cabbb6fecf"  # Alternatively, load from .env

# Research Agent using SerpAPI
def research_agent(query):
    search = SerpAPIWrapper()
    return search.run(query)

# Use Case Generation Agent
def use_case_agent(industry_insights):
    llm = OpenAI(temperature=0.7)
    prompt = f"""
    Based on the following industry insights, generate 5 relevant AI/GenAI use cases:
    {industry_insights}
    """
    return llm(prompt)

# Streamlit App
st.title("Multi-Agent System for AI Use Case Generation")

company_or_industry = st.text_input("Enter a Company or Industry for Research")
if st.button("Generate Proposal"):
    st.write("Conducting research...")
    research = research_agent(company_or_industry)
    st.write(research)

