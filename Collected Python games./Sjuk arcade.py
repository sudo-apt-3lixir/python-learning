import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os
import math


# ============================================================
# PYTHON ARCADE ULTIMATE
# ============================================================

APP_NAME = "Python Arcade Ultimate"
DATA_FILE = "python_arcade_data.json"


# ============================================================
# FÄRGER / TEMAN
# ============================================================

THEMES = {
    "Dark": {
        "bg": "#111318",
        "panel": "#191c24",
        "button": "#242936",
        "button_hover": "#303747",
        "text": "#ffffff",
        "secondary": "#9ca3af",
        "accent": "#6c63ff",
        "success": "#22c55e",
        "danger": "#ef4444",
        "entry": "#20242d"
    },

    "Purple": {
        "bg": "#120b1f",
        "panel": "#1e1233",
        "button": "#301c4f",
        "button_hover": "#43276e",
        "text": "#ffffff",
        "secondary": "#c4b5fd",
        "accent": "#a855f7",
        "success": "#22c55e",
        "danger": "#ef4444",
        "entry": "#25163b"
    },

    "Blue": {
        "bg": "#08111f",
        "panel": "#0e1b2d",
        "button": "#142943",
        "button_hover": "#1c3a60",
        "text": "#ffffff",
        "secondary": "#93c5fd",
        "accent": "#3b82f6",
        "success": "#22c55e",
        "danger": "#ef4444",
        "entry": "#102137"
    },

    "Green": {
        "bg": "#08150e",
        "panel": "#102219",
        "button": "#173325",
        "button_hover": "#214a34",
        "text": "#ffffff",
        "secondary": "#86efac",
        "accent": "#22c55e",
        "success": "#4ade80",
        "danger": "#ef4444",
        "entry": "#14291e"
    }
}


# ============================================================
# SPARAD DATA
# ============================================================

default_data = {
    "xp": 0,
    "level": 1,
    "games_played": 0,
    "questions_answered": 0,
    "correct_answers": 0,
    "best_math": 0,
    "best_history": 0,
    "best_guess": 999,
    "streak": 0,
    "best_streak": 0,
    "achievements": [],
    "theme": "Dark"
}


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            for key in default_data:
                if key not in data:
                    data[key] = default_data[key]

            return data

        except Exception:
            return default_data.copy()

    return default_data.copy()


data = load_data()


def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception:
        pass


# ============================================================
# APP
# ============================================================

root = tk.Tk()

root.title(APP_NAME)
root.geometry("1100x720")
root.minsize(900, 600)


# ============================================================
# HJÄLPFUNKTIONER
# ============================================================

def theme():
    return THEMES[data["theme"]]


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def add_xp(amount):
    data["xp"] += amount

    while data["xp"] >= data["level"] * 100:
        data["xp"] -= data["level"] * 100
        data["level"] += 1

        messagebox.showinfo(
            "LEVEL UP!",
            f"🔥 LEVEL UP!\n\nDu är nu level {data['level']}!"
        )

    save_data()


def update_stats(correct):
    data["questions_answered"] += 1

    if correct:
        data["correct_answers"] += 1
        data["streak"] += 1

        if data["streak"] > data["best_streak"]:
            data["best_streak"] = data["streak"]

    else:
        data["streak"] = 0

    save_data()


def unlock(name):
    if name not in data["achievements"]:
        data["achievements"].append(name)

        messagebox.showinfo(
            "🏆 Achievement Unlocked!",
            f"Du låste upp:\n\n🏆 {name}"
        )

        save_data()


def styled_button(parent, text, command, width=25):
    colors = theme()

    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=2,
        font=("Arial", 13, "bold"),
        bg=colors["button"],
        fg=colors["text"],
        activebackground=colors["button_hover"],
        activeforeground=colors["text"],
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    return button


