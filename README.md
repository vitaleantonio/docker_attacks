# About The Project

This repository is a collection of attacks created to exploit the "sensitive" parameters of Docker, searchable in [docker run reference](https://docs.docker.com/engine/reference/commandline/run/). A replication guide can be found in each directory.

The repository is organized as follows:

## Attacks replication

Replication of attacks on Docker referred to [Understanding the Security Risks of Docker Hub](https://www-users.cse.umn.edu/~kjlu/papers/docker.pdf).

The reference directory is [attacks_replication](https://github.com/vitaleantonio/docker_attacks/tree/main/attacks_replication).

## Novel attacks

They represent new attacks that aim to exploit "sensitive" Docker parameters and present in [new_attacks](https://github.com/vitaleantonio/docker_attacks/tree/main/new_attacks).

## A simple web server

A simple web server that allows the execution of some attacks, found in [simple_web_server](https://github.com/vitaleantonio/docker_attacks/tree/main/simple_web_server).

## Analysis results 

Through the use of the tools listed below, security analysis was performed on the created docker containers to see if they can detect the presence of inserted malicious scripts. The results can be found in [analysis_results](https://github.com/vitaleantonio/docker_attacks/tree/main/analysis_results).

The tools used are:

- [Snyk](https://snyk.io)
- [Trivy](https://trivy.dev)
- [Dockle](https://containers.goodwith.tech/)
- [Grype](https://github.com/anchore/grype)
