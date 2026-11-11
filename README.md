# Around the Table

A multiplayer card game built in Python with Tkinter, using the Model–View–Controller
pattern. Originally written for 48024 Programming 2 at UTS, and rebuilt here with a
proper version control workflow, automated tests and continuous integration as part
of 43030 Professional Practice in Computing.

## What it does

Two to four players take turns drawing cards from a shared deck, placing them into a
temporary hand, and then committing them to their playing hand. Each card carries an
attack value, a style and a health value. Players select a card to play each round,
and the player with the highest total health when someone calls the game wins.

## Running it

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python LoginView.py
```

Enter at least two player names and press **Start Game**. The dealer window controls
the round; each player gets their own window.

## Project structure

```
.
├── LoginView.py          # Entry point — player setup
├── DealerView.py         # Dealer window: deal, play round, call
├── PlayerView.py         # Per-player window: hand and temp hand
├── DeckView.py           # Deck contents browser
├── CardView.py           # Single card image
├── ErrorView.py          # Error dialog
├── PlayerWinView.py      # End-of-game result
├── TkUtils.py            # Shared Tkinter styling helpers
├── model/                # Game logic — no UI dependencies
│   ├── player.py
│   ├── dealer.py
│   ├── login_model.py
│   └── exception/        # Domain exceptions
├── tests/                # Unit tests for the model layer
├── image/                # Card and UI artwork
└── .github/workflows/    # Continuous integration
```

## Architecture

The split between `model/` and the view classes is what makes the game testable. The
model holds all game logic and imports nothing from Tkinter, so it can be exercised
without a display. The view classes own the widgets and delegate every decision to the
model, surfacing domain exceptions (`EmptyDeckException`, `FullHandException`,
`RoundNotReadyException`) through `ErrorView` rather than handling them silently.

## Testing

```bash
pytest tests/ -v
```

Tests cover the model layer only. The view classes require a display and are verified
manually. CI runs the same command on every push and on every pull request to `main`.

## Development workflow

Work happens on feature branches and merges to `main` through pull requests. CI must
pass before a branch is merged.

```bash
git checkout -b feature/your-change
# make changes
git add -A
git commit -m "Describe the change"
git push -u origin feature/your-change
# open a pull request on GitHub
```

## Licence

Coursework project. Not licensed for reuse.
