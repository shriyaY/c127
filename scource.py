import bs4


def scrape():

    for i in range(0,10):
        print(f'Scrapping page{i+1} ...')

        soup = BuetifulSoup(browser.page_source, "html.parser")

        for ul_tag in soup.find_all(ul)