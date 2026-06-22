# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied

- Game purpose: A number guessing game built with Streamlit where the player tries to guess a secret value and receives hints.
- Bugs found: The guess parser rejected text like "guess 50", the hint logic could be wrong, and game logic was mixed into the UI code.
- Fixes applied: Moved core logic into `logic_utils.py`, fixed guess parsing for text input, corrected hint handling, and simplified the app state flow.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "Too High"
3. User enters a guess of 40 → "Too Low"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

python3 -m pytest -v
============================= test session starts =============================
platform darwin -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
cachedir: .pytest_cache
rootdir: /Users/qiuzifeng/Desktop/CodePath 2026/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 14 items

tests/test_game_logic.py::test_parse_guess_number_in_text PASSED        [  7%]
tests/test_game_logic.py::test_parse_guess_with_phrase PASSED           [ 14%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED       [ 21%]
tests/test_game_logic.py::test_evaluate_guess_negative_number PASSED    [ 28%]
tests/test_game_logic.py::test_parse_guess_decimal_input PASSED         [ 35%]
tests/test_game_logic.py::test_evaluate_guess_decimal_input PASSED      [ 42%]
tests/test_game_logic.py::test_parse_guess_extremely_large_value PASSED [ 50%]
tests/test_game_logic.py::test_evaluate_guess_extremely_large_value PASSED [ 57%]
tests/test_game_logic.py::test_get_attempt_limit_values PASSED          [ 64%]
tests/test_game_logic.py::test_new_game_state_resets_values PASSED      [ 71%]
tests/test_game_logic.py::test_evaluate_guess_handles_guess_text PASSED [ 78%]
tests/test_game_logic.py::test_winning_guess PASSED                     [ 85%]
tests/test_game_logic.py::test_guess_too_high PASSED                    [ 92%]
tests/test_game_logic.py::test_guess_too_low PASSED                     [100%]

============================= 14 passed in 0.02s ==============================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
