import requests
from bs4 import BeautifulSoup
import pprint
import configparser

def read_properties(property_file_path,section):
    config = configparser.ConfigParser()
    config.read(property_file_path)
    return dict(config.items(section))

def sort_stories_by_votes(hackernews_list):
    return sorted(hackernews_list,key = lambda k:k['points'],reverse=True)

def get_content(links,subtext,min_votes):
    info = []
    for index in range(len(links)):
        title = links[index].getText()
        link = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if  points>=min_votes :
                info.append({'title': title,'link': link,'points':points})
    return info

def scrape_hacker_news():
    property_file_path = './config.properties'
    section = 'HACKERNEWS'
    configurations = read_properties(property_file_path, section)
    hackernews_url = configurations['url']
    max_items = int(configurations['max.items'])
    min_votes = int(configurations['min.votes'])
    max_pages = int(configurations['max.pages'])
    content_list = []
    page = 1
    while page<=max_pages:
        hackernews_response = requests.get(hackernews_url+str(page))
        soup = BeautifulSoup(hackernews_response.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        content_list+=(get_content(links,subtext,min_votes))
        page = page+1
    content_list = sort_stories_by_votes(content_list)   
    if len(content_list) >= max_items:    
        return content_list[:max_items]
    return content_list

if __name__ == '__main__':
    pprint.pprint(scrape_hacker_news())