def title(parent, text, subtitle=None):
    colors = theme()

    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 30, "bold"),
        bg=colors["bg"],
        fg=colors["text"]
    )

    label.pack(pady=(25, 5))

    if subtitle:
        sub = tk.Label(
            parent,
            text=subtitle,
            font=("Arial", 12),
            bg=colors["bg"],
            fg=colors["secondary"]
        )

        sub.pack(pady=(0, 20))


def create_card(parent, title_text, text, command):
    colors = theme()

    card = tk.Frame(
        parent,
        bg=colors["panel"],
        width=250,
        height=150
    )

    card.pack_propagate(False)

    label = tk.Label(
        card,
        text=title_text,
        font=("Arial", 17, "bold"),
        bg=colors["panel"],
        fg=colors["text"]
    )

    label.pack(pady=(20, 5))

    desc = tk.Label(
        card,
        text=text,
        font=("Arial", 10),
        bg=colors["panel"],
        fg=colors["secondary"],
        wraplength=210
    )

    desc.pack()

    button = styled_button(card, "ÖPPNA", command, 18)
    button.pack(pady=10)

    return card


# ============================================================
# SIDEBAR
# ============================================================

def build_sidebar():
    colors = theme()

    sidebar = tk.Frame(
        root,
        bg=colors["panel"],
        width=210
    )

    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    logo = tk.Label(
        sidebar,
        text="PYTHON\nARCADE",
        font=("Arial", 22, "bold"),
        bg=colors["panel"],
        fg=colors["accent"]
    )

    logo.pack(pady=30)

    menu_items = [
        ("🏠 Dashboard", dashboard),
        ("🧮 Kalkylator", calculator),
        ("🎮 Lekar", games_menu),
        ("📚 Historia", history_menu),
        ("🏆 Achievements", achievements_page),
        ("📊 Statistik", statistics_page),
        ("⚙ Inställningar", settings_page)
    ]

    for text, command in menu_items:
        button = tk.Button(
            sidebar,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            bg=colors["panel"],
            fg=colors["text"],
            activebackground=colors["button_hover"],
            activeforeground=colors["text"],
            relief="flat",
            anchor="w",
            padx=20,
            pady=12,
            cursor="hand2"
        )

        button.pack(fill="x")

    bottom = tk.Frame(sidebar, bg=colors["panel"])
    bottom.pack(side="bottom", fill="x", pady=20)

    level_label = tk.Label(
        bottom,
        text=f"⭐ LEVEL {data['level']}",
        font=("Arial", 12, "bold"),
        bg=colors["panel"],
        fg=colors["text"]
    )

    level_label.pack()

    xp_label = tk.Label(
        bottom,
        text=f"{data['xp']} XP",
        bg=colors["panel"],
        fg=colors["secondary"]
    )

    xp_label.pack()


# ============================================================
# PAGE SYSTEM
# ============================================================

def page():
    clear_window()
    build_sidebar()

    colors = theme()

    content = tk.Frame(
        root,
        bg=colors["bg"]
    )

    content.pack(
        side="right",
        fill="both",
        expand=True
    )

    return content


# ============================================================
# DASHBOARD
# ============================================================

