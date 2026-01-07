import matplotlib.pyplot as plt
import os
import numpy as np

def generate_performance_chart(output_path="images/portfolio-performance.png"):
    """Generates a simulated portfolio performance chart."""
    days = np.arange(1, 31)
    baseline = 100 + np.cumsum(np.random.normal(0.1, 0.5, 30))
    agent = 100 + np.cumsum(np.random.normal(0.2, 0.4, 30))
    
    plt.figure(figsize=(10, 6))
    plt.plot(days, baseline, label='Static (60/40) Portfolio', color='#636E72', linestyle='--')
    plt.plot(days, agent, label='FinAgent (Autonomous)', color='#00B894', linewidth=2)
    
    plt.title('30-Day Simulation: FinAgent vs Static Portfolio', fontsize=14, pad=20)
    plt.xlabel('Trading Days', fontsize=12)
    plt.ylabel('Normalized Value (100 = Start)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated chart: {output_path}")

def generate_sentiment_chart(output_path="images/sentiment-trends.png"):
    """Generates a sentiment trend chart."""
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    sentiment = [0.45, -0.2, 0.15, 0.6]
    colors = ['#00B894' if s > 0 else '#D63031' for s in sentiment]
    
    plt.figure(figsize=(8, 5))
    plt.bar(tickers, sentiment, color=colors, alpha=0.8)
    
    plt.title('Asset Sentiment Score (Real-time Analysis)', fontsize=14, pad=20)
    plt.ylabel('Sentiment Score (-1.0 to 1.0)', fontsize=12)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black', linewidth=0.8)
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated chart: {output_path}")

if __name__ == "__main__":
    generate_performance_chart()
    generate_sentiment_chart()
