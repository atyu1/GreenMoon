all: installdht

installdht:
	@echo "Install DHT11 dependencies - before containers"
	sudo pip3 install --upgrade setuptools
	pip3 install adafruit-circuitpython-dht
	sudo apt-get install libgpiod2
	sudo reboot
