# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It looks normal and ran okay, but the logic doesn't seem to be working. I should have guess the number correctly but it still keep ask me guessing.

- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").
1. When I clicked 'New Game', nothing happened. No new game started.
2. There is no way to restart a game
3. The game logic doesn't seem to be working

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| click the button | Start a new game | Nothing happened
| 'guess 50' | too high｜not a number｜not a number |
| I followed the hints, kept go lower | eventually get to correct number, from 20 and 7 attempts | it stopped me at there's still 1 attempt left, and the actual num is 73| |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude copilot, ChatGPT

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Correct: For the restart game logistics, it said the rerun logistics does not reset the fields, stats, score, history, etc.
  I verify through checking the code myself, seeing if all the resets values AI suggested are there. Then checked with chatgpt again to double verify.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Incorrect/Misleading: Same problem trying to fix above, but at first, it asked me to change 'session_state key' directly. However, claude code doesn't know it's Streamlit and Streamlit doesn't allow to do that directly. I got to know the first suggestion was incorrect b/c there showed an error on the game website and used ChatGPT to verify the reason.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  By checking on the running app, to see manualy if the issue is resolved/ask AI to self check again.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  One test I ran using pytest was for checking the fixed game logic. There were a few rounds of test failures (guess too high and too low) but it fixed itself eventually.

- Did AI help you design or understand any tests? How?
  Yes. It helped me design pytest. I just asked it to create one for the last bug i fixed, then I run in the terminal to self check if everything is passed or not.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit's rerun is like playing a video. Everytime you starts the run, it goes from top to bottom (each line). If you restarts in the middle, it won't remeber anything, and will just starts from zero.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Create a pytest on every bug fixed is necessary. Before this practice, I don't have this habit.

- What is one thing you would do differently next time you work with AI on a coding task?
  Next time I'll ask it to review all the files as a whole and list out the possible places to fix. This probably helps save token. Because everytime I ask it to debug once, it runs through the file attached once.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  It doesn't help you magically fix everything. You have to manually review it yourself (& maybe double check with another AI bot) to make sure everything is fixed by the way you wanted.
