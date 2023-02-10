# Swarm Game

**Swarm Game** is a simple game I threw together with the Python Arcade engine.
The object of the game is to pick up all of the jewels that appear on screen, while avoiding all the poison bubbles.
You control your character using the mouse (or trackpad, or whatever you use to move the mouse cursor on your computer), and you pick up the jewels by touching them. You "die" if you touch the poison.

Press "Q" to quit at any time, and press "P" to pause the game.

The game's name, which isn't very unique, I know; comes from the fact that everything that appears on screen is coming at you from the left, right, top, and bottom; and there is a lot of it "swarming" the player. I believe this game is called a "Bullet Hell."

The purpose for writing this game was for me to learn how a game engine worked. I was also itching to pick up Python again, having been using other languages for quite some time now. It was pretty neat.

[Software Demo Video](https://youtu.be/MLXRm49_1x4)

## "build" Instructions

To build this game from source, you need Python 3. I used 3.10.5, but I'm sure newer versions of Python 3 will work just fine.
You will also need Python Arcade. Just run `pip install arcade` if you don't have it.
There is only one Python file, but there are a few PNG and WAV files that are needed. Make sure the "images" and "sfx" directories are right next to "swarmgame.py."
Run the swarmgame.py, and you should be good to go!

No executable binary is made, so you aren't really "bulding" anything, but whatever. It works and that's what matters.

## Tools used

Notepad++. I normally use Vim, but this was the editor I picked this time around.
I used Python 3 with the Python Arcade and Random libraries. 
Also used GIMP, the GNU Image Manipulation Program, for editing some of the sprites.

## License

Swarm Game is licensed under the MIT License. The assets however are are covered by other Free Software licenses.
In any case, Swarm Game is Free and Open Source software.

## Useful Websites

* [Jon Fincher's Python Arcade tutroial on Real Python](https://realpython.com/arcade-python-game-framework/)
* [Official website for the Python Arcade library](https://api.arcade.academy/en/latest/index.html)
* [GeeksforGeeks](https://www.geeksforgeeks.org/)
* [Paul Vincent Craven's 2D Game tutorial with Python Arcade on opensource.com](https://www.geeksforgeeks.org/)
* [Wikimedia Commons (where I got my images from)](https://commons.wikimedia.org/wiki/Main_Page)

## Credits

The player sprite in the game is the Firefox icon from the Crystal Icons project. It was made by Everaldo Coelho, and is licensed under the GNU Lesser General Public License v2.1.

Firefox is a trademark of Mozilla. I hope they don't mind.

The poison sprite is made by someone under the alias of 7Soul1. It is licensed under the Creative Commons CC0 1.0 Universal Public Domain Dedication.

The diamond sprite is made by someone under the alias of gubrww. It is licensed under the Creative Commons CC0 1.0 Universal Public Domain Dedication.

The sound effects came from KDE 2, which was developed by the KDE Free Software community. I don't know exactly who made the sounds, but they are licensed under the GNU Lesser General Public License v2.1.

## Future Work

* The code quality could use some TLC, and it also needs some performance tweeks.
* The algorithms for how the sprites are being spawned needs work.
* Adding a start screen would be nice.
* Adding a reset key would also be nice.
* At some point, I would like to use my own assets instead of borrowing others' work.
