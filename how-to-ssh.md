# How to SSH into the PI ?


## Prerequisits

- you should configure the WIFI connection, hostname, username and password in the "Raspberry PI Imager" Software before Installing the OS on your SD Card
- also configure SSH connection to use "Passord" and not priv/pub Keys.


### On Windows:
- install putty
- ssh into it..

### on any linux:
- open terminal
- `ssh raspberrypi@THE-RASPBERRIES-IP-ADRESS`
-> yes
-> enter your password


## Problems?
Too many authentication failures?
ssh -o PreferredAuthentications=password <hostname_or_ip>