# Python RC Control
Uses GNURadio to record and replay RF signals, including doorbells, gate controls, car keys, and RC cars

## Setup
This script requires GNURadio Companion and its Python bindings to be installed. For this tutorial, it is assumed that the hardware being used to read and broadcast radio signals is the HackRF One, which can be purchased [here](https://greatscottgadgets.com/hackrf/)

### Ubuntu
Run

`sudo apt-get install gqrx`

which should install the Software Defined Radio (SDR) program GQRX and its dependencies on the system. Next, run

`sudo apt-get install osmocomsdr`

which will install the osmocom drivers.

### OS X
With MacPorts installed, run

`suod port install gqrx`

which will install GQRX and its dependencies. 

## Recording
Open `record.grc` and make sure the HackRF One is connected. Run the script and play your radio signal. This will store it in a raw file, or the file name specified in the `File Sink` block. 

## Playback
Open `replay.grc` and run the script. This will play your recorded signal.

## RC Control
To control an RC Car, record each signal -- forward, reverse, left, right, forward-left, forward-right, reverse-left, and reverse-right. Alternatively, signals are provided which will work with a 49 MHz RC car. Run

`python RCcontrol.py`

which will open up a blank window. Click on the window. Now, the keys Q, W, E, A, D, Z, X, and C will control the RC car. 
