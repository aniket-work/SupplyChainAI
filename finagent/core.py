import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta

class PortfolioManager:
    """Manages the portfolio state and rebalancing execution."""
    def __init__(self, initial_balance=100000):
        self.balance = initial_balance
        self.holdings = {
            "AAPL": 0.25,
            "MSFT": 0.25,
            "GOOGL": 0.25,
            "AMZN": 0.25
        }
        self.history = []

    def get_portfolio_value(self, prices):
        """Calculates total portfolio value based on current prices."""
        total_value = 0
        for ticker, weight in self.holdings.items():
            total_value += self.balance * weight # Simplified simulation logic
        return total_value

    def rebalance(self, new_weights):
        """Updates portfolio weights."""
        self.holdings = new_weights
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "weights": new_weights.copy()
        })
        return f"Rebalanced portfolio to: {new_weights}"

class SentimentAnalyzer:
    """Simulates sentiment analysis using LLM or heuristic."""
    def __init__(self):
        self.tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

    def analyze_news(self, news_items):
        """Analyzes sentiment for each ticker."""
        # In a real PoC, this would call GPT-4o
        # For this script, we'll return simulated sentiment scores (-1 to 1)
        sentiment_scores = {}
        for ticker in self.tickers:
            # Simulated logic: random sentiment for demonstration
            sentiment_scores[ticker] = np.random.uniform(-0.5, 0.5)
        return sentiment_scores

class RebalancingAgent:
    """Core Agent coordinating sentiment analysis and portfolio management."""
    def __init__(self):
        self.portfolio = PortfolioManager()
        self.analyzer = SentimentAnalyzer()

    def step(self, news_stream):
        """Performs one iteration of sentiment analysis and rebalancing."""
        sentiment_scores = self.analyzer.analyze_news(news_stream)
        
        # Strategy: Shift weights based on sentiment
        # If sentiment > 0.1, increase weight. If < -0.1, decrease.
        current_weights = self.portfolio.holdings
        adjustment_factors = {ticker: 1 + score for ticker, score in sentiment_scores.items()}
        
        raw_weights = {ticker: current_weights[ticker] * adjustment_factors[ticker] for ticker in self.tickers}
        total_raw = sum(raw_weights.values())
        new_weights = {ticker: weight / total_raw for ticker, weight in raw_weights.items()}
        
        result = self.portfolio.rebalance(new_weights)
        return result, new_weights, sentiment_scores

if __name__ == "__main__":
    agent = RebalancingAgent()
    news = ["Apple launches new AI chip", "Microsoft reports record earnings"]
    log, weights, scores = agent.step(news)
    print(log)
    print(f"Sentiment Scores: {scores}")
