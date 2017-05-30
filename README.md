# Ultimate TicTacToe Python Player Samples

Here you will find samples of Ultimate TicTacToe player algorithm written in Python.
These samples exist to get you up and running quickly for a UTTT competition.

## Prerequisites

You'll need to have python3 installed. See https://www.python.org/downloads/ for instructions, and download the latest version (3.6).
Once that's done, you need to install the ultimate_ttt package on which this player depends:

`sudo pip3 install ultimate_ttt`

## Setting up the project

We recommend you fork this repository, then work from that.
Alternatively, you can also clone it using: 

`git clone https://github.com/socialgorithm/uttt-player-py.git`

After you have cloned either the fork or the original repository, switch to the uttt-player-py directory and install the local package:

`sudo pip3 install .`

Run tests to make sure you have completed the setup correctly:

`python3 setup.py test`

## Starting work
After this, you can start work on your player. 
We have provided the `ultimate_ttt_player/random_player.py` file to get you started.

The _only_ method you need to edit to improve this player is `get_my_move` (line 25) - and any other method that this would call.
You can see that the random player just picks a valid board at random, then a valid position within that board. You can obviously do better... ;)

After you have made some changes, make sure to test your player works properly:

```
sudo pip3 install . --upgrade
python3 setup.py test
```

For the more advanced competitors, feel free to rename your player to something else e.g. `ninja_player.py`  - but make sure you have a corresponding testing file and wrapper file.

## Further testing

If you think you have a good approach, you can test your player against a random one using *uabc*:

`uabc -p -f -g 100 “python3 samples/random_player_wrapper.py”`

See https://socialgorithm.org/ultimate-ttt-docs/sections/player/testing_locally.html for more instructions, including how to setup uabc.

## I'm ready for battle!

You'll be using *uabc* to play against others on the day; check with us for the exact command to run.



