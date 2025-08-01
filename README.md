# 📝 LangChain Summarizer: YouTube & Web URL Text Summarization
This project leverages LangChain, LLMs, and Streamlit to summarize content from YouTube videos or website URLs. It's a powerful tool for quickly understanding long-form content by extracting core insights using LLMs.

---

# 📊 Problem Statement
In today’s digital world, individuals are overloaded with information from long YouTube videos, articles, and web pages. Manually going through this content consumes valuable time and often leads to missing key points.

**There is a need for an AI-driven summarization tool that can:**

- Condense lengthy videos and articles into short, meaningful summaries.
- Save time for students, professionals, and researchers.
- Improve knowledge consumption by presenting only the most relevant information.
  
This project addresses the challenge by integrating LangChain with LLMs to generate concise, accurate, and context-aware summaries directly from URLs.

---

# 📌 Features
- 🔗 Summarize YouTube Videos by providing the video link.
- 🌐 Summarize Website Content from any URL.
- 🧠 Powered by LangChain and OpenAI/GPT-based LLMs.
- ⚡ Fast and intuitive Streamlit frontend for easy interaction.
- 📎 Copy or download the summarized output.

---

# 🧰 Tech Stack

- LangChain
- OpenAI
- Streamlit
- Python-dotenv
- Streamlit

---

# 🧪 How It Works

**🔍 YouTube Summarization:**

- Extracts transcript using YoutubeLoader.
- Converts transcript to chunks.
- Feeds chunks to LLM using LangChain summarization chain.

**🌍 Website Summarization:**

- Loads page text via UnstructuredURLLoader.
- Similar chunking and summarization pipeline is applied.

---

# ⚙️ Setup Instructions

***1. Clone the Repository**

- git clone https://github.com/Kuntalsvyas/LangChain-Summarize-Text-From-YT-or-Website.git
- cd LangChain-Summarize-Text-From-YT-or-Website

**2. Create Virtual Environment (Optional but recommended)**
  
- python -m venv venv
- source venv/bin/activate  # On Windows use: venv\Scripts\activate

**3. Install Dependencies**
- pip install -r requirements.txt

**4.🚀 Run the App**
- streamlit run app.py

---

# 📊 Results
The summarizer produces concise, structured summaries that capture the main ideas and insights of long-form content.

- YouTube Videos: A 20-minute video can be condensed into a 2–3 paragraph summary highlighting the core message, key statistics, and examples.
- Web Pages: Lengthy articles are reduced into bullet-point style takeaways for quicker reading.
- Accuracy: Summaries are context-aware, preserving the intent of the original content without losing important details.

This makes it highly valuable for students, researchers, analysts, and professionals who want to save time while still extracting maximum knowledge.

---

# 🔮 Future Enhancements

- 🗂️ Add history panel to view and revisit past summaries.
- 🗣️ Support for multilingual summarization (e.g., Hindi, Spanish).
- 📱 Mobile-optimized Streamlit interface for better UX on smaller screens.
- 📤 Export to PDF/Markdown for downloadable summaries.
- 🔧 Adjustable summarization length (brief, medium, detailed).
- 🔍 Highlight key points and quotes from source text.
- 🔁 Batch summarization for multiple URLs/videos in one go.
- 🔐 User authentication and personal summary storage.

---

# 🙌 Author
Built by Kuntal Vyas If you found this useful, ⭐ the repo and share!
