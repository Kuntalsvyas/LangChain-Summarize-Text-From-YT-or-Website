import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from dotenv import load_dotenv
import traceback

load_dotenv()
#streamlit app 
st.set_page_config(page_title="LangChain:Summarize Text From YT or Website",page_icon="🐦")
st.title("🐦 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')



#Get the Groq API key and url(YT or Website) field to summarized 
with st.sidebar:
    groq_api_key=st.text_input("GROQ API Key",value="",type="password")
    
generic_url=st.text_input("URL",label_visibility="collapsed")

#Gemma model using Groq API
llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key.strip())

prompt_template = """
Summarize the following content in approximately 300 words.
Content: {text}
"""

prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    #validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the GROQ API key and a URL to summarize.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video URL or a website URL.")
    
    else:
        try:
            with st.spinner("Waiting..."):
                #Loading the website or YT video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 header={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()
                
                #Chain For Summarization 
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)
                
                st.success("Summary generated:")
                st.write(output_summary)

        except Exception:
            tb = traceback.format_exc()
            st.error("An error occurred; full details below.")
            st.code(tb)
                