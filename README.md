## Features

- Player-controlled spaceship movement and rotation
- Shoot projectiles with cooldown handling
- Random asteroid spawning from screen edges
- Asteroid collision detection
- Asteroid splitting mechanics
- Game-over detection
- JSON-based game state and event logging system

## Technologies Used

- Python
- Pygame
- Object-Oriented Programming (Inheritance & Polymorphism)
- Vector mathematics (`pygame.Vector2`)
- JSON logging

## Project Structure

```
main.py             # Main game loop
player.py           # Player movement and shooting
asteroid.py         # Asteroid behavior and splitting
asteroidfield.py    # Asteroid spawning system
shot.py             # Projectile logic
circleshape.py      # Base class for game objects
constants.py        # Game configuration values
logger.py           # Event and game-state logging
```

## How to Run

### Install dependencies

```bash
uv sync
```

or

```bash
pip install pygame
```

### Start the game

```bash
uv run main.py
```

## Controls

| Key | Action |
|------|---------|
| W | Move forward |
| S | Move backward |
| A | Rotate left |
| D | Rotate right |
| Space | Shoot |

## What I Learned

Through this project I gained hands-on experience with:

- Building a real-time game loop
- Working with inheritance and reusable base classes
- Managing game objects using sprite groups
- Using vectors for movement and rotation
- Implementing collision systems
- Logging application state for debugging and analysis
