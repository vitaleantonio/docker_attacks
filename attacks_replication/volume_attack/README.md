# Replication volume attack

## Volume attack

### Description
Setting "--v (HOST_PATH):(CONTAINER_PATH)" as sensitive parameter the (HOST_PATH) contents will be mounted in (CONTAINER_PATH). With this specific example when running this volume attack the (HOST_PATH) contents will be loaded in remote git repository.

### Build
```
docker build --build-arg VERSION=<GITHUB_TOKEN> . -t volume-attack
```
### How to run
```
docker run -t -d -v <HOST_PATH>:<CONTAINER_PATH> volume-attack
```
