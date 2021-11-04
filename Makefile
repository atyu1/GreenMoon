SHELL := /bin/bash

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

MYPATH:=$(shell pwd)/.env
config:
	source $(MYPATH)