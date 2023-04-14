# E-Paper Micropython Implementation

This repository contains the code for implementing E-Paper display using Micropython. The code is written for the Waveshare E-Ink 3.7 Inch Display using a Raspberry Pi Pico W board and uses the self-implemented E-Paper module for displaying the content.

## Dependencies

The following dependencies are required to run the code:

- [Micropython](https://micropython.org/)
- [PicoZero](https://github.com/RaspberryPiFoundation/picozero)

## Installation

1. Download and install Micropython firmware on your ESP32 board.
2. Install the dependencies by running the following commands:

    ```
    $ ampy --port /dev/ttyUSB0 put picozero.py
    ```

3. Clone this repository:

    ```
    $ git clone <https://github.com/rohit1901/e-paper.git>
    ```

4. Upload the code to your ESP32 board:

    ```
    $ ampy --port /dev/ttyUSB0 put main.py
    ```


## Usage

1. Follow the Raspberry Pi Pico W Official Guide [https://projects.raspberrypi.org/en/projects/get-started-pico-w](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
2. Connect the ESP32 board to your computer using Thonny IDE.
3. Update the SSID and PASSWORD in lib/constants.py
4. The code should automatically run on connecting the Pico W to a power source.

## License

This project is licensed under the MIT License - see the LICENSE file for details.