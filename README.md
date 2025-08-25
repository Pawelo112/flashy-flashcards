# 📘 Flashy — Learning Flashcards with Tkinter

This project is an interactive flashcard application built with **Python** and **Tkinter** to help learn any subject that you want - in this example it is French vocabulary.  
It shows a French word, allows you to flip the card to see its English translation, and tracks your progress by saving words you already learned.

## 📑 Table of Contents
- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [📷 User Interface](#-UI)
- [🚀 Usage](#-usage)
- [⚙️ Installation](#️-installation)
- [🧠 Summary](#-summary)
- [📜 License](#-license)

## ✨ Features
- 🎴 Flashcards with **French word on the front** and **English translation on the back**  
- 🔄 **Flip button** to switch between front and back  
- ✔️ **Mark as Known** → removes the word from future practice and saves progress  
- ❌ **Skip button** → shows a new card without removing the word  
- 💾 Progress persistence: learned words are stored in `data/words_to_learn.csv`  
- 🖼️ User-friendly UI with custom card images

## 📂 Project Structure
<details>
<summary><strong>Click to expand</strong></summary>
  
flashy-flashcards/  
│── data/  
│    ├── french_words.csv  # Original dataset of words  
│    ├── words_to_learn.csv # Auto-generated: stores remaining words to learn  
│  
│── images/ # Images used in UI  
│    ├── card_front.png  
│    ├── card_back.png  
│    ├── right.png  
│    ├── wrong.png  
│    └── flip.png  
│  
│── main.py # Main application code  
│── README.md # Project documentation  

</details>

## 📸 UI
<p align="center">
  <img src="https://github.com/user-attachments/assets/6e3c092c-9d25-4ef9-8ce4-0fbca1a4c677" alt="Flashcard Front" width="400"/>
  <img src="https://github.com/user-attachments/assets/d86336a0-b125-4db1-bcfb-5945f7f760e3" alt="Flashcard Back" width="400"/>
</p>

---

## 🚀 Usage
- Click ❌ (Still learning) to skip and see a new card.
- Click ✔️ (Learned) if you know the word → it will be removed from your learning list.
- Click 🔄 (Flip) to flip the card and see the translation.
- Your progress is automatically saved into data/words_to_learn.csv.

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flashy-flashcards.git
   cd flashy-flashcards
   ```  
2. **Install Dependencies**
   ```bash
   pip install pandas
   ```
3. **Run the app**
   ```bash
   python main.py
   ```

## 🧠 Summary

**This project** is a customizable flashcard learning tool. It’s perfect for:
- Learning **French vocabulary** (for example),
- Or any other language / subject you like!

You can just modify the CSV file (`data/french_words.csv`) to include your own word pairs (e.g. Spanish–English, medical terms, coding concepts, etc.), then change 
the dictionaries keys in the  main code and app will do the rest:
- Show a random word on the front,
- Let you flip it to see the translation\explanation,
- Keep track of which ones you’ve learned by saving them to `data/words_to_learn.csv`.

## 📖License
Copyright © 2025 [Paweł Marcinkowski](https://github.com/Pawelo112).  
This project is [MIT](https://github.com/Pawelo112/flashy-flashcards/blob/main/LICENSE) licensed.
