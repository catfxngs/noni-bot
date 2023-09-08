# Noni Discord Bot

Meow meow, meow. Meow!

<img src="assets/hat.jpg" alt="Noni wearing a sombrero." width="200"/>

Want to add the bot to your server? [Click here](https://placeholder/)! 

## Self-hosting

Make a new application on the [Discord Developer Portal](https://discord.com/developers/applications).

`$ pip install -r requirements.txt`

Create a `.dotenv` in the `/secret` directory and paste the following:

```
DISCORD_TOKEN=your.token.here
```

You can also modify the `config.json` file.

```json
{
    "PREFIX": "/"
}
```

If I have to tell you to **never** make your bot token public, you probably shouldn't be here.

`$ python3 noni.py`

### Docker

In progress.
