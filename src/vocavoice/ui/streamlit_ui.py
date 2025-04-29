import streamlit as st
from vocavoice.ui_vocavoice import run_vocavoice

# Streamlit page setup
st.set_page_config(
    page_title="Vocabulary Podcast Creator",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
with st.sidebar:
    

    st.title("🎯 Settings")
    st.markdown("Customize your podcast content below:")

    language = st.selectbox("🌐 Language:", ["English", "Spanish", "French", "German", "Turkish"])

    preset_topics = ["Technology", "Travel", "Daily Life", "Education", "Space", "Food", "Relationships"]
    selected_topic = st.selectbox("📚 Topic:", options=preset_topics + ["Custom"])

    if selected_topic == "Custom":
        topic = st.text_input("Enter your own topic:", placeholder="e.g., Sustainable Energy")
    else:
        topic = selected_topic

    vocabulary_input = st.text_area("✏️ Vocabulary words (comma separated):", placeholder="e.g., algorithm, neural, data, intelligence")

    language_level = st.selectbox("📈 Language Level:", ["A2", "B1", "B2", "C1"])

    voice_style = st.selectbox("🎙️ Voice Style:", ["friendly", "serious", "excited"])

    llm_model = st.selectbox("💬 Choose LLM Model:", options=["gpt-4o-mini"])

    tts_model = st.selectbox("🎙️ Choose TTS Model:", options=["gpt-4o-mini-tts", "tts-1", "tts-1-hd"])

    tts_voice = st.selectbox("🎤 Choose TTS Voice:", options=["alloy", "ash", "ballad", "coral", "echo", "fable", "nova", "onyx", "sage", "shimmer"])

    api_key = st.text_input("Enter your OpenAI API Key", type="password", placeholder="Enter your OpenAI API Key here")

    start_button = st.button("🚀 Create My Podcast")

# --- Main Content with Columns ---
col1, col2 = st.columns([3, 1])  # Sol daha küçük, sağ daha büyük

with col1:
    st.title("🎙️ Vocabulary-Based Podcast Creator")
    st.markdown("""
    Welcome! This tool will help you create a mini podcast using the vocabulary words you've learned today.  
    It will generate a script and audio for you automatically. Practice makes perfect! 🚀
    """)
    
with col2:
    st.markdown("### 🙋‍♂️ About the Creator")
    st.markdown("""
    Created with ❤️ by **Serkan Yaşar**  
    🔗 [LinkedIn](https://www.linkedin.com/in/serkanyasar)  
    💼 [GitHub](https://github.com/serkanyasr)  
    🌐 [Website](https://www.serkanyasar.dev)  
    """)    
st.markdown("---")


# --- Crew Start ---
if start_button:
    if not topic or not vocabulary_input or not llm_model or not api_key:
        st.error("❗ Please provide all necessary information: topic, vocabulary words, LLM Model, and API Key!")
    else:
        vocabulary_list = [word.strip() for word in vocabulary_input.split(",") if word.strip()]

        with st.spinner("Generating your podcast... 🎧.This may take up to 1 minute. Please hang tight!"):
            results = run_vocavoice(
                language=language,
                topic=topic,
                vocabulary_list=vocabulary_list,
                language_level=language_level,
                voice_style=voice_style,
                llm_model=llm_model,
                tts_model=tts_model,
                tts_voice=tts_voice,
                api_key=api_key
            )


            st.success("✅ Your podcast is ready!")
            st.write(results)
            # Show script
            st.write("### 📝 Generated Script")

            try:
                with open(results["script_file_full_path"], "r") as f:
                    script_content = f.read()
                st.text(script_content)
            except:
                st.error("script_file_full_path not found")
                
            try:
                # Show audio
                st.write("### 🔊 Listen to Your Podcast")
                with open(results["audio_file_full_path"], "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3")
            except:
                st.error("audio_file_full_path")
