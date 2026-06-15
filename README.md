# docker-python-discord-bot

Just a simple Discord bot written in Python (discord.py) that runs inside a single Docker container.

## How to run it with Docker Compose

Create a docker-compose.yml file, throw your bot token in there, and point the volume to wherever your code lives.

```yaml
services:
  discord-bot:
    image: ghcr.io/holeinonegolfer/docker-python-discord-bot:latest
    container_name: discord-bot
    restart: always
    environment:
      - DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    volumes:
      # Maps your local data folder to the container's data folder
      - ./data:/data
```

Once that's set up, just run:

```bash
docker-compose up -d
```
