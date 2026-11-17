# 🃏 BlackJack

**A command-line Blackjack game in Python with betting, a 3:2 blackjack payout and a player balance saved between sessions.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

---

## ✨ Features

- Full 52-card deck, shuffled every round
- Correct hand scoring, with **Aces counting as 11 or 1** automatically
- Betting with a **$5 minimum** and a **3:2 payout** on blackjack
- **Saved balance**: your money is stored in a file and loaded the next time you play
- **Buy-in**: top up your money when you drop below the minimum bet
- Input checking, so invalid bets and numbers are handled cleanly

## 📁 Files

| File | Purpose |
|---|---|
| `blackjack.py` | Game logic: deck, hands, betting and the main game loop |
| `db.py` | Reads and writes the player's balance (creates it with $100 if missing) |

## 🚀 Run it

```bash
python blackjack.py
```

No extra packages are needed, only the Python standard library.

---

👩‍💻 Developed by **[Anumol Thomas](https://github.com/anuthomson)**
