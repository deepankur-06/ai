# 🤖 Family AI Chatbot

A friendly AI chatbot built with Natural Language Processing (NLP) that you can share with your family!

## Features
- 💬 Understands and responds to natural language queries
- 🎯 Intent recognition and entity extraction
- 📚 Learn from conversations
- 🌐 Web interface for easy interaction
- 🚀 Ready to deploy and share

## Tech Stack
- **NLP**: Hugging Face Transformers, NLTK
- **Model**: DistilBERT + Seq2Seq architecture
- **Web**: Streamlit (easy to share)
- **Backend**: Python

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/deepankur-06/ai.git
cd ai
pip install -r requirements.txt
```

### Run the Chatbot

```bash
streamlit run app.py
```

The chatbot will open in your browser at `http://localhost:8501`

## Project Structure

```
ai/
├── README.md
├── requirements.txt
├── app.py                    # Main Streamlit app
├── data/
│   ├── intents.json         # Intent patterns and responses
│   └── faq.json             # FAQ database
├── models/
│   ├── intent_classifier.py # Intent classification
│   ├── response_generator.py# Response generation
│   └── tokenizer.py         # Text tokenization
├── notebooks/
│   └── training.ipynb       # Training notebook
└── utils/
    ├── preprocessing.py     # Text preprocessing
    └── config.py           # Configuration
```

## How It Works

1. **User Input** → Text preprocessing
2. **Intent Recognition** → Classify user intent
3. **Entity Extraction** → Extract key information
4. **Response Generation** → Generate appropriate response
5. **Display** → Show response to user

## Training Data

The chatbot is trained on:
- Common FAQ patterns
- Family-friendly conversations
- Helpful information queries

## Deployment

### Share with Family

**Option 1: Streamlit Cloud (Recommended)**
- Free and easy to share
- Deploy with: `streamlit run app.py`
- Share link with family

**Option 2: Heroku**
- Traditional web hosting
- More customizable

**Option 3: Local Network**
- Run on your machine
- Share within home network

## Future Enhancements
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Persistent memory
- [ ] Custom training data
- [ ] Emoji support
- [ ] User preferences

## License
MIT

## Support
For issues or suggestions, open an issue on GitHub!

---

**Made with ❤️ for family**
