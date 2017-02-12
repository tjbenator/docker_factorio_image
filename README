# Factorio Docker Container
Try to keep this Container as simple as I could. You can set any setting in `server-settings.json` with environment variables.


## Start new container

```bash
docker run -d \
  -v [PATH]:/opt/factorio/saves \
  -p [PORT]:34197/udp \
  tjbenator/factorio
```

## Environment Variables
Example usage:
```bash
docker run -d \
  --env FACTORIO_MAX_PLAYERS=30 \
  -v [PATH]:/opt/factorio/saves \
  -p [PORT]:34197/udp \
  tjbenator/factorio
```

Available Variables:
```bash
FACTORIO_ONLY_ADMINS_CAN_PAUSE_THE_GAME=True
FACTORIO_MAX_UPLOAD_IN_KILOBYTES_PER_SECOND=0
FACTORIO_IGNORE_PLAYER_LIMIT_FOR_RETURNING_PLAYERS=False
FACTORIO_REQUIRE_USER_VERIFICATION=True
FACTORIO_TAGS=['game', 'tags']
FACTORIO_ADMINS=[]
FACTORIO_AUTOSAVE_ONLY_ON_SERVER=True
FACTORIO_ALLOW_COMMANDS=admins-only
FACTORIO_AFK_AUTOKICK_INTERVAL=0
FACTORIO_USERNAME=
FACTORIO_DESCRIPTION="Description of the game that will appear in the listing"
FACTORIO_AUTOSAVE_SLOTS=5
FACTORIO_VISIBILITY_LAN=True
FACTORIO_VISIBILITY_PUBLIC=True
FACTORIO_AUTOSAVE_INTERVAL=10
FACTORIO_AUTO_PAUSE=True
FACTORIO_MAX_PLAYERS=0
FACTORIO_PASSWORD=
FACTORIO_MINIMUM_LATENCY_IN_TICKS=0
FACTORIO_NAME="Name of the game as it will appear in the game listing"
FACTORIO_TOKEN=
FACTORIO_GAME_PASSWORD=
```
