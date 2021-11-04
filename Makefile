SHELL := /bin/bash

all: installdht setconfig

installdht:
	@echo "Install DHT11 dependencies - before containers"
	sudo apt install -y git
	sudo apt-get install python3-libgpiod
	sudo apt-get install libgpiod2
	sudo pip3 install git+git://github.com/pyeve/cerberus.git
	sudo pip3 install -r requiremenets.txt
	sudo reboot

MYPATH:=$(shell pwd)/.env
config:
	source $(MYPATH)