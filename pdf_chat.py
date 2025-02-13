import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util
import re

class EnhancedPDFChatbot:
    def __init__(self, pdf_path):
        self.pdf_text = self._extract_text(pdf_path)
        self.sentences = self._remove_duplicates(self._split_into_sentences(self.pdf_text))
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Load model locally

    def _extract_text(self, pdf_path):
        """Extract text from PDF file"""
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
        return text.strip()

    def _split_into_sentences(self, text):
        """Split text into sentences with improved regex"""
        text = re.sub(r'\s+', ' ', text.replace('\n', ' ').replace('\r', ' '))
        sentences = re.split(r'(?<!\b\w\.\w)(?<!\b[A-Z]\.)(?<!\s[a-z]\.)[.!?]\s', text)
        return [s.strip() for s in sentences if len(s.strip()) > 10]

    def _remove_duplicates(self, sentences):
        """Remove near-duplicate sentences"""
        return list(set(sentences))

    def _calculate_similarity(self, text1, text2):
        """Calculate semantic similarity using sentence embeddings"""
        embeddings1 = self.model.encode([text1], convert_to_tensor=True)
        embeddings2 = self.model.encode([text2], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
        return similarity.item()

    def get_response(self, question, num_responses=3):
        """Get response for user question"""
        similarities = []
        for i, sentence in enumerate(self.sentences):
            score = self._calculate_similarity(question, sentence)
            similarities.append((score, sentence, i))
        
        similarities.sort(reverse=True, key=lambda x: x[0])
        top_responses = similarities[:num_responses]
        organized_answers = self._organize_answers(top_responses)
        return organized_answers

    def _organize_answers(self, top_responses):
        """Organize answers into a coherent response"""
        organized = []
        for score, sentence, index in top_responses:
            context = self._get_context(index)
            response = {
                'answer': sentence,
                'similarity': score,
                'context': context
            }
            organized.append(response)
        return organized

    def _get_context(self, index):
        """Get surrounding sentences for context"""
        context = []
        if index > 0:
            context.append(self.sentences[index - 1])
        context.append(self.sentences[index])
        if index < len(self.sentences) - 1:
            context.append(self.sentences[index + 1])
        return " ".join(context)

# Streamlit UI
st.set_page_config(layout="wide")  # Set layout to wide

col1, col2 = st.columns([1, 3])

with col1:
    st.title("📄 PDF Chatbot")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    chatbot = EnhancedPDFChatbot("temp.pdf")
    st.success("✅ PDF processed successfully!")

with col2:
    chat_container = st.container()
    with chat_container:
        st.subheader("📝 Chat History:")
        for question, answer in st.session_state.chat_history:
            st.write(f"**You:** {question}")
            st.write(f"{answer}")

    user_input = st.text_input("Ask something about the PDF:", key="chat_input")
    if user_input:
        responses = chatbot.get_response(user_input)
        if responses:
            response_text = "\n".join([f"📌 {r['answer']}\n💡 Context: {r['context']}" for r in responses])
            st.session_state.chat_history.append((user_input, response_text))
            st.rerun()
