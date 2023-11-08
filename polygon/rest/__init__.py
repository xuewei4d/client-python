from .aggs import AggsClient
from .trades import TradesClient
from .quotes import QuotesClient
from .snapshot import SnapshotClient
from .indicators import IndicatorsClient
from .summaries import SummariesClient
from .reference import (
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
    ContractsClient,
)
from .vX import VXClient
from typing import Optional, Any
import os

BASE = "https://api.polygon.io"
ENV_KEY = "POLYGON_API_KEY"


class RESTClient(
    AggsClient,
    TradesClient,
    QuotesClient,
    SnapshotClient,
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
    ContractsClient,
    IndicatorsClient,
    SummariesClient,
):
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(ENV_KEY),
        connect_timeout: float = 10.0,
        read_timeout: float = 10.0,
        num_pools: int = 10,
        retries: int = 3,
        base: str = BASE,
        verbose: bool = False,
        trace: bool = False,
        max_conns_per_sec: int = 1,
        max_conns_time_span: float = 0.005,
        custom_json: Optional[Any] = None,
    ):
        super().__init__(
            api_key=api_key,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            num_pools=num_pools,
            retries=retries,
            base=base,
            verbose=verbose,
            trace=trace,
            max_conns_per_sec=max_conns_per_sec,
            max_conns_time_span=max_conns_time_span,
            custom_json=custom_json,
        )
        self.vx = VXClient(
            api_key=api_key,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            num_pools=num_pools,
            retries=retries,
            base=base,
            verbose=verbose,
            trace=trace,
            max_conns_per_sec=max_conns_per_sec,
            max_conns_time_span=max_conns_time_span,
            custom_json=custom_json,
        )
