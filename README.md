
# AI4Bharat Tamil & English Text-to-Speech

This project demonstrates how to generate Tamil and English speech using **ai4bharat/indic-parler-tts**.

---

## 🔑 Step 1: Create a Hugging Face API Token

1. Go to https://huggingface.co
2. Sign in or create an account
3. Click your profile → **Settings**
4. Open **Access Tokens**
5. Click **New token**
6. Name it (e.g., `tts-project`)
7. Select **Read** permission
8. Copy the token

⚠️ **Never hardcode your token in code**  
Use environment variables instead.

---

## 🛠 Step 2: Set API Token

### Linux / macOS
```bash
export HF_TOKEN=your_token_here
```

### Windows (PowerShell)
```powershell
setx HF_TOKEN "your_token_here"
```

---

## 📦 Step 3: Install Dependencies

```bash
pip install torch soundfile pydub gradio git-lfs
pip install git+https://github.com/huggingface/parler-tts.git
git clone https://github.com/descriptinc/audiotools.git
pip install ./audiotools
```

---

## ▶️ Step 4: Run the Program

```bash
python main.py
```

A Gradio web interface will open in your browser.

---

## 📁 Project Structure

```
.
├── main.py
├── README.md
```

---

## 🚀 Features

- Tamil & English TTS
- Multiple voice styles
- Web-based UI (Gradio)

---

## ❌ Security Notice

❌ Do NOT upload API keys to GitHub  
✅ Use environment variables only
