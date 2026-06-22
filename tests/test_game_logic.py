from logic_utils import (
    check_guess,
    evaluate_guess,
    get_attempt_limit,
    new_game_state,
    parse_guess,
)

def test_parse_guess_number_in_text():
    ok, value, error = parse_guess("guess 50")
    assert ok is True
    assert value == 50
    assert error is None


def test_parse_guess_with_phrase():
    ok, value, error = parse_guess("my guess is 50")
    assert ok is True
    assert value == 50
    assert error is None


def test_get_attempt_limit_values():
    assert get_attempt_limit("Easy") == 6
    assert get_attempt_limit("Normal") == 8
    assert get_attempt_limit("Hard") == 5


def test_new_game_state_resets_values():
    state = new_game_state("Easy")
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert 1 <= state["secret"] <= 20
    assert state["attempt_limit"] == 6


def test_evaluate_guess_handles_guess_text():
    result = evaluate_guess("guess 50", 50, 0, 1)
    assert result["ok"] is True
    assert result["guess"] == 50
    assert result["outcome"] == "Win"
    assert result["score"] == 80


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
