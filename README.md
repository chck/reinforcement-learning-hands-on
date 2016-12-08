# reinforcement-learning-hands-on

## Installation

- docker
- docker for Mac
- Xquartz (under 2.7.8)
- socat

### XQuartz

Make sure your pre-installed version is under 2.7.8.

[Download Xquartz 2.7.8](https://www.xquartz.org/releases/XQuartz-2.7.8.html)

After installation, restart your machine.

### socat

```
brew install socat
```

## Usage

### Prepare X Window

Type following commands in another console.

```
open -a XQuartz
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
...
```

### Run sample application

```
# pull container
docker pull chck/rl-hands-on

# or build container, if needed
#docker build . -t rl-hands-on

# check your ip address
IP_ADDR=
IP_ADDR=$(ifconfig en0 | grep "inet " | awk '{print $2};')
echo $IP_ADDR

# run container and
docker run -it -e DISPLAY=${IP_ADDR}:0 -v $(pwd):/work chck/rl-hands-on /bin/bash

# run sample application on container console
python ...  # FIXME
```

