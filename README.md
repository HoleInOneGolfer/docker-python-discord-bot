# docker-python-discord-bot

single docker container Discord bot built with Python and discord.py.

## Docker Compose configuration example:

```yaml
services:
  discord-bot:
    build: .
    container_name: discord-bot
    restart: always
    environment:
      - DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    volumes:
      - ./bot:/data
```
