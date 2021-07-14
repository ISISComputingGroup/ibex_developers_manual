# Graylog

[Graylog](https://docs.graylog.org/) is a logging framework which has a web interface that enables users to search logs, including custom fields on logs, historically. 

The plan for using Graylog is that we dump everything into it from various sources such as the GUI, blockserver and genie_python. 

### Setting up Graylog using docker

Docker and `docker compose` can be used to spin up a local graylog server with all the dependencies - to do this use [this file](https://docs.graylog.org/en/4.0/pages/installation/docker.html#persisting-data). 