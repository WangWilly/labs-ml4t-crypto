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

## Development

### Prerequisites

- `brew install ta-lib`
- Poetry: `2.1.2` (package poetry `1.8.3`, installed using Python `3.12.4`)

```bash
# Install dependencies
poetry install
# Activate the virtual environment
poetry shell
```

### Prepare the data

- https://www.freqtrade.io/en/stable/data-download/

```bash
freqtrade download-data --config user_data/config.json --exchange binance --data-format-ohlcv user_data/data/binance/BTC_USDT_USDT-5m-futures.json --trading-mode futures --pairs "BTC/USDT:USDT" --days 10 --timeframes 5m
```

### Backtesting

```bash
freqtrade backtesting --config user_data/config_test.json --datadir user_data/data/binance --data-format-ohlcv json --strategy SampleStrategy --pairs "BTC/USDT:USDT" --timeframe 5m
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
