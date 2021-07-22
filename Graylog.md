> [Wiki](Home) > [genie_python](genie_python) > [Graylog](Graylog)

# Graylog

[Graylog](https://docs.graylog.org/) is a logging framework which has a web interface that enables users to search logs, including custom fields on logs, historically. 

The plan for using Graylog is that we dump everything into it from various sources such as the GUI, blockserver and genie_python. Currently only genie_python uses graylog. It uses the `graypy` library to do add an extra logging handler. 

### Setting up Graylog using docker

Docker and `docker compose` can be used to spin up a local graylog server with all the dependencies - to do this use [this file](https://docs.graylog.org/en/4.0/pages/installation/docker.html#persisting-data), call it `docker-compose.yml` locally and run `docker-compose up`. You can use `docker-compose down` to kill Graylog and its dependencies this way as well. 

You will need to add a Graylog `GELF UDP` input on your local instance - this can done using the web interface and can be found under `System -> Inputs`

To access the web interface on a local machine you _must_ use `127.0.0.1:9000` - `localhost:9000` does not seem to work (possibly because of Docker network issues) 


### Adding inputs 

Graylog requires inputs to be specified before it starts taking logs. This can be done through the web interface via System -> Inputs 