import tkinter as tk
from tkinter import scrolledtext
import re
from difflib import SequenceMatcher


# Banking FAQs
faqs = [
    {
        "question": "How can I open a bank account?",
        "answer": "You can open a bank account by visiting a bank branch or using the bank's official online account-opening service."
    },
    {
        "question": "How can I check my bank balance?",
        "answer": "You can check your balance using mobile banking, internet banking, an ATM, or by visiting your bank."
    },
    {
        "question": "How can I reset my ATM PIN?",
        "answer": "You can usually reset your ATM PIN through your bank's ATM, mobile banking app, or internet banking service."
    },
    {
        "question": "What should I do if my ATM card is lost?",
        "answer": "Immediately block your card using your bank's official app, helpline, or branch to prevent unauthorized use."
    },
    {
        "question": "How can I transfer money?",
        "answer": "You can transfer money using UPI, NEFT, RTGS, IMPS, or your bank's mobile/internet banking service."
    },
    {
        "question": "What is UPI?",
        "answer": "UPI is a digital payment system that allows you to send and receive money directly between bank accounts."
    },
    {
        "question": "How can I update my mobile number?",
        "answer": "You can update your registered mobile number through your bank's branch or supported digital banking services."
    },
    {
        "question": "What should I do if a transaction fails?",
        "answer": "Check your account and transaction status first. If the money was debited but the transaction failed, contact your bank through its official support channel."
    }
]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


def similarity(text1, text2):
    return SequenceMatcher(
        None,
        clean_text(text1),
        clean_text(text2)
    ).ratio()


def get_answer(user_question):
    best_score = 0
    best_answer = None

    for faq in faqs:
        score = similarity(user_question, faq["question"])

        if score > best_score:
            best_score = score
            best_answer = faq["answer"]

    if best_score >= 0.35:
        return best_answer

    return "Sorry, I couldn't find a suitable answer. Please try asking your banking question differently."


def send_message():
    user_question = entry.get().strip()

    if not user_question:
        return

    chat.insert(tk.END, "You: " + user_question + "\n")

    answer = get_answer(user_question)

    chat.insert(tk.END, "Bot: " + answer + "\n\n")

    entry.delete(0, tk.END)


# Create window
root = tk.Tk()
root.title("Banking FAQ Chatbot")
root.geometry("500x600")

title = tk.Label(
    root,
    text="Banking FAQ Chatbot",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

chat = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=55,
    height=25
)
chat.pack(padx=10, pady=10)

entry = tk.Entry(
    root,
    font=("Arial", 14)
)
entry.pack(
    padx=10,
    pady=5,
    fill=tk.X
)

send_button = tk.Button(
    root,
    text="Send",
    font=("Arial", 12, "bold"),
    command=send_message
)
send_button.pack(pady=10)
def clear_chat():
    chat.delete("1.0", tk.END)


clear_button = tk.Button(
    root,
    text="CLEAR CHAT",
    font=("Arial", 12),
    command=clear_chat
)
clear_button.pack(pady=5)

root.mainloop()