from logic_utils import check_guess
from logic_utils import update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Pytest generated with Claude
# Test that winning early gives a high score
def test_win_early_attempt():
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10 * 1 = 90

def test_win_later_attempt():
    score = update_score(0, "Win", 5)
    assert score == 50  # 100 - 10 * 5 = 50

# Test that score never drops below minimum 10 points for a win
def test_win_minimum_points():
    score = update_score(0, "Win", 10)
    assert score == 10  # would be 0 but clamped to 10

# Test that Too High always deducts points (no more +5 reward)
def test_too_high_deducts():
    score = update_score(100, "Too High", 2)  # even attempt, used to give +5
    assert score == 95  # should always deduct 5

def test_too_high_deducts_odd():
    score = update_score(100, "Too High", 3)  # odd attempt
    assert score == 95

# Test that Too Low always deducts points
def test_too_low_deducts():
    score = update_score(100, "Too Low", 1)
    assert score == 95