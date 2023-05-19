# Violate the isolation of filesystem

## Jupyter Base Notebook

### Description
Setting "--volume src:dest" as sensitive parameter the host data are shared with container. With this specific project when running jupyter-base-notebook the data shared by the host is sent to the malicious web server.

### Build
```
docker build -t my-base-notebook .
```

### Preliminary steps

Before running the container:

- create a `data` folder inside the project and insert one or more files of your choice;
- start the [webserver](https://github.com/vitaleantonio/docker_attacks/tree/main/simple_web_server) to receive the data.

### Run using localhost
```
docker run -p 8888:8888 -v $(pwd)/data:/home/jovyan --network host my-base-notebook
```
### Run using ngrok url
Change the url inside conf.sh

```
docker run -p 8888:8888 -v $(pwd)/data:/home/jovyan my-base-notebook
```
