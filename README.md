# twitter-token-tracker
Monitor token launches in real-time and act instantly. This bot watches a specified Twitter handle for token contract addresses or presale
<!-- updated: 2025-11-04-r01 -->

## Description
This small utility fetches the latest tweet from a given Twitter handle and prints its content to the console. It is intended for monitoring token launch announcements posted on Twitter.

## Features
- Retrieves the most recent tweet from a specified Twitter handle.
- Displays the tweet content in a readable format.
- Handles errors gracefully and reports failures.

## Requirements
- Python 3
- `snscrape` library (used for Twitter scraping)

## Installation
```bash
pip install snscrape
```

## Usage
```bash
python handle.py
```
The script will prompt for a Twitter handle (without the `@`).

## Project Structure
- `handle.py` – Main script that fetches the latest tweet.
- `README.md` – Project documentation.
- `LICENSE` – License file.
- `.gitignore` – Git ignore patterns.

## License
MIT License – see the [LICENSE](LICENSE) file.
