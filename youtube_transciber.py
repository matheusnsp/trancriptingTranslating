import yt_dlp
import whisper
import os
import textwrap
from googletrans import Translator

def download_audio(youtube_url, output_folder="downloads"):
    """Downloads audio from a YouTube video."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        audio_file = f"{output_folder}/{info['id']}.mp3"
        return audio_file

def transcribe_audio(audio_path):
    """Transcribes audio using Whisper."""
    model = whisper.load_model("small")  # Change to "medium" or "large" for better accuracy
    result = model.transcribe(audio_path)
    return result["text"]

def translate_text(text, target_lang="pt"):
    """Translates text to Portuguese using Google Translate."""
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

def format_transcript(text, width=80):
    """Formats the transcript for better readability."""
    paragraphs = text.split('. ')
    formatted_text = "\n\n".join(textwrap.fill(p, width=width) for p in paragraphs)
    return formatted_text

def save_transcript(text, filename):
    """Saves transcript to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    youtube_url = input("Enter YouTube video URL: ")
    print("\n🔄 Downloading audio...")
    audio_file = download_audio(youtube_url)

    print("\n📝 Transcribing original language...")
    original_transcript = transcribe_audio(audio_file)

    print("\n🌍 Translating to Portuguese...")
    translated_transcript = translate_text(original_transcript, "pt")

    print("\n🖋 Formatting transcripts...")
    formatted_original = format_transcript(original_transcript)
    formatted_translated = format_transcript(translated_transcript)

    print("\n--- 📜 TRANSCRIPTION (Original Language) ---\n")
    print(formatted_original)

    print("\n--- 🌎 TRADUÇÃO (Português) ---\n")
    print(formatted_translated)

    save_transcript(formatted_original, "transcript_original.txt")
    save_transcript(formatted_translated, "transcript_pt.txt")

    print("\n✅ Transcripts saved as 'transcript_original.txt' and 'transcript_pt.txt'")

if __name__ == "__main__":
    main()
