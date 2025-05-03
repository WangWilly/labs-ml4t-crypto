from pandas import DataFrame

from freqtrade.configuration import Configuration

from freqtrade.data.history import load_pair_history
from freqtrade.enums import CandleType

from freqtrade.data.dataprovider import DataProvider
from freqtrade.resolvers import StrategyResolver

from freqtrade.plot.plotting import generate_candlestick_graph
from freqtrade.data.btanalysis import load_backtest_data

################################################################################

def apply_strategy(config: dict[str, any], candles: list, pair: str) -> DataFrame:
    strategy = StrategyResolver.load_strategy(config)
    strategy.dp = DataProvider(config, None, None)
    strategy.ft_bot_start()

    # Generate buy/sell signals using strategy
    df = strategy.analyze_ticker(candles, {"pair": pair})

    # print(f"Generated {df['enter_long'].sum()} entry signals")
    # print(f"Generated {df['exit_long'].sum()} exit signals")

    # Filter out only the relevant columns
    df.drop(columns=["enter_long", "exit_long"], inplace=True)
    df.drop(columns=["enter_short", "exit_short"], inplace=True)
    data = df.set_index("date", drop=False)

    return data

################################################################################

if __name__ == "__main__":
    ############################################################################

    '''
    freqtrade download-data --config user_data/config.json --exchange binance --data-format-ohlcv user_data/data/binance/BTC_USDT_USDT-5m-futures.json --trading-mode futures --pairs "BTC/USDT:USDT" --days 10 --timeframes 5m

    freqtrade backtesting --config user_data/config_test.json --datadir user_data/data/binance --data-format-ohlcv json --strategy SampleStrategy --pairs "BTC/USDT:USDT" --timeframe 5m
    '''

    ############################################################################

    user_data_path = "user_data"
    cfg_path       = f"{user_data_path}/config.json"

    cfg_timeframe = "5m"              # Timeframe to analyze
    cfg_strategy  = "SampleStrategy"  # Name of the strategy class

    candle_pair        = "BTC/USDT:USDT"         # Pair to analyze - Only use one pair here
    candle_data_format = "json"                  # Data format to load
    candle_type        = CandleType.FUTURES      # Type of data to load (Futures or Spot)

    backtest_dir = f"{user_data_path}/backtest_results"

    ############################################################################

    config = Configuration.from_files([cfg_path])
    config["timeframe"] = cfg_timeframe
    config["strategy"] = cfg_strategy

    ############################################################################

    data_location = config["datadir"]
    candles = load_pair_history(
        datadir=data_location,
        timeframe=cfg_timeframe,
        pair=candle_pair,
        data_format=candle_data_format,
        candle_type=candle_type,
    )

    print(f"Loaded {len(candles)} rows of data for {candle_pair} from {data_location}")

    ############################################################################
    
    data = apply_strategy(config, candles, candle_pair)
    # print(data.columns)
    
    ############################################################################

    # Load backtested trades as dataframe
    trades = load_backtest_data(backtest_dir)

    # Show value-counts per pair
    pair = trades[trades["pair"] == candle_pair][["open_date", "close_date", "profit_ratio", "exit_reason"]]
    print(pair)

    ############################################################################

    # Generate candlestick graph
    graph = generate_candlestick_graph(
        pair=candle_pair,
        data=data,
        trades=trades,
        indicators1=[],
        indicators2=["rsi"],
    )
    graph.show(renderer="browser")
