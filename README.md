# PinKIE

**PinKIE** - **P**i-based **in**-**K**itchen **I**nformation and **E**ntertainment

_A Raspberry Pi Display_

## Introduction

A wall-mounted display for the kitchen, using a Rasberry Pi Zero W and the gorgeous [Pimoroni Inky Impression](https://shop.pimoroni.com/products/inky-impression) 7-colour e-ink display.

Designed to show useful (and not-so-useful) information using a simple, card-based structure. Each card is a static, full-screen image showing pictures, text, graphics etc. There is a default card which is usually shown when idle. The four side-mounted buttons on the display can be used to cycle through groups of one or more alternative cards, which display for a while before reverting to the default. A background scheduler downloads new data and updates the card images.

## Hardware

* Raspberry Pi Zero WH
* Pimoroni Inky Impression display
* Micro SD card
* Micro USB power supply
* 3D-printed [wall-mount case](https://github.com/scripsi/inky-impression-case)

## Software Setup

Install the latest version of the Raspbian Lite operating system to the micro SD card using [Raspberry Pi Imager](https://www.raspberrypi.org/software/). Before ejecting the card, open the `/boot` partition and create two files:

1. an empty file called `ssh` - eg:

```shell
/boot $ touch ssh
```

2. a file called `wpa_supplicant.conf` containing the following:

```conf
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="[WIFI-SSID]"
    scan_ssid=1
    psk="[WIFI-PASSWORD]"
    key_mgmt=WPA-PSK
}
```

Eject the micro SD card and put it into the Raspberry Pi. Connect the power supply, wait for it to boot, and then SSH to it as the `pi` user with the default password of `raspberry`.

Use `raspi-config` to set the hostname and change the default password:

```shell
sudo raspi-config
```

Then update the software to the latest versions:

```shell
sudo apt update
sudo apt upgrade
```

Install and set up the Inky display, using Pimoroni's handy one-liner:

```shell
curl https://get.pimoroni.com/inky | bash
```

Install additional python packages:

```shell
sudo apt install python3-gpiozero python3-schedule python3-pandas
```

Update the python image library and dependencies:

```shell
sudo python3 -m pip install --upgrade Pillow
sudo apt install libopenjp2-7
```

## Creating images

Copy the palette file to `~/.config/GIMP/2.10/palettes`

legible colour schemes:

```
Background    Text
Black         White,Yellow,Orange
White         Black,Green,Blue,Red
Green         Black,White,Yellow,Orange
Blue          White,Yellow,Orange
Red           White,Yellow,Orange
Yellow        Black,Green,Blue,Red
Orange        Black,Green,Blue,Red
```