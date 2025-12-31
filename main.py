
# -*- coding: utf-8 -*-
import os
import torch
import soundfile as sf
import gradio as gr
from huggingface_hub import login
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer

# Login using environment variable
token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError("HF_TOKEN environment variable not set")

login(token=token)

device = "cuda" if torch.cuda.is_available() else "cpu"

model = ParlerTTSForConditionalGeneration.from_pretrained(
    "ai4bharat/indic-parler-tts"
).to(device)

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-parler-tts")

voice_styles = {
    "Tamil - Female": "A female speaker delivering expressive Tamil speech.",
    "Tamil - Male": "A male speaker delivering formal Tamil speech.",
    "English - Male (Indian Accent)": "A male speaker with an Indian accent speaks clearly.",
    "English - Female (Indian Accent)": "A female speaker with an Indian accent speaks warmly."
}

def generate_voice(text, voice):
    description = voice_styles[voice]
    inputs = tokenizer(description, return_tensors="pt").to(device)
    prompt = tokenizer(text, return_tensors="pt").to(device)
    audio = model.generate(
        input_ids=inputs.input_ids,
        prompt_input_ids=prompt.input_ids
    ).cpu().numpy().squeeze()
    output = "output.wav"
    sf.write(output, audio, model.config.sampling_rate)
    return output

with gr.Blocks(title="AI4Bharat TTS") as app:
    gr.Markdown("# 🎤 AI4Bharat Text-to-Speech")
    text = gr.Textbox(label="Text")
    voice = gr.Dropdown(list(voice_styles.keys()), value="Tamil - Female")
    btn = gr.Button("Generate")
    audio = gr.Audio(type="filepath")
    btn.click(generate_voice, [text, voice], audio)

app.launch()
