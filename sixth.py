import sys
import requests
from lxml import html


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    response = requests.get(url)

    if response.status_code !=200:
        print("Chyba")
        return[]
    
    
    tree = html.fromstring(response.content)


    xpath = '//a/@href'
    hrefs = tree.xpath(xpath) 

    hrefs = [href for href in hrefs]

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)
    except IndexError:
        print("Zadejte URL jako argument")
