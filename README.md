# Leekz Bot 

This bot manages the #leekz channel in the VEX UK server. It deletes any non-image messages, and creates a thread under any legitimate leekz.

## Dependencies

Dependencies are handled through a vanilla pip `requirements.txt`. Run `pip install -r requirements.txt` to install all dependencies.

## Discord.py

Discord.py is used as a framework for building a Discord bot, see https://discordpy.readthedocs.io/en/stable/ for more information on using Discord.py.

Discord.py requires an API token to start, see https://discordpy.readthedocs.io/en/stable/discord.html for more info.

## Environment Variables

The discord token will be loaded from an environment variable called `LEEKZ_TOKEN`. This can be either specified in the command line or through other means, or through a `.env` file in the same directory as `main.py`, which will be automatically loaded by `python-dotenv`.  

## Docker

A `Dockerfile` is provided to allow you to build a container image of your bot easily, which makes it easy to deploy the bot. `docker compose up` will build and run the container using the config specified in `docker-compose.yml`, including using the environment variables in `.env` to provide configuration. 

## GitHub Actions

GitHub Actions runs the CI jobs specified in `.github/workflows/ci.yml` on every push to `main`. The CI does a few things:

The CI will build a container image and publish it to `ghcr.io`, which allows you to easily share and deploy the bot anywhere. 

