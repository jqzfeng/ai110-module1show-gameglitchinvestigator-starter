import streamlit as st
from logic_utils import (
    evaluate_guess,
    get_attempt_limit,
    get_range_for_difficulty,
    new_game_state,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit = get_attempt_limit(difficulty)

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    new_state = new_game_state(difficulty)
    st.session_state.secret = new_state["secret"]
    st.session_state.attempts = new_state["attempts"]
    st.session_state.score = new_state["score"]
    st.session_state.status = new_state["status"]
    st.session_state.history = new_state["history"]

if "attempts" not in st.session_state:
    st.session_state.attempts = 0  # FIX: Start at zero so first submit is attempt 1, using AI agent mode

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

# Use an on-click callback for the New Game button so we modify session_state
# before Streamlit re-runs and re-instantiates widgets (avoids APIException).
def new_game_callback(difficulty_arg):
    new_state = new_game_state(difficulty_arg)
    st.session_state.attempts = new_state["attempts"]
    st.session_state.secret = new_state["secret"]
    st.session_state.score = new_state["score"]
    st.session_state.status = new_state["status"]
    st.session_state.history = new_state["history"]
    guess_key = f"guess_input_{difficulty_arg}"
    st.session_state[guess_key] = ""
    st.success("New game started.")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button(
        "New Game 🔁",
        on_click=new_game_callback,
        args=(difficulty,),
    )
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# FIXME: Here doesn't work as expected. fixed once.
# FIX: Restart the game logistics using AI agent mode

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    result = evaluate_guess(
        raw_guess,
        st.session_state.secret,
        st.session_state.score,
        st.session_state.attempts,
    )

    if not result["ok"]:
        st.session_state.history.append(raw_guess)
        st.error(result["error"])
    else:
        st.session_state.history.append(result["guess"])

        if show_hint:
            st.warning(result["message"])

        st.session_state.score = result["score"]

        if result["outcome"] == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
