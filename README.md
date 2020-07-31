# RESTful-Mininet-Ryu

Ryu SDN controller with RESTful Mininet.

## Prerequisite

* [run_containers.py](https://github.com/ngcdi-cam/run_containers)

## Getting Started


### Start with `run_containers.py` in Docker containers

Create the docker network. You only need to do this once.

```
$ docker network create mas-network
```

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
* [Mininet](http://mininet.org/)
* [Ryu](https://ryu-sdn.org/)
