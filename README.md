# 📄 PDF Chatbot with RAG (Retrieval-Augmented Generation)

A **Streamlit-powered chatbot** that allows users to ask questions about PDF files using **offline AI retrieval** with **voice-to-text and text-to-voice features** for better accessibility.

## 🚀 Features

✅ **Offline Functionality** – No internet required after setup.  
✅ **PDF Content Extraction** – Reads & processes PDF text.  
✅ **AI-Powered Retrieval** – Uses `all-MiniLM-L6-v2` for semantic search.  
✅ **Voice-to-Text Input** – Users can ask questions via speech.  
✅ **Text-to-Speech Responses** – Chatbot reads responses aloud for accessibility.  
✅ **Optional LLM Generation** – Can use GPT/Llama for response generation.  
✅ **User-Friendly UI** – Built with **Streamlit**.  

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Amanmeb/Pdf_Chatboat.git
cd Pdf_Chatboat
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Download Model for Offline Use**
Run once to save the AI model locally:
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
model.save('models/all-MiniLM-L6-v2')
```

### **4️⃣ Run the Chatbot**
```sh
streamlit run pdf_chat_ui.py
```

---


```

---

## 🔧 Technologies Used
- **Python 3.8+**
- **Streamlit** – UI framework  
- **PyPDF** – PDF text extraction  
- **Sentence Transformers** – AI model for retrieval  
- **SpeechRecognition** – Convert speech to text  
- **pyttsx3** – Convert text to speech  
- **Torch** – Machine learning backend  

---


---

## 👨‍💻 Author
🔹 **Amanuel Mebratu**  
🔹 GitHub: [Amanmeb](https://github.com/Amanmeb)  
🔹 Email: amanzia7@gmail.com  

