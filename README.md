## About me

This is an interview project, with a micro dockerized webapp that allows to select two numerical columns of several car models from a PosgreSQL database and plot it using [Python Plotly Dash](https://dash.plotly.com/layout).

Also with a [Jupyter Notebook](https://jupyter.org/) file which explains how to plot a sine wave from a given picture and answering a logical question.

## Try it on

On the exercise_1 folder, test locally by adding a `DATABASE_URI` on `.env` file and running the following [Docker](https://docs.docker.com/) commands.

```console
$ docker build -t crossnova-test .
```

```console
$ docker run -d -p 5000:5000 crossnova-test
```

## AWS 

The [application](http://54.226.114.43:5000/) is hosted in a AWS cluster with IP `54.226.114.43` and PORT `5000`.