def dashboard():
    content = page()

    title(
        content,
        "🎮 PYTHON ARCADE",
        "Välkommen tillbaka, gamer."
    )

    stats_frame = tk.Frame(
        content,
        bg=theme()["bg"]
    )

    stats_frame.pack(pady=10)

    stats = [
        ("⭐", "Level", data["level"]),
        ("⚡", "XP", data["xp"]),
        ("🔥", "Streak", data["streak"]),
        ("🎯", "Frågor", data["questions_answered"])
    ]

    for icon, name, value in stats:
        card = tk.Frame(
            stats_frame,
            bg=theme()["panel"],
            width=160,
            height=100
        )

        card.pack_propagate(False)
        card.pack(side="left", padx=8)

        tk.Label(
            card,
            text=f"{icon} {value}",
            font=("Arial", 20, "bold"),
            bg=theme()["panel"],
            fg=theme()["accent"]
        ).pack(pady=(15, 3))

        tk.Label(
            card,
            text=name,
            bg=theme()["panel"],
            fg=theme()["secondary"]
        ).pack()

    tk.Label(
        content,
        text="VAD VILL DU GÖRA?",
        font=("Arial", 18, "bold"),
        bg=theme()["bg"],
        fg=theme()["text"]
    ).pack(pady=25)

    cards = tk.Frame(
        content,
        bg=theme()["bg"]
    )

    cards.pack()

    create_card(
        cards,
        "🧮 Kalkylator",
        "Räkna snabbt och enkelt.",
        calculator
    ).grid(row=0, column=0, padx=10, pady=10)

    create_card(
        cards,
        "🎮 Lekar",
        "Spela quiz och utmana dig själv.",
        games_menu
    ).grid(row=0, column=1, padx=10, pady=10)

    create_card(
        cards,
        "📚 Historia",
        "Testa dina historiekunskaper.",
        history_menu
    ).grid(row=0, column=2, padx=10, pady=10)

    create_card(
        cards,
        "🏆 Achievements",
        "Se vad du har låst upp.",
        achievements_page
    ).grid(row=1, column=0, padx=10, pady=10)

    create_card(
        cards,
        "📊 Statistik",
        "Se hur bra du faktiskt är.",
        statistics_page
    ).grid(row=1, column=1, padx=10, pady=10)

    create_card(
        cards,
        "⚙ Inställningar",
        "Ändra tema och data.",
        settings_page
    ).grid(row=1, column=2, padx=10, pady=10)


# ============================================================
# KALKYLATOR
# ============================================================

def calculator():
    content = page()

    title(
        content,
        "🧮 KALKYLATOR",
        "En lite mer avancerad calculator."
    )

    display = tk.Entry(
        content,
        font=("Arial", 25),
        justify="right",
        bg=theme()["entry"],
        fg=theme()["text"],
        insertbackground=theme()["text"],
        relief="flat"
    )

    display.pack(
        padx=80,
        pady=20,
        fill="x",
        ipady=15
    )

    buttons = [
        ["7", "8", "9", "/", "√"],
        ["4", "5", "6", "*", "x²"],
        ["1", "2", "3", "-", "%"],
        ["0", ".", "(", ")", "+"],
        ["C", "⌫", "="]
    ]

    button_frame = tk.Frame(
        content,
        bg=theme()["bg"]
    )

    button_frame.pack()

    def press(value):
        if value == "C":
            display.delete(0, tk.END)

        elif value == "⌫":
            current = display.get()
            display.delete(0, tk.END)
            display.insert(0, current[:-1])

        elif value == "=":
            try:
                expression = display.get()
                answer = eval(
                    expression,
                    {"__builtins__": None},
                    {}
                )

                display.delete(0, tk.END)
                display.insert(0, str(answer))

            except Exception:
                display.delete(0, tk.END)
                display.insert(0, "ERROR")

        elif value == "√":
            try:
                number = float(display.get())
                display.delete(0, tk.END)
                display.insert(0, str(math.sqrt(number)))

            except Exception:
                display.delete(0, tk.END)
                display.insert(0, "ERROR")

        elif value == "x²":
            try:
                number = float(display.get())
                display.delete(0, tk.END)
                display.insert(0, str(number ** 2))

            except Exception:
                display.delete(0, tk.END)
                display.insert(0, "ERROR")

        elif value == "%":
            try:
                number = float(display.get())
                display.delete(0, tk.END)
                display.insert(0, str(number / 100))

            except Exception:
                display.delete(0, tk.END)
                display.insert(0, "ERROR")

        else:
            display.insert(tk.END, value)

    for row, row_buttons in enumerate(buttons):

        for col, value in enumerate(row_buttons):

            button = tk.Button(
                button_frame,
                text=value,
                command=lambda v=value: press(v),
                width=6,
                height=2,
                font=("Arial", 15, "bold"),
                bg=theme()["button"],
                fg=theme()["text"],
                activebackground=theme()["button_hover"],
                relief="flat"
            )

            button.grid(
                row=row,
                column=col,
                padx=4,
                pady=4
            )

    root.bind(
        "<Return>",
        lambda event: press("=")
    )


