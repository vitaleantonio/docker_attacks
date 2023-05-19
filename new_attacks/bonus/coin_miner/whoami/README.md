# Coin Miner

## Whoami

### Description
With this specific project when running whoami a malicious coinminer is started which sends the hash found to a malicious webserver.

### Build
```
docker build -t whoami .
```
### Preliminary steps

Before running the container you need to start the [webserver](https://github.com/vitaleantonio/docker_attacks/tree/main/simple_web_server) to get the hash.

### Run using localhost
```
docker run -d -P --network host whoami
```
### Run using ngrok url
Change the url inside conf.py

```
docker run -d -P whoami
```
