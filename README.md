# Go CLI Game

A lightweight, terminal-based implementation of the strategic board game **Go**. The application provides a distraction-free command-line experience where two players can play on a configurable board while following core Go rules.

## Features

- Two-player local gameplay
- Configurable board size
- Black and White player names
- Terminal-based board display
- Standard Go coordinate notation
- Stone placement and turn management
- Capture of opponent groups
- Liberty checking
- Suicide move prevention
- Ko rule enforcement
- Pass functionality
- Game ends after both players pass
- Resignation support
- Help command
- Quit command
- Captured stone tracking
- JSON game-state storage
- Automated test suite

## Technologies

- **Python 3**
- **pytest**
- **JSON** for game-state storage
- Command-line interface (CLI)

## Project Structure

```text
go-cli-game/
│
├── app/
│   ├── game/
│   │   ├── board.py
│   │   ├── game.py
│   │   ├── player.py
│   │   ├── rules.py
│   │   └── stone.py
│   │
│   ├── persistence/
│   │   └── json_storage.py
│   │
│   └── ui/
│       ├── display.py
│       └── validators.py
│
├── tests/
│   ├── test_board.py
│   ├── test_cli.py
│   ├── test_game.py
│   ├── test_rules.py
│   └── test_storage.py
│
├── main.py
├── requirements.txt
└── pytest.ini


## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/codewithmDEV/go-cli-game
cd go-cli-game
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the game

```bash
python3 main.py
```