# ============================================================
# LEKAR MENY
# ============================================================

def games_menu():
    content = page()

    title(
        content,
        "🎮 LEKAR",
        "Välj ditt nästa challenge."
    )

    games = tk.Frame(
        content,
        bg=theme()["bg"]
    )

    games.pack()

    create_card(
        games,
        "🎯 Gissa numret",
        "Hitta det hemliga numret.",
        guess_number
    ).grid(row=0, column=0, padx=15, pady=15)

    create_card(
        games,
        "✅ Sant eller falskt",
        "Hur mycket vet du egentligen?",
        true_false
    ).grid(row=0, column=1, padx=15, pady=15)

    create_card(
        games,
        "🧠 Matte Challenge",
        "Fem slumpade mattefrågor.",
        math_challenge
    ).grid(row=0, column=2, padx=15, pady=15)


# ============================================================
# GISSA NUMRET
# ============================================================

def guess_number():
    content = page()

    title(
        content,
        "🎯 GISSA NUMRET",
        "Välj svårighetsgrad."
    )

    result = tk.Label(
        content,
        text="",
        font=("Arial", 15),
        bg=theme()["bg"],
        fg=theme()["text"]
    )

    result.pack(pady=15)

    def start_game(max_number, difficulty):

        for widget in content.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        number = random.randint(1, max_number)
        attempts = 0

        question = tk.Label(
            content,
            text=f"Jag tänker på ett tal mellan 1 och {max_number}!",
            font=("Arial", 17),
            bg=theme()["bg"],
            fg=theme()["text"]
        )

        question.pack(pady=20)

        entry = tk.Entry(
            content,
            font=("Arial", 16),
            bg=theme()["entry"],
            fg=theme()["text"],
            insertbackground=theme()["text"]
        )

        entry.pack(pady=10)

        def guess():

            nonlocal attempts

            try:
                value = int(entry.get())
                attempts += 1

                if value < number:
                    result.config(text="⬆ För lågt!")

                elif value > number:
                    result.config(text="⬇ För högt!")

                else:
                    result.config(
                        text=f"🎉 RÄTT!\nDu klarade det på {attempts} försök!"
                    )

                    xp = max(10, 100 - attempts * 5)

                    add_xp(xp)

                    data["games_played"] += 1

                    if attempts < data["best_guess"]:
                        data["best_guess"] = attempts

                    update_stats(True)

                    if attempts == 1:
                        unlock("ONE SHOT")

                    save_data()

            except ValueError:
                result.config(text="Skriv ett heltal!")

        styled_button(
            content,
            "Gissa",
            guess,
            18
        ).pack(pady=10)

    styled_button(
        content,
        "🟢 Easy 1–50",
        lambda: start_game(50, "Easy"),
        25
    ).pack(pady=5)

    styled_button(
        content,
        "🟡 Medium 1–100",
        lambda: start_game(100, "Medium"),
        25
    ).pack(pady=5)

    styled_button(
        content,
        "🔴 Hard 1–1000",
        lambda: start_game(1000, "Hard"),
        25
    ).pack(pady=5)


# ============================================================
# SANT ELLER FALSKT
# ============================================================

