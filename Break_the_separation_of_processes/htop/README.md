# Break the separation of processes

## Htop

### Description
Setting "--pid host" as sensitive parameter the host processes are shared with container processes. With this specific project when running Htop the Firefox pid will be killed.

### Build
```
docker build -t my-htop
```
### How to run
```
docker run -it --pid host myhtop
```
