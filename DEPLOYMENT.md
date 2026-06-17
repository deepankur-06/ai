# Deployment Guide - Share Your Chatbot with Family

## Quick Start

### 1. **Local Computer (Easiest)**

```bash
# Clone the repository
git clone https://github.com/deepankur-06/ai.git
cd ai

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
streamlit run app.py
```

The chatbot opens at `http://localhost:8501`

---

## Sharing Options

### **Option 1: Streamlit Cloud (Recommended) ⭐**

**Best for:** Sharing publicly, easiest deployment

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "Deploy an app"
5. Select your repository and branch
6. Share the public link with family!

**Pros:**
- Free hosting
- Automatic updates
- Easy to share
- No server management

---

### **Option 2: Local Network Share**

**Best for:** Family members on same WiFi

1. Run the chatbot on your machine:
```bash
streamlit run app.py
```

2. Find your local IP:
   - **Windows:** `ipconfig` → IPv4 Address
   - **Mac/Linux:** `ifconfig` → inet

3. Share the link: `http://<YOUR_IP>:8501` with family members on same network

---

### **Option 3: Heroku Deployment**

**Best for:** Always-on hosting

1. Install Heroku CLI
2. Create `Procfile`:
```
web: streamlit run --server.port=$PORT app.py
```

3. Deploy:
```bash
heroku login
heroku create your-chatbot-name
git push heroku main
```

---

### **Option 4: Google Colab**

**Best for:** Quick sharing, no installation needed

1. Upload to Colab
2. Install requirements: `!pip install -r requirements.txt`
3. Run: `!streamlit run app.py`
4. Use the public link to share

---

## Customization for Family

### Add Family Members' Names

Edit `utils/config.py`:

```python
FAMILY_MEMBERS = ["Mom", "Dad", "Sister", "Brother"]
```

### Add Custom Responses

Edit `utils/config.py` and add new intents:

```python
"family_greeting": {
    "patterns": ["how is mom", "how is dad"],
    "responses": ["They're wonderful!", "Great! How are they?"]
}
```

### Add Family Photos

1. Create `assets/` folder
2. Add photos
3. Update `app.py` to display them

---

## Troubleshooting

### Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### Dependencies Not Installing
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Connection Issues
- Check firewall settings
- Ensure both devices on same network
- Disable VPN if needed

---

## Next Steps

1. ✅ Get feedback from family
2. 🎯 Add more intents based on requests
3. 📚 Train on custom family conversations
4. 🎨 Customize the UI with family colors/photos
5. 🚀 Deploy to production

---

**Enjoy sharing with your family! 👨‍👩‍👧‍👦**
