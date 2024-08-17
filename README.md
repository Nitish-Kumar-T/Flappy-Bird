# Flappy-Bird

This is a simple Flappy Bird clone developed using Python and Pygame. The objective of the game is to control a bird and navigate it through a series of pipes without hitting them. The score increases as the bird passes through the gaps between the pipes.

## Demo
[Screencast from 2024-07-10 09-47-58.webm](https://github.com/user-attachments/assets/95557c64-4431-4d28-825b-81f2031fd729)

## Features

- Smooth and responsive controls
- Infinite scrolling pipes
- Realistic gravity and physics
- Score tracking
- Game over and restart functionality

## Installation

### Prerequisites

1. **Python 3.x**: Make sure you have Python 3.x installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Pygame**: You need to install the Pygame library to run this game. You can install it using pip:

    ```bash
    pip install pygame
    ```

### Install the Game

1. Clone this repository or download the ZIP file and extract it to your desired location:

    ```bash
    git clone https://github.com/your-username/flappy-bird-clone.git
    cd flappy-bird-clone
    ```

### Add Required Assets

Ensure you have the following image files in the game directory:

- `bird.png`: The image of the bird.
- `pipe.png`: The image of the pipe.
- `background.png`: The background image.
- `gameover.png`: The game over image.

You can create your own images or download similar assets from the internet.

## Running the Game

Navigate to the game directory and run the game using the following command:

```bash
python main.py
```
## Gameplay Instructions
- **Controls**: Press the `Space` bar to make the bird fly upward. Release it to let the bird fall due to gravity.
- **Objective**: Navigate the bird through the gaps between the pipes without hitting them. The game ends if the bird hits a pipe or the ground.
- **Restart**: If the game ends, press the `Space` bar to restart.

## Customization

- You can modify the `screen_width` and `screen_height` variables to change the size of the game window.
- Adjust the `gravity` and `player.velocity` values to tweak the game physics.
- Customize the pipe spacing and size by modifying the `create_pipes()` function.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as you like.

## Credits

This game was developed using Python and the Pygame library. All images and assets are placeholders and can be replaced with your own designs.
