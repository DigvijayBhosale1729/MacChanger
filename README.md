# MacChanger
A command line tool to change your MAC Address on a Linux/Unix based machine using ifconfig.

## Usage

**Remember to become sudo before using this script using**
```
sudo su
```

Execute the script using 
```
python3 macChanger.py [options]
```
##### The Various Options are listed below and can be accessed using ```--help```

```
Usage: macChanger.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface that needs a MAC Address Change
  -m NEW_MAC, --mac=NEW_MAC
                        The New MAC Address that we want
```

