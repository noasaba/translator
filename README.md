# Translator Discord Bot

This is a Discord bot that translates messages using the DeepL API. It is built using Python and can be deployed using Docker.

## How to Use

### 1. Pull & Build the Docker Image

Ensure you have Docker installed on your system. Follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>

    Build the Docker image:

    docker build -t translator-discord-bot .

2. Run the Docker Container

Run the container using the following command:

docker run -d --name translator-bot \
  -e DISCORD_TOKEN=<your-discord-token> \
  -e DEEPL_API_KEY=<your-deepl-api-key> \
  translator-discord-bot

Replace <your-discord-token> and <your-deepl-api-key> with your actual credentials.
3. Access Logs (Optional)

To view the bot's logs, use:

docker logs -f translator-bot

4. Stopping and Removing the Container

To stop the container:

docker stop translator-bot

To remove the container:

docker rm translator-bot

5. Updating the Bot

If there are updates to the bot:

    Pull the latest changes:

git pull

Rebuild the Docker image:

docker build -t translator-discord-bot .

Restart the container:

    docker stop translator-bot
    docker rm translator-bot
    docker run -d --name translator-bot \
      -e DISCORD_TOKEN=<your-discord-token> \
      -e DEEPL_API_KEY=<your-deepl-api-key> \
      translator-discord-bot

Enjoy using the Translator Discord Bot!
