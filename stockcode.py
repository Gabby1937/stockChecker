import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def stock_analysis(ticker, days):
    # Import data from Yahoo Finance
    data = yf.download(ticker, interval="1d", period=f"{days}d")

    # Calculate 20-day moving average
    data['20ma'] = data['Close'].rolling(window=20).mean()

    # Create a chart of the closing price and the moving average
    plt.plot(data['Close'], label='Close')
    plt.plot(data['20ma'], label='20-day MA')
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title(f'{ticker} Stock Price')

    # Save chart to an image file
    plt.savefig(f'{ticker}_chart.png')
    
    # Email chart
    email_user = "gabrieljohnson1937@gmail.com"#"YOUR_EMAIL_ADDRESS"
    email_password = "yvnsbpfocfindwwk"#"YOUR_EMAIL_PASSWORD"
    recipient = "gabbbyjohnson193752@gmail.com"#"RECIPIENT_EMAIL_ADDRESS"
    
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = recipient
    msg['Subject'] = f"{ticker} Stock Analysis"
    
    with open(f'{ticker}_chart.png', 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)
        
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, recipient, msg.as_string())
    server.quit()

# Example usage
stock_analysis("TSLA", 14)
