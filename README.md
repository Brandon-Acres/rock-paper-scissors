# Rock Paper Scissors (with Lizard-Spock Extension)

A command-line Rock Paper Scissors game written in Python, featuring modular design, extendable rules (like Lizard-Spock), and unit/integration testing.

---

## Features

- Play against a random computer opponent
- Modular architecture using template game class and player interface.
- pluggable player types (user or computer)
- manual and automated test support with `pytest`
- extendable rulesets (e.g. Lizard-Spock)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Brandon-Acres/rock-paper-scissors.git
cd rock-paper-scissors
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate # macOS/Linux
# OR
.venv\Scripts\activate # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
To use pytest for testing:
```bash
pip install pytest
```

---

## Running the Game

Run the app from the `src/` folder like this:
```bash
cd src
python -m rock_paper_scissors
```

## Running Tests
Run all automated tests from the project root:
```bash
pytest
```
Run a specific test file:
```bash
pytest tests/test_basic_rps_game.py
```


## Project Structure:

```bash
rock-paper-scissors/
│   LICENSE
│   pytest.ini
│   README.md
│   requirements.txt
│
├───.pytest_cache
│   
│
├───src
│   └───rock_paper_scissors
│       │   menu.py                     # CLI menu logic
│       │   __init__.py
│       │   __main__.py                 # App entry point
│       │
│       ├───games                       # Game logic
│       │   │   basic_rps_game.py
│       │   │   template_rps_game.py
│       │   │   __init__.py
│       │   │
│       │   └───__pycache__
│       │           
│       │
│       ├───moves                       # Move set definitions
│       │   │   basic_moves.py
│       │   │   lizard_spock_moves.py
│       │   │   move_set.py
│       │   │
│       │   └───__pycache__
│       │           
│       │
│       ├───players                     # Player types
│       │   │   iplayer.py
│       │   │   random_computer_player.py
│       │   │   user_player.py
│       │   │   __init__.py
│       │   │
│       │   └───__pycache__
│       │           
│       │
│       ├───rules                       # Rule definitions
│       │   │   basic_rules.py
│       │   │   lizard_spock_rules.py
│       │   │
│       │   └───__pycache__
│       │           cpython-311.pyc
│       │
│       └───__pycache__
│               
│
└───tests                              # unit and integration tests
    │   test_app_flow.py
    │   test_basic_rps_game.py
    │   test_lizard_spock_basic_rps_game.py
    │   test_main_menu.py
    │   test_random_computer_player.py
    │   test_user_player.py
    │
    ├───manual_tests                    # Manual tests
    │       manual_test_basic_rps_game.py
    │
    └───__pycache__
```