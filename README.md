# Chess.com-AI
A Python program that takes screenshots of the `chessboard`  while playing on `chess.com`  and uses  `STOCKFISH`  to generate the best possible move and uses `pyautogui` to make the moves on the website.

It can play in 
- Both as BLACK and WHITE
- RAPID
- BLITZ
- BULLET MATCHES

with almost `99% ACCURACY`

### What steps you have to follow??
- Download or clone my Repository to your device
- type `pip install -r requirements.txt` in command prompt(this will install required package for project)
- Make sure to install the modren version of `STOCKFISH` from [STOCKFISH](https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-windows-x86-64-avx2.zip) and add it to the system path.
- You should adjust the screenshot co-ordinates based on your display ratio so that the screenshot function only take the screenshot of the `CHESSBOARD`
- Make sure to change the chessboard theme setting as given below and enable auto-promote to queen.
- Just run the `chess.com RAPID FINAL.py` or  `chess.com BULLET Final.py`
<img src='https://github.com/MusadiqPasha/Chess.com-AI/blob/main/settings.png'>

### Project flow & explaination

- After you run the project , the program will detect if we are playing as BLACK or WHITE and flips the board if we're playin as BLACK.
- It'll automatically take the `SCREENSHOT` of the given chessboard region into `FEN NOTATION` when our timer starts.
- It'll send the `FEN NOTATION` to `STOCKFISH` to generate the BEST MOVE.
- You can adjust `STOCKFISH` LEVEL and DEPTH to generate the move more accurately.
- Then the program will move the 'MOVE' suggested by `STOCKFISH` on the `CHESSBOARD` 
  
### Screenshots

<img src='https://github.com/MusadiqPasha/Chess.com-AI/blob/main/input.png'>

## Disclaimer : This chess.com bot is intended solely for educational purposes. Any use of this bot in a real-world context is strongly discouraged. The author and contributors of this bot take no responsibility for any consequences resulting from its use in any context other than educational experimentation and learning.

## Acknowledgement : 
This project uses files from the "tensorflow_chessbot" GitHub repository of [Exiledz](https://github.com/Exiledz), which is available at [tensorflow_chessbot](https://github.com/Exiledz/tensorflow_chessbot). 
The following files from that repository have been incorporated into this project:
- [chessboard_finder](https://github.com/MusadiqPasha/Chess.com-AI/blob/main/chessboard_finder.py)
- [frozen_graph](https://github.com/MusadiqPasha/Chess.com-AI/blob/main/frozen_graph.pb)
- [helper_functions](https://github.com/MusadiqPasha/Chess.com-AI/blob/main/helper_functions.py)
- [helper_image_loading](https://github.com/MusadiqPasha/Chess.com-AI/blob/main/helper_image_loading.py)
- [tensorflow_chessbot](https://github.com/MusadiqPasha/Chess.com-AI/blob/main/tensorflow_chessbot.py)


## Just follow me and Star⭐ my repository 
## Thank You!!

