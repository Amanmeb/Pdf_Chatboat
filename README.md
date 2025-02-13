# 📄 PDF Chatbot with RAG (Retrieval-Augmented Generation)
A **Streamlit-powered chatbot** that allows users to ask questions about PDF files using **offline AI retrieval**.

## 🚀 Features
✅ **Offline Functionality** – No internet required after setup.  
✅ **PDF Content Extraction** – Reads & processes PDF text.  
✅ **AI-Powered Retrieval** – Uses `all-MiniLM-L6-v2` for semantic search.  
✅ **Optional LLM Generation** – Can use GPT/Llama for response generation.  
✅ **User-Friendly UI** – Built with Streamlit.  

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Amanmeb/Pdf_Chatboat.git
cd Pdf_Chatboat
2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Download Model for Offline Use

Run once to save the AI model locally:

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
model.save('models/all-MiniLM-L6-v2')

4️⃣ Run the Chatbot

streamlit run pdf_chat_ui.py
