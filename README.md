# codealpha_banking_faq_chatbot
# Banking FAQ Chatbot

A Python-based Banking FAQ Chatbot developed as part of the CodeAlpha AI Internship – Task 2.

## Project Overview

This chatbot answers common banking-related questions using NLP-based text preprocessing and similarity matching.

The chatbot compares the user's question with a collection of frequently asked banking questions and provides the most relevant answer.

## Features

- Banking FAQ question answering
- Text preprocessing
- Similarity-based question matching
- Interactive chat interface
- Send button
- Clear Chat button
- Works offline after installation

## Technologies Used

- Python
- Tkinter
- NLTK
- SequenceMatcher
- Regular Expressions

## How It Works

1. User enters a banking question.
2. The chatbot cleans and preprocesses the text.
3. The question is compared with stored FAQ questions.
4. The most similar question is selected.
5. The corresponding answer is displayed.

## Example Questions

- How do I check my bank balance?
- I lost my ATM card
- What is UPI?
- How can I send money?
- My transaction failed
- I forgot my ATM PIN

## How to Run

Install the required library:

```bash
pip install nltk