def true_false():
    content = page()

    title(
        content,
        "✅ SANT ELLER FALSKT",
        "Tre frågor. En chans."
    )

    questions = [
        ["Sverige ligger i Europa.", "sant"],
        ["Jorden är platt.", "falskt"],
        ["Vatten fryser vid 0 grader Celsius.", "sant"],
        ["Stockholm är Sveriges huvudstad.", "sant"],
        ["Månen är större än jorden.", "falskt"],
        ["En vecka har 7 dagar.", "sant"],
        ["Solen är en planet.", "falskt"],
        ["H2O är vatten.", "sant"],
        ["En timme har 60 minuter.", "sant"],
        ["Sverige ligger i Afrika.", "falskt"],
        ["Frankrike ligger i Sydamerika.", "falskt"],
        ["Romarriket hade stor betydelse för Europas historia.", "sant"]
    ]

    random.shuffle(questions)

    current = 0
    score = 0

    question_label = tk.Label(
        content,
        text="",
        font=("Arial", 18),
        wraplength=650,
        bg=theme()["bg"],
        fg=theme()["text"]
    )

    question_label.pack(pady=40)

    result = tk.Label(
        content,
        text="",
        font=("Arial", 14),
        bg=theme()["bg"],
        fg=theme()["secondary"]
    )

    result.pack(pady=15)

    buttons = tk.Frame(
        content,
        bg=theme()["bg"]
    )

    buttons.pack()

    def show_question():
        question_label.config(
            text=f"Fråga {current + 1} / 3\n\n{questions[current][0]}"
        )

    def answer(value):

        nonlocal current
        nonlocal score

        correct = value == questions[current][1]

        update_stats(correct)

        if correct:
            score += 1
            add_xp(20)
            result.config(
                text="🎉 Rätt!"
            )
        else:
            result.config(
                text="❌ Fel!"
            )

        current += 1

        if current >= 3:

            question_label.config(
                text=f"🏆 RESULTAT\n\n{score} / 3 rätt!"
            )

            if score > 0:
                add_xp(score * 20)

            if score == 3:
                unlock("PERFEKT QUIZ")

            if score > data["best_history"]:
                data["best_history"] = score

            data["games_played"] += 1

            for button in buttons.winfo_children():
                button.config(state="disabled")

            save_data()

        else:
            show_question()

    styled_button(
        buttons,
        "✅ SANT",
        lambda: answer("sant"),
        15
    ).grid(row=0, column=0, padx=10)

    styled_button(
        buttons,
        "❌ FALSKT",
        lambda: answer("falskt"),
        15
    ).grid(row=0, column=1, padx=10)

    show_question()


# ============================================================
# MATTE CHALLENGE
# ============================================================

def math_challenge():
    content = page()

    title(
        content,
        "🧠 MATTE CHALLENGE",
        "Fem slumpade frågor."
    )

    question_label = tk.Label(
        content,
        text="",
        font=("Arial", 20),
        bg=theme()["bg"],
        fg=theme()["text"]
    )

    question_label.pack(pady=35)

    entry = tk.Entry(
        content,
        font=("Arial", 18),
        bg=theme()["entry"],
        fg=theme()["text"],
        insertbackground=theme()["text"]
    )

    entry.pack(pady=10)

    result = tk.Label(
        content,
        text="",
        font=("Arial", 14),
        bg=theme()["bg"],
        fg=theme()["secondary"]
    )

    result.pack(pady=15)

    current = 0
    score = 0
    correct_answer = 0

    def new_question():

        nonlocal correct_answer

        number1 = random.randint(1, 30)
        number2 = random.randint(1, 30)

        operation = random.choice([
            "+",
            "-",
            "*"
        ])

        if operation == "+":
            correct_answer = number1 + number2

        elif operation == "-":
            correct_answer = number1 - number2

        else:
            correct_answer = number1 * number2

        question_label.config(
            text=f"Fråga {current + 1} / 5\n\n"
                 f"{number1} {operation} {number2} = ?"
        )

    def answer():

        nonlocal current
        nonlocal score

        try:
            value = float(entry.get())

            correct = value == correct_answer

            update_stats(correct)

            if correct:
                score += 1
                result.config(text="🎉 Rätt!")
                add_xp(25)

            else:
                result.config(
                    text=f"❌ Fel! Rätt svar: {correct_answer}"
                )

            current += 1

            entry.delete(0, tk.END)

            if current >= 5:

                question_label.config(
                    text=f"🏆 RESULTAT\n\n{score} / 5 rätt!"
                )

                entry.config(state="disabled")
                answer_button.config(state="disabled")

                if score > data["best_math"]:
                    data["best_math"] = score

                if score == 5:
                    unlock("MATTE MASTER")

                data["games_played"] += 1

                save_data()

            else:
                new_question()

        except ValueError:
            result.config(
                text="Skriv ett nummer!"
            )

    answer_button = styled_button(
        content,
        "Svara",
        answer,
        18
    )

    answer_button.pack(pady=10)

    new_question()


# ============================================================
# HISTORIA MENY
# ============================================================

def history_menu():
    content = page()

    title(
        content,
        "📚 HISTORIA ARCADE",
        "Hur bra koll har du på historien?"
    )

    frame = tk.Frame(
        content,
        bg=theme()["bg"]
    )

    frame.pack()

    create_card(
        frame,
        "📖 Historiequiz",
        "Testa dina historiekunskaper.",
        history_quiz
    ).grid(row=0, column=0, padx=15, pady=15)

    create_card(
        frame,
        "🕵️ Vem är jag?",
        "Identifiera historiska personer.",
        who_am_i
    ).grid(row=0, column=1, padx=15, pady=15)

    create_card(
        frame,
        "📅 Gissa årtalet",
        "Vilket år hände det?",
        guess_year
    ).grid(row=0, column=2, padx=15, pady=15)


# ============================================================
# HISTORIEQUIZ
# ============================================================

def history_quiz():
    content = page()

    title(
        content,
        "📖 HISTORIEQUIZ",
        "Fem frågor."
    )

    questions = [
        ["När började andra världskriget?", "1939"],
        ["När slutade andra världskriget?", "1945"],
        ["När började första världskriget?", "1914"],
        ["När landade människan på månen?", "1969"],
        ["När började Franska revolutionen?", "1789"],
        ["När föll Berlinmuren?", "1989"],
        ["När blev Sverige medlem i EU?", "1995"],
        ["Vem var Sveriges kung och grundade Vasaätten?", "Gustav Vasa"],
        ["Vem var Frankrikes kejsare under Napoleonkrigen?", "Napoleon"],
        ["Vilken stad var centrum för det antika romarriket?", "Rom"]
    ]

    random.shuffle(questions)

    current = 0
    score = 0

    question_label = tk.Label(
        content,
        text="",
        font=("Arial", 18),
        wraplength=700,
        bg=theme()["bg"],
        fg=theme()["text"]
    )

    question_label.pack(pady=30)

    entry = tk.Entry(
        content,
        font=("Arial", 16),
        bg=theme()["entry"],
        fg=theme()["text"],
        insertbackground=theme()["text"]
    )

    entry.pack(pady=10)

    result = tk.Label(
        content,
        text="",
        font=("Arial", 14),
        bg=theme()["bg"],
        fg=theme()["secondary"]
    )

    result.pack(pady=15)

    def show_question():
        question_label.config(
            text=f"Fråga {current + 1} / 5\n\n{questions[current][0]}"
        )

    def answer():

        nonlocal current
        nonlocal score

        value = entry.get().strip()

        correct = value.lower() == questions[current][1].lower()

        update_stats(correct)

        if correct:
            score += 1
            add_xp(30)
            result.config(text="🎉 Rätt!")

        else:
            result.config(
                text=f"❌ Fel! Rätt svar: {questions[current][1]}"
            )

        current += 1
        entry.delete(0, tk.END)

        if current >= 5:

            question_label.config(
                text=f"🏆 RESULTAT\n\n{score} / 5 rätt!"
            )

            entry.config(state="disabled")
            answer_button.config(state="disabled")

            if score > data["best_history"]:
                data["best_history"] = score

            if score == 5:
                unlock("HISTORY LEGEND")

            data["games_played"] += 1

            save_data()

        else:
            show_question()

    answer_button = styled_button(
        content,
        "Svara",
        answer,
        18
    )

    answer_button.pack()

    show_question()


# ============================================================
# VEM ÄR JAG?
# ============================================================

