# 💰 extra.ge Price Tracker

This is a Python script that monitors a specific product on [extra.ge](https://extra.ge).  
If the product's price falls below your target, it sends you an email notification.

## 📦 Requirements

- Python 3.x
- Gmail account with [App Password](https://support.google.com/accounts/answer/185833)
- `python-dotenv` for managing environment variables

## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/extra-ge-price-tracker.git
   cd extra-ge-price-tracker
```

Install dependencies:

> pip install python-dotenv


>Create a .env file:

```
PRODUCT_URL=https://catalog.extra.ge/api/products/dell-p2723qe-lcd-monitor-27-monitori/747028
TARGET_PRICE=1000

EMAIL_FROM=your.email@gmail.com
EMAIL_TO=destination@email.com
EMAIL_APP_PASS=your_app_password
```
