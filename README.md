# RESTful-Mininet-Ryu

Ryu SDN controller with RESTful Mininet.

## Prerequisite

* [run_containers.py](https://github.com/ngcdi-cam/run_containers)

## Getting Started

Clone the repo first

```
$ git clone https://github.com/ngcdi-cam/restful-mininet-ryu --recursive --depth=1
```

Please note the `--recursive` flag.

### Start with `run_containers.py` in Docker containers

#### Creating the Docker network

Create the docker network. You only need to do this once.

```
$ docker network create mas-network
```

#### Building the Docker images

```
$ cd mininet
$ docker build -t mbyzhang/mininet .
$ cd ../ryu
$ docker build -t mbyzhang/awareness . 
```

#### Running the containers

Then, run

```
$ run_containers.py -c ryu-config.yaml
$ run_containers.py -c mininet-config.yaml
```

or run `./start.sh`.

---

To stop, run

```
$ docker stop mnet1 ryu-sdn-1
```

or run `./stop.sh`

### Start manually

Run 

```
$ ./ryu/ryu_stp_switch start        # start Ryu in background. To stop, replace `start` with `stop`
$ # ./ryu/ryu_stp_switch start-fg   # alternatively, start Ryu in foreground, which is useful for debugging
$ ./mininet/mininet_rest start      # (as root) start Mininet in background
$ # ./mininet/mininet_rest start-fg # alternatively, start Mininet in foreground
```

## Customizing
### Mininet

See `mininet/mininet_rest.conf`.

## Contributors

* Peter Zhang: the scripts
* Marco Perez Hernandez: Project ideas and Docker images

## Credit

* [mininetRest](https://github.com/cgiraldo/mininetRest)
* [ryu-network-awareness](https://github.com/ngcdi-cam/ryu-network-awareness)
* [Mininet](http://mininet.org/)
* [Ryu](https://ryu-sdn.org/)
