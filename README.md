# Labs for Freqtrade

## Freqtrade Docker Setup

This is a simple setup for Freqtrade using Docker. It uses the official Freqtrade Docker image and sets up a basic configuration.

### Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine
- Basic knowledge of Docker and Docker Compose
- https://www.freqtrade.io/en/stable/docker_quickstart/
- https://github.com/ccxt/ccxt/?tab=readme-ov-file

### Setup Instructions

```bash
mkdir ft_userdata
cd ft_userdata/
# Download the docker-compose file from the repository
curl https://raw.githubusercontent.com/freqtrade/freqtrade/stable/docker-compose.yml -o docker-compose.yml

# Pull the freqtrade image
docker compose pull

# Create user directory structure
docker compose run --rm freqtrade create-userdir --userdir user_data

# Create configuration - Requires answering interactive questions
docker compose run --rm freqtrade new-config --config user_data/config.json
```

### Running Freqtrade

```bash
# Start the Freqtrade bot
docker compose up -d
```

## MISC

### Readings

- https://github.com/PacktPublishing/Machine-Learning-for-Algorithmic-Trading-Second-Edition_Original

### Data

- https://www.algoseek.com/data-drive.html
- https://finviz.com/calendar.ashx

### Indicators

- https://en.wikipedia.org/wiki/Kelly_criterion

### Libraries

- https://github.com/microsoft/qlib
- https://github.com/mementum/backtrader
- https://zipline.ml4trading.io/
