import openai
import os
import requests
from bs4 import BeautifulSoup

def main():
    openai.api_key = get_key()
    gpt_reworker()

def gpt_reworker():

    article_data = scrape_news()

    with open("prompt.txt", "r", encoding='utf-8') as f:
        prompt = f.read()

    messages = []
    print("Translation on the way\n")
    with open("translated_articles.txt", "w", encoding='utf-8') as translation:
        for data in article_data:

            content = data['date'] + '\n' + data['title'] + '\n' + data['body'] + '\n\n'

            messages.append({"role":"user", "content":prompt + '\n' + content})

            response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.4
                )

            reply = response["choices"][0]['message']['content']
            messages.append({"role":"assistant", "content":reply})

            translation.write(reply)
            translation.write('\n\n')

    print("There you go!")

    return

def get_key():
    key = os.environ.get("OPENAI_API_KEY")
    return key

def scrape_news():

    print("Reading from italian news... ")
          
    url = "https://www.ansa.it/sito/notizie/topnews/index.shtml"
    response = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")

    # Find all the article elements with the class "news small"
    articles = soup.find_all("article", class_="news small")

    # Create an empty list to hold the article data
    article_data = []

    # Loop through each article and extract the date, title, and link
    for article in articles:
        date_div = article.find("div", class_="news-date")
        date = date_div.find("em").text.strip()
        title_h3 = article.find("h3", class_="news-title")
        title = title_h3.find("a").text.strip()
        link = title_h3.find("a")["href"]
        
        article_dict = {
            "link": link,
            "title": title,
            "date": date,
            "body": ''
        }
        
        # Add the article dictionary to the article data list
        article_data.append(article_dict)

    with open("articles.txt", "w", encoding='utf-8') as articles_file:
        for data in article_data:
            response = requests.get("https://www.ansa.it/" + data['link'])
            soup = BeautifulSoup(response.content, 'lxml')
            article_body_div = soup.find('div', attrs={'itemprop': 'articleBody'})
            article_body = article_body_div.get_text(strip=True)

            data['body'] = article_body
            #print(data['body'])

            # Write the article data to the file in the desired format
            articles_file.write(data['date'] + '\n')
            articles_file.write(data['title'] + '\n')
            articles_file.write(data['body'] + '\n\n')
    
    print("Done\n")
    return article_data
    

main()