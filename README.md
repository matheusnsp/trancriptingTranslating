# YouTube Video Transcriber & Translator

## 📌 Description
This Python script downloads the audio from a YouTube video, transcribes it using OpenAI's Whisper, and translates the transcript into Portuguese using Google Translate. 
The formatted transcripts are displayed in the terminal and saved as text files.

## 🚀 Features
- **Downloads audio from YouTube videos** using `yt-dlp`
- **Transcribes the original language** using `whisper`
- **Translates to Portuguese** using `googletrans`
- **Formats transcripts for better readability**
- **Saves transcripts as text files** (`transcript_original.txt` & `transcript_pt.txt`)

## 🛠️ Requirements
Make sure you have the following dependencies installed:

```sh
pip install yt-dlp openai-whisper googletrans==4.0.0-rc1
```

## 📜 Usage
1. **Run the script:**
   ```sh
   python script.py
   ```
2. **Enter the YouTube video URL** when prompted.
3. **Wait for the transcription and translation to complete.**
4. **Check the output in the terminal and text files.**

## 📂 Output
- **transcript_original.txt** → Contains the transcript in the original language
- **transcript_pt.txt** → Contains the translated transcript in Portuguese

## 🔧 Configuration
- You can change the Whisper model in `whisper.load_model("small")` to `medium` or `large` for better accuracy.
- Modify the `translate_text` function to support different languages if needed.

## ⚡ Example Output
```
--- 📜 TRANSCRIPTION (Original Language) ---

This is the first part of the video, where the speaker introduces the topic.

In the next section, they discuss the impact of technology on modern life.
Many experts believe that artificial intelligence will revolutionize various
industries.

--- 🌎 TRADUÇÃO (Português) ---

Esta é a primeira parte do vídeo, onde o palestrante introduz o tema.

Na próxima seção, eles discutem o impacto da tecnologia na vida moderna.
Muitos especialistas acreditam que a inteligência artificial revolucionará
diversas indústrias.

✅ Transcripts saved as 'transcript_original.txt' and 'transcript_pt.txt'
```

## 📢 Notes
- **Make sure you have an internet connection** for translation.
- **Processing time depends on the video length** and the Whisper model used.
- **Whisper only supports non-English to English translation natively**, so Google Translate is used for English to Portuguese conversion.
