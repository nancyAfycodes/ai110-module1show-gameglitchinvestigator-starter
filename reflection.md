# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Some of the issues found on running the file includes:
  - score card was negative.
  - New game button does not work. Even if difficulty level was changed, it did not reflect the amount of guesses needed to complete the game
  - difficulty level did not match number range. For example, 'normal' game mode had a number guess range between 1 and 100. Hint keeps showing 'go LOWER' even though number guessed is outside of range.
  - Changing game difficulty did not change the game
  - Game history did not reset after selecting 'new game'. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- For this project, I used Claude. First, I stated the issues I was having with my code then copied my code into Claude to assist with debugging.
- An example of a correct suggestion was the 'hint' section. It noted that it the hint for either 'Go Higher' or 'Go lower' was reversed. To test, I reversed the hint an tried to play the game again. I chose 'Normal' and when I entered a guess that was to high or low, the hint provided matched. Here's the AI suggestion (below)
![alt text](image.png)

- In terms of misleading suggestion, AI did not comprehend that the number of guess and difficulty level have to work together. It suggested that I increase the guess range to 200. However, when I stated that the difficult level and number of guesses go together, it accepted my reasoning as seen below
![alt text](image-1.png)
---


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
- To test the bugs identified in part I, I ran several test to determine if the bugs were fixed once corrections were made. For example, the hint, 'go higher' or 'go lower' was reversed in the original code. With the correction, the hints after each guess matched guess until the correct guess was made.
Each test was designed using Claude, since I copied my code into AI prompt, I was able to ask it to generate a test that ensures that guesses and hint are in sync with each other
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
- I secret number keeps changing,because the session. state generate a random number each time a new game is played. Using random.randint, the game generate a random integer wach time a game is played.
- The simplest way to explain Streamlit is to state that it runs the game script from the beginning of the code each time the user plays the game. The 'session state' is a form of memory that saves each user interaction with the user
- To make the secret number stable, I removed the if/else conditional that compared the int (number guesses) to a string that's located in lines 162 - 163 in app.py file.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- I'd like to get more comfortable using AI to debug code. This is my real first attempt at using AI  to debug, and I have learned to state the issues experienced first then using AI to correct, rather than allow AI to make decisions on my behalf. This allows me to have better control and ensures that any changes are not made unexpectedly. 
- I have always thought of AI as a assistant rather than a tool that can be used to replace human thinking. I think AI is only effective if the user has control of the interaction and the user is not entirely dependent on AI for all decision making. 