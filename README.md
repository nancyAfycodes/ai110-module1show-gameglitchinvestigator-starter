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
-   Purpose of the game is to guess a number, depending on difficulty - easy, normal or hard, based on number of attempts. 
- [ ] Detail which bugs you found.
-    Some of the bugs found include, incorrect hints, adjusting number range to match difficulty level for the game, stablizing the secret number for each guess. 
- [ ] Explain what fixes you applied.
-    Reversed the hints for 'go lower or higher' to reflect the correct hint when a number is selected. In addition, I adjusted the number range for each level to account for uniformity. Furthermore, I removed the if/else conditional, in lines 162-164 in apppy file to allow for consistent guess each time the user plays the game.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]. Images shows hint of Go lower and higher working in the correct order.
<img width="2852" height="1606" alt="image" src="https://github.com/user-attachments/assets/d23703c4-d08a-4ab7-833f-aa03ffa2002c" />

<img width="2876" height="1654" alt="image" src="https://github.com/user-attachments/assets/a5d563c5-5a5f-42f9-94d3-b06c2c810000" />



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
