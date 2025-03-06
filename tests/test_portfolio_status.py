from unittest.mock import patch, MagicMock
import yfinance
from src.portfolio_status import show_watchlist
from src.user import User

def test_watchlist():
    """Test that show_watchlist returns a list, containing lists of stock
    watchlist information.
    """

    mock_feed = MagicMock()
    mock_feed.tickers['stock'].info = {
        'currentPrice': 121,
        'regularMarketChangePercent': '1.5',
    }

    with patch('yfinance.Tickers', return_value=mock_feed):
        result = show_watchlist(['stock'])

        assert result == [
            ['stock', 121, '1.5%']
        ]