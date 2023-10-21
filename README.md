# G.R.IN.C.H
**G**PIO **R**aspberry **IN**terface for **C**limate and **H**eating


A simple, and incomplete, Project to setup a raspberry pi for reading temp sensors and controlling a fan's speed.
The sensor data is stored in a sqlite database, and the data is shown on a homepage in your local homenetwork.
Everything is written in python. 

## What is:

### raspberry pi
It's just a small computer with some kind of unix (linux) running on it. It has the GPIOs you can connect your sensors and fans to. 

### raspian OS
The operating system installed on the raspberry pi. Like windows/mac OS on your own PC. 
We need to install this on a new raspberry pi to do anything with it. 

### python3 (not python2)
The programming language we use to write code e.g."a script" that does everything we need to do for our project.
- Reading the sensors
- controlling the fan
- saving the data in the database
- reading the data from the database
- creating a webserver to show you the homepage

We need to install this so the raspberry pi undertands the code you write. (very probably already installed)

### sqlite3
A very lightweight SQL database. Your data will be saved in a file on your raspberry pi. This file "is the database" and the software sqlite3 knows how to write to/read form that file. If we want to be able to read the data later on without going insane, we need a structured way to save it first. SQL is our structured way. 

### flask
A webserver framework written in python, it also can handle templage generation.

What does that mean? 
A bunch of python functions to make setting up a webserver and the homepage easier for us. 

## Prerequisites you may not have:
- Bring a monitor, mouse and keyboard. This makes working with a raspberry pi easier. 
- if you have a old raspberry, check if it has build-in WIFI. You may need a WIFI-USB-dongle if it is not built-in. Ask whoever gave you the raspberry if they have it. Not all dongles you can buy will work.
- If it has wifi -> check its IP in your routers "local homepage"
- or bring a "crosslink" network cable to connect your own PC to the raspberry
- or bring a normal netwock calbe and plug your raspberry into your home router -> check its IP in your routers "local homepage"


## Read Tutorials like this:

### Raspberry itself
https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html
https://www.raspberrypi.com/software/
### GPIO
https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
### Local Webserver 
https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/1
### Database
https://www.pythonforthelab.com/blog/storing-data-with-sqlite/
https://randomnerdtutorials.com/sqlite-database-on-a-raspberry-pi/
https://pimylifeup.com/raspberry-pi-sqlite/
### DC Fans
https://www.digikey.com/en/maker/tutorials/2019/how-to-control-a-dc-fan-using-the-raspberry-pi
### Sensors
https://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/


## How to set up your Raspberry PI
0. If you got a raspberry pi from your university, it may already have an OS installed. 
 If that is the case, skip installing a new OS might save you some time, but you may have to fight with the already installed software from previous users
1. install the OS for your PI on an SD Card  (see step 2 before installing it)
https://www.raspberrypi.com/software/

2. configure the PI installations network, so the PI can connect to your local network.
3. Insert it into your PI, connect your pi to power and wait a couple minutes. 

`If you have no idea what SSH is, just plugin a monitor, mouse and keyboard in your raspberry. it is way easier` 

4. connect to the PI via SSH  (if you dont have a monitor, mouse and keyboard at hand)




# 0) Configure your PI
0. sudo apt update
1. install python3 if not already preinstalled
2. install sqlite3

## 1) clone the repo
git clone https://github.com/EliasPh/GRINCH.git
cd GRINCH

## A) Install the Database
1. sudo apt-get install sqlite3
you can ignore:
`perl: warning: Setting locale failed. perl: warning: Please check that your locale settings:...`

2. create your database
enter `sqlite3 sensordata.db` 
then enter the following

```
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> CREATE TABLE sensorA(id INTEGER PRIMARY KEY AUTOINCREMENT, temperature NUMERIC, currentdate DATE, currenttime TIME, device TEXT);
sqlite> CREATE TABLE sensorB(id INTEGER PRIMARY KEY AUTOINCREMENT, temperature NUMERIC, currentdate DATE, currenttime TIME, device TEXT);
sqlite> CREATE TABLE fanRPM(id INTEGER PRIMARY KEY AUTOINCREMENT, fanspeed NUMERIC, currentdate DATE, currenttime TIME, device TEXT);
sqlite> COMMIT; -> this might fail, dont worry
sqlite> .quit
```
you will find the file sensordata.db in your current directory



## A) Install Flask
`> pip3 install flask`

```
raspberrypi@raspberrypi:~/my-project/GRINCH $ pip3 install flask
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: flask in /usr/lib/python3/dist-packages (1.1.2)

```

## How to start the server
> python "path to where you cloned the repo/GRINCH/the-actial-code/webserver.py



## Things you may have to think about
- The fan you will use may be 12V or 5V and can have different amps. If you are powering the fan directly from the raspberry, you should read up if you can fry your raspberry with a 12V fan. Brush up your electrotechnical knowledge and/or google something like "raspberry pi 12V 0.12A fan"


## Troubleshooting
- Downloaded an img but it is .xy ?
https://www.cyberciti.biz/faq/how-to-extract-tar-xz-files-in-linux-and-unzip-all-files/