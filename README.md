# imac_g3_osd_cli
## A python based CLI for making monitor adjustment to an iMac G3 over I2C from a raspberry pi.

This was tested on a raspberry pi 4 running Raspberry Pi OS Debian version: 11 (bullseye)

To use the script:
- Open a terminal and clone the repo.
```bash
git clone https://github.com/qbancoffee/imac_g3_osd_cli.git
```
- Change to the directory.
```bash
cd imac_g3_osd_cli 
```
- Make the install script executable.(although it already should be)
```bash
chmod +x ./install
```
- Install the script.
```bash
sudo ./install
```

At this point everything needed should be installed, so reboot the raspberry pi, log in, open a terminal and type the following.

```bash
sudo edit-ivad-init
```
The script is in the path so you should be able to run it from anywhere.

WRITE INSTRUCTIONS FOR USE HERE
