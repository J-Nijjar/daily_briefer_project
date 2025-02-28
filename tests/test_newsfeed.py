import pytest
import unittest
from unittest.mock import Mock, MagicMock
# from src.news_feed import get_news_feed

mock = Mock(return_value="Success")
print(mock())
mock_url = Mock(return_value="http://example.com/rss-feed")
print(mock_url())

def test_received_feed():
    pass