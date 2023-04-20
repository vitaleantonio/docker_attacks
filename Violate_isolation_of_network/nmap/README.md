# Violate the isolation of network

## Nmap

### Description
Setting "--network host" as sensitive parameter the host network is shared with container network. With this specific project when running Nmap all incoming connections are disabled for 60 seconds, after that incoming connections are re-enabled.

### Build
```
docker build -t my-nmap
```
### How to run
```
docker run --network host -it nmap <url-to-check>
```
