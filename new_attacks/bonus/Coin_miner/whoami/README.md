# Coin Miner

## Whoami

### Build
```
docker build -t whoami .
```
### Run using localhost
```
docker run -d -P --network host whoami
```
### Run using ngrok url
Change the url inside conf.py

```
docker run -d -P whoami
```
