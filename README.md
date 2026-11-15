
# Nikkei 225 Volatility vs. Social Stress Animation

A lightweight Python vibecoding pipeline that pulls Nikkei 225 (`^N225`) price history, renders frame-by-frame dark-mode dual-axis charts, and compiles them into an animated MP4 video.

## Visual Aesthetic
- Dark terminal canvas (`#121212` figure / `#181818` plot area)
- Left axis: Nikkei 225 Close (`#1a73e8`)
- Right axis: Social Stress & Railway Delay Proxy (`#ff9800`)

> **Note on Data:** `^N225` prices are fetched live via `yfinance`. The Social Stress & Railway Delay Proxy is a synthetic illustrative series generated from return shocks and cumulative noise for visual exploration, not an official government or transit dataset.

## Setup (GitHub Codespaces or Local)
```bash
pip install yfinance matplotlib pandas numpy imageio imageio-ffmpeg