def who_am_i():
    content = page()

    title(
        content,
        "🕵️ VEM ÄR JAG?",
        "Identifiera personen."
    )

    people = [
        [
            "Jag var svensk kung och grundade Vasaätten.",
            "Gustav Vasa"
        ],
        [
            "Jag var svensk kung och dog i slaget vid Lützen.",
            "Gustav II Adolf"
        ],
        [
            "Jag var fransk kejsare och förlorade vid Waterloo.",
            "Napoleon"
        ],
        [
            "Jag var en egyptisk drottning.",
            "Kleopatra"
        ],
        [
            "Jag var en brittisk drottning under den viktorianska eran.",
            "Victoria"
        ],
        [
            "Jag var en amerikansk president under det amerikanska inbördeskriget.",
            "Abraham Lincoln"
        ]
    ]

    person = random.choice(people)

    tk.Label(
        content,
        text=person[0],
        font=("Arial", 19),
        wraplength=700,
        bg=theme()["bg"],
        fg=theme()["text"]
    ).pack(pady=50)

    entry = tk.Entry(
        content,
        font=("Arial", 16),
        bg=theme()["entry"],
        fg=theme()["text"],
        insertbackground=theme()["text"]
    )

    entry.pack(pady=10)

    result = tk.Label(
        content,
        text="",
        font=("Arial", 14),
        bg=theme()["bg"],
        fg=theme()["secondary"]
    )

    result.pack(pady=15)

    def answer():

        value = entry.get().strip()

        correct = value.lower() == person[1].lower()

        update_stats(correct)

        if correct:
            result.config(text="🎉 RÄTT!")
            add_xp(50)
            unlock("HISTORY DETECTIVE")

        else:
            result.config(
                text=f"❌ Fel! Personen var {person[1]}"
            )

        button.config(state="disabled")

    button = styled_button(
        content,
        "Svara",
        answer,
        18
    )

    button.pack()


# ============================================================
# GISSA ÅRTALET
# ============================================================

def guess_year():
    content = page()

    title(
        content,
        "📅 GISSA ÅRTALET",
        "Vilket år hände detta?"
    )

    events = [
        ["Andra världskriget börjar", 1939],
        ["Första världskriget börjar", 1914],
        ["Franska revolutionen börjar", 1789],
        ["Människan landar på månen", 1969],
        ["Berlinmuren faller", 1989],
        ["Sverige blir medlem i EU", 1995],
        ["Titanic sjunker", 1912],
        ["Dagen då Gustav Vasa valdes till kung av Sverige", 1523]
    ]

    event = random.choice(events)

    tk.Label(
        content,
        text=event[0],
        font=("Arial", 20),
        wraplength=700,
        bg=theme()["bg"],
        fg=theme()["text"]
    ).pack(pady=50)

    entry = tk.Entry(
        content,
        font=("Arial", 18),
        bg=theme()["entry"],
        fg=theme()["text"],
        insertbackground=theme()["text"]
    )

    entry.pack(pady=10)

    result = tk.Label(
        content,
        text="",
        font=("Arial", 14),
        bg=theme()["bg"],
        fg=theme()["secondary"]
    )

    result.pack(pady=15)

    def answer():

        try:
            value = int(entry.get())

            correct = value == event[1]

            update_stats(correct)

            if correct:
                result.config(text="🎉 Rätt!")
                add_xp(40)

            else:
                result.config(
                    text=f"❌ Fel! Rätt år: {event[1]}"
                )

            button.config(state="disabled")

        except ValueError:
            result.config(
                text="Skriv ett årtal!"
            )

    button = styled_button(
        content,
        "Svara",
        answer,
        18
    )

    button.pack()


# ============================================================
# ACHIEVEMENTS
# ============================================================

