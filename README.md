# Noni Discord Bot

Meow meow, meow. Meow!

<img src="assets/hat.jpg" alt="Noni wearing a sombrero." width="200"/>

Want to add the bot to your server? [Click here](https://placeholder/)! 

## Self-hosting

Make a new application on the [Discord Developer Portal](https://discord.com/developers/applications).

`$ pip install -r requirements.txt`

Run the bot with `$ python3 noni.py` or `$ py -3 noni.py` and enter your token.

If you choose to save it, a **.env** will be generated and remembered for the next run. The variable is ignored by git, but keeping your bot token in plaintext is always a risk. Please remember to **never share your token!** You can easily reset it in the portal.

Command prefixes and other variables can be modified in the `config.json` file.

```json
{
    "PREFIX": "/"
}
```

### Docker

In progress.

