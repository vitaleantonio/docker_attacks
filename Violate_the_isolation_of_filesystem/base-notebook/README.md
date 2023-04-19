# Violate the isolation of filesystem

## Jupyter Base Notebook

### Build
```
docker build -t my-base-notebook .
```
### Run using localhost
```
docker run -p 8888:8888 -v $(pwd)/data:/home/jovyan --network host my-base-notebook
```
### Run using ngrok url
Change the url inside conf.sh

```
docker run -p 8888:8888 -v $(pwd)/data:/home/jovyan my-base-notebook
```
