all: installdht

installdht:
	@echo "Install DHT11 dependencies - before containers"
	sudo pip3 install --upgrade setuptools
	sudo pip3 install adafruit-circuitpython-dht
	sudo apt-get install python3-libgiod
	sudo apt-get install libgpiod2
	sudo pip3 install requests
	sudo pip3 install git+git://github.com/pyeve/cerberus.git
	sudo reboot