import hackernews_scrapper as hs
import requests
import time

def prepare_request(post_url,post_title,CONSUMER_KEY,ACCESS_TOKEN):
    request = {"url":post_url,
    "title":post_title,
    "consumer_key":CONSUMER_KEY,
    "access_token":ACCESS_TOKEN}
    return request

def save_posts_to_pocket():
    property_file_path = './pocket.properties'
    section = 'POCKET'
    configurations = hs.read_properties(property_file_path, section)
    API_ENDPOINT = configurations['url']
    CONSUMER_KEY = configurations['consumer_key']
    ACCESS_TOKEN = configurations['access_token']
    top_hackernews_posts = hs.scrape_hacker_news()
    for post in top_hackernews_posts:
        post_title = post['title']
        post_url = post['link']
        request = prepare_request(post_url,post_title,CONSUMER_KEY,ACCESS_TOKEN)
        response = requests.post(url = API_ENDPOINT, data = request)
        if response.status_code == 200:
            print(f'Saved {post_title} to pocket')
        else:
            print(f'Status Code {response.status_code}. Couldn\'t save {post_title}')

if __name__ == '__main__':
    save_posts_to_pocket()