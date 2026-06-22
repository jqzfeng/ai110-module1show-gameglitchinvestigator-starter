import random
import re

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def get_attempt_limit(difficulty: str):
    """Return the attempt limit for the selected difficulty."""
    attempt_limit_map = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    return attempt_limit_map.get(difficulty, 8)


def new_game_state(difficulty: str):
    """Return a fresh game state for a new game."""
    low, high = get_range_for_difficulty(difficulty)
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
        "low": low,
        "high": high,
        "attempt_limit": get_attempt_limit(difficulty),
    }


def evaluate_guess(raw_guess: str, secret: int, current_score: int, attempt_number: int):
    """Parse and evaluate a guess, returning structured result data."""
    ok, guess_int, err = parse_guess(raw_guess)
    if not ok:
        return {
            "ok": False,
            "guess": None,
            "error": err,
            "outcome": None,
            "message": None,
            "score": current_score,
        }

    outcome, message = check_guess(guess_int, secret)
    score = update_score(
        current_score=current_score,
        outcome=outcome,
        attempt_number=attempt_number,
    )
    return {
        "ok": True,
        "guess": guess_int,
        "error": None,
        "outcome": outcome,
        "message": message,
        "score": score,
    }

# FIX: parse numbers embedded in text like 'guess 50', using AI agent mode
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    match = re.search(r"[-+]?\d+(?:\.\d+)?", raw)
    if not match:
        return False, None, "That is not a number."

    try:
        text = match.group(0)
        if "." in text:
            value = int(float(text))
        else:
            value = int(text)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"  # FIX: Correct high guess hint, using AI agent mode

    return "Too Low", "📈 Go HIGHER!"      # FIX: Correct low guess hint, using AI agent mode


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
