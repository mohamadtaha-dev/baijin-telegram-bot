# 🎮 Baijin — Persian Telegram Word Game

**Baijin** is a Persian word puzzle game developed with Python and the Telegram Bot API.

Players solve scrambled Persian words, earn rewards, lose hearts when they make mistakes, and progress through different game stages.

---

## ✨ Features

* 🎮 Interactive Telegram gameplay
* 🧩 Persian scrambled-word puzzles
* 🎯 Stage-based progression
* ❤️ Heart/life system
* 🏆 Leaderboard
* 👤 Player profiles
* 🎁 Daily rewards
* 💰 Coins and XP system
* 💾 SQLite database
* 📱 Telegram keyboard interface

---

## 🛠️ Technologies

| Technology             | Usage                     |
| ---------------------- | ------------------------- |
| 🐍 Python              | Main programming language |
| 🤖 Telegram Bot API    | Bot communication         |
| 🗄️ SQLite             | Database                  |
| 📦 python-telegram-bot | Telegram bot framework    |
| 📄 JSON                | Word data                 |

---

## 🎯 How the Game Works

The player receives a scrambled Persian word.

For example:

```text
تابک
```

The player has to find the correct word:

```text
کتاب
```

Each stage contains multiple words.

Players need to solve the required words to progress to the next stage.

Wrong answers reduce the player's hearts.

---

## 📂 Project Structure

```text
baijin-telegram-bot/
│
├── main.py          # Main bot application
├── database.py      # Database and player data management
├── game.py          # Game logic
├── keyboards.py     # Telegram keyboard layouts
├── words.json       # Persian word data
├── .gitignore       # Ignored files
└── README.md        # Project documentation
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/mohamadtaha-dev/baijin-telegram-bot.git
```

Enter the project directory:

```bash
cd baijin-telegram-bot
```

Install the dependencies:

```bash
pip install python-telegram-bot
```

---

## 🔐 Configuration

Create a `config.py` file locally and add your Telegram Bot Token:

```python
TOKEN = "YOUR_BOT_TOKEN"
```

> Never publish your real bot token on GitHub.

---

## ▶️ Run the Bot

Run:

```bash
python main.py
```

If everything is configured correctly, the bot will start and be ready to receive Telegram messages.

---

## 🚀 Future Improvements

Planned improvements include:

* 🌐 Web-based admin panel
* 📊 Advanced player statistics
* 🥇 Global ranking system
* 🎨 Improved game interface
* 🔔 More game modes
* ☁️ 24/7 cloud deployment
* 📈 Expanded Persian word database

---

## 👨‍💻 Developer

**Mohamad Taha**

Python Developer interested in:

* 🤖 Artificial Intelligence
* 🧠 Machine Learning
* 👁️ Computer Vision
* 📊 Data Science
* 🐍 Python Development

GitHub:
https://github.com/mohamadtaha-dev

---

## ⭐ Support

If you find this project interesting, consider giving it a ⭐ on GitHub.

---

**Built with Python 🐍 and curiosity 💡**
