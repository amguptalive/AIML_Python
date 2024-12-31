import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
# STOCK_NAME = "IBM"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "8ZXRCM3TX322CC9G"
#STOCK_API_KEY = "demo"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "938dc5a6f16e4060aab351d7ca1e166e"

TWILIO_SID = "ACf4cdf1702ab028ceb2cacf74bbbdc739"
TWILIO_AUTH_TOKEN ="251be7f74026db6860b12a0c66fef83e"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json()["Time Series (Daily)"])
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

print(yesterday_closing_price)
# 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

print(day_before_yesterday_closing_price)
# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
difference = (yesterday_closing_price - day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# 4. Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
# diff_percent = round((difference / yesterday_closing_price) * 100)
diff_percent = (difference / yesterday_closing_price) * 100
print(diff_percent)
# 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if diff_percent > 0.01:
# print("Get News")


## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
print(abs(diff_percent))
if abs(diff_percent) > 0.01:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }


# 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
three_articles = articles[:3]
print(three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME} :{up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

# TODO 9. - Send each article as a separate message via Twilio.
for article in formatted_articles:
    message = client.messages.create(
      from_='+18558287490',
      body=article,
      to='+18777804236'
     #to='+16508346809'
    )

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""