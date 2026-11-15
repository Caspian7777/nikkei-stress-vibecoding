import os
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

print("Fetching Nikkei 225 data...")
df = yf.download("^N225", period="6mo", interval="1d")
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.droplevel(1)

dates = df.index
close_prices = df["Close"]

np.random.seed(42)
price_returns = close_prices.pct_change().fillna(0)
delay_index = (
    50
    - price_returns * 500
    + np.random.normal(0, 3, len(close_prices)).cumsum()
)
delay_index = np.clip(delay_index, 10, 100)

os.makedirs("frames", exist_ok=True)
print("Rendering animation frames...")

for i in range(10, len(dates) + 1, 1):
    fig, ax1 = plt.subplots(figsize=(10, 5), facecolor="#121212")
    ax1.set_facecolor("#181818")

    sub_dates = dates[:i]
    sub_close = close_prices[:i]
    sub_delay = delay_index[:i]

    ax1.plot(sub_dates, sub_close, color="#1a73e8", linewidth=2, label="Nikkei 225 Close")
    ax1.set_ylabel("Nikkei 225 Index", color="#1a73e8", fontsize=10)
    ax1.tick_params(axis="y", labelcolor="#1a73e8")
    ax1.tick_params(axis="x", colors="#aaaaaa")
    ax1.grid(True, color="#2a2a2a", linestyle="--", alpha=0.5)

    ax2 = ax1.twinx()
    ax2.set_facecolor("none")
    ax2.plot(sub_dates, sub_delay, color="#ff9800", linewidth=1.5, linestyle="--", label="Social Stress Index")
    ax2.set_ylabel("Social Stress & Railway Delay Proxy", color="#ff9800", fontsize=10)
    ax2.tick_params(axis="y", labelcolor="#ff9800")

    plt.title(
        f"Nikkei 225 Market Volatility vs. Social Stress ({sub_dates[-1].strftime('%Y-%m-%d')})",
        color="#ffffff",
        fontsize=12,
    )
    plt.tight_layout()

    plt.savefig(f"frames/frame_{i:04d}.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)

print("Frames generated! Compiling video...")

image_folder = "frames"
video_name = "stock_trend_animation.mp4"
images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]
imageio.mimsave(
    video_name,
    [imageio.imread(os.path.join(image_folder, img)) for img in images],
    fps=12,
)

print(f"Done! Video saved as: {video_name}")
