# docker-python-discord-bot

single docker container Discord bot built with Python and discord.py.

## Docker Compose configuration example

```yaml
services:
  discord-bot:
    image: ghcr.io/holeinonegolfer/docker-python-discord-bot:latest
    container_name: discord-bot
    restart: always
    environment:
      - DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    volumes:
      - ./bot:/data
```