def achievements_page():
    content = page()

    title(
        content,
        "🏆 ACHIEVEMENTS",
        "Hur många kan du låsa upp?"
    )

    achievements = [
        ("ONE SHOT", "Gissa rätt på första försöket."),
        ("PERFEKT QUIZ", "Få 3/3 på Sant eller falskt."),
        ("MATTE MASTER", "Få 5/5 på Matte Challenge."),
        ("HISTORY LEGEND", "Få 5/5 på Historiequiz."),
        ("HISTORY DETECTIVE", "Klara Vem är jag?.")
    ]

    for name, description in achievements:

        unlocked = name in data["achievements"]

        if unlocked:
            status = "🏆 UNLOCKED"
        else:
            status = "🔒 LOCKED"

        frame = tk.Frame(
            content,
            bg=theme()["panel"],
            width=600,
            height=70
        )

        frame.pack(pady=5)
        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=status,
            font=("Arial", 12, "bold"),
            bg=theme()["panel"],
            fg=theme()["accent"]
        ).pack(side="left", padx=15)

        tk.Label(
            frame,
            text=name,
            font=("Arial", 13, "bold"),
            bg=theme()["panel"],
            fg=theme()["text"]
        ).pack(side="left")

        tk.Label(
            frame,
            text=description,
            font=("Arial", 10),
            bg=theme()["panel"],
            fg=theme()["secondary"]
        ).pack(side="right", padx=15)


# ============================================================
# STATISTIK
# ============================================================

def statistics_page():
    content = page()

    title(
        content,
        "📊 STATISTIK",
        "Din Python Arcade-profil."
    )

    total = data["questions_answered"]

    if total > 0:
        accuracy = round(
            data["correct_answers"] / total * 100
        )
    else:
        accuracy = 0

    stats = [
        ("⭐ Level", data["level"]),
        ("⚡ XP", data["xp"]),
        ("🎮 Spel spelade", data["games_played"]),
        ("❓ Frågor", total),
        ("✅ Rätt", data["correct_answers"]),
        ("🎯 Accuracy", str(accuracy) + "%"),
        ("🔥 Bästa streak", data["best_streak"]),
        ("🧠 Bästa matte", data["best_math"]),
        ("📚 Bästa historia", data["best_history"]),
        ("🎯 Bästa gissning", data["best_guess"])
    ]

    for name, value in stats:

        frame = tk.Frame(
            content,
            bg=theme()["panel"],
            width=500,
            height=45
        )

        frame.pack(pady=3)
        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=name,
            font=("Arial", 11, "bold"),
            bg=theme()["panel"],
            fg=theme()["text"]
        ).pack(side="left", padx=15)

        tk.Label(
            frame,
            text=str(value),
            font=("Arial", 11, "bold"),
            bg=theme()["panel"],
            fg=theme()["accent"]
        ).pack(side="right", padx=15)


# ============================================================
# INSTÄLLNINGAR
# ============================================================

def settings_page():
    content = page()

    title(
        content,
        "⚙ INSTÄLLNINGAR",
        "Anpassa Python Arcade."
    )

    tk.Label(
        content,
        text="🎨 Välj tema",
        font=("Arial", 17, "bold"),
        bg=theme()["bg"],
        fg=theme()["text"]
    ).pack(pady=20)

    for theme_name in THEMES:

        button = styled_button(
            content,
            theme_name,
            lambda t=theme_name: change_theme(t),
            20
        )

        button.pack(pady=5)

    tk.Label(
        content,
        text="⚠ DANGER ZONE",
        font=("Arial", 18, "bold"),
        bg=theme()["bg"],
        fg=theme()["danger"]
    ).pack(pady=(40, 10))

    styled_button(
        content,
        "🗑 Reset all statistik",
        reset_data,
        25
    ).pack()


def change_theme(name):
    data["theme"] = name
    save_data()
    dashboard()


def reset_data():

    answer = messagebox.askyesno(
        "Reset",
        "Är du säker?\n\nAll XP, statistik och achievements försvinner."
    )

    if answer:

        for key in default_data:
            data[key] = default_data[key]

        save_data()

        messagebox.showinfo(
            "Reset",
            "All statistik har återställts."
        )

        dashboard()


# ============================================================
# START
# ============================================================

dashboard()

root.mainloop()