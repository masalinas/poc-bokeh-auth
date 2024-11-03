# Description
A PoC with bokeh server with a custom basic login view

## STEPS

- **STEP01_2**: Execute application from embedded bokeh server bootstrap file

```
python boostrap.py
```

- **STEP02**: Build the docker image

Exec this command to build:

```
$ docker build -t poc-bokeh-auth .
```

- **STEP03**: run the docker container

Exec this command to run the container:

```
$ docker run --rm --name poc-bokeh-auth -p 5006:5006 poc-bokeh-auth
```

- **STEP04**: tag image docker image to be uploaded to azure

```
$ docker tag poc-bokeh-auth avibdocker.azurecr.io/poc-bokeh-auth:1.0.0
```

- **STEP05**: push image docker image

```
$ docker push avibdocker.azurecr.io/poc-bokeh-auth:1.0.0