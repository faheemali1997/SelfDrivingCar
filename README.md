#Control an RC car with Arduino

This repository contains the code for creating a self driving model RC Car. The RC car is controlled via an arduino board and uses image processing to collect the data and neural networks to predict the driving of car. The image is fed via an iphone places on top of the model RC Car.

##Requirements

* Python 3
* Arduino IDE

##Example usage

Open `rc-car-arduino` with your Arduino IDE and upload the sketch to your Arduino board.

Open `serial_controller_gui.py` with a text editor and change the serial port in the constructor to match your needs. Then run the script with:

```bash
python serial_controller_gui.py
```

Press W, A, S, D keys to control your RC car.
