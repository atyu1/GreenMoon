all: installdht setconfig

installdht:
	@echo "Install DHT11 dependencies - before containers"
	sudo apt install -y git
	sudo pip3 install --upgrade setuptools
	sudo pip3 install adafruit-circuitpython-dht
	sudo apt-get install python3-libgpiod
	sudo apt-get install libgpiod2
	sudo pip3 install requests
	sudo pip3 install git+git://github.com/pyeve/cerberus.git
	sudo reboot

setconfig:
	export GREENMOON_ROOM="test_room"
	export GREENMOON_LOCATION="test_location"
	export GREENMOON_NAME="test_name"
	export GREENPLANET_URL="http://localhost:8080/api/v1"