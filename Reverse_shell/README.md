# Reverse shell

## Tcpdump

### Description
Setting "--network host" as sensitive parameter the host network is shared with container network (it is necessary since tcpdump is used to analyze network). With this specific configuration when runnig tcpdump a reverse shell is created having access to container files and to host network.
<br />
Setting "-v ($HOME):/app/data --network host" as sensitive parameters the host network is shared with container network and the user's "home" is loaded in container memory. With this specific configuration when runnig tcpdump a reverse shell is created, with this we have access to container files, host network and user's home.

### Usage
To make this work modify the ATTACKER'S IP in victim.py, otherwise it will only work locally.

### Build
```
docker build -t my-tcpdump
```
### How to run

#### Using only --network
```
docker run -it --network host my-tcpdump
```

#### Using --network and -v
```
docker run -it -v ($HOME):/app/data --network host my-tcpdump
```
