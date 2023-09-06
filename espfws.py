def priceFinder(url, amount_of_pages=10):
    import requests
    from bs4 import BeautifulSoup
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    
    def getFirstPage(url):
        import requests 
        from bs4 import BeautifulSoup

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        for page in soup.find_all("a", class_="pagination__item"):
            if "pgn=1" in page.get("href"):
                return page.get("href")

    url = getFirstPage(url)

        
    def findItem(url):  
        
            
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
    
    
        
        titles = []
        prices = []

        items = {}

        for t in soup.find_all(class_="s-item__title"):
            titles.append(t.text)
        for p in soup.find_all(class_="s-item__price"):
            prices.append(p.text)

        for i in range(len(titles)):
            items[titles[i]] = prices[i]

        def pricesout():
            for item in items:
                print(item, items[item] + "\n")

        def insort(dict):
            arr = [(dict[i].split(" ")[0].replace("£", "").replace("$", "")) for i in dict]
            arr = [float(i.replace(",", "")) for i in arr]
            for i in range(len(arr)-1):
                j = i
                while arr[j] > arr[j+1] and j >= 0:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    j -= 1

            return [str(i) for i in arr]

        def find(dict, find=None):
            found = []
            for key, value in dict.items():
                if find in value:
                    found.append(key) 
            return found



        arr = insort(items)
        key = find(items, arr[0])
            
        out = [key[0], ": ", items[key[0]]]
            
        return " ".join(out)

        
    out_prices = []    
    urls = []
    
    for i in range(1, amount_of_pages):
        urll = url.split("pgn=")[0] + "pgn=" + str(i)
        urls.append(urll)

    for ur in urls:
        p = findItem(ur)
        out_prices.append(p)
        


    
    return "\n".join(out_prices)
    




URL = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=desk&_sacat=0&LH_TitleDesc=0&_odkw=laptop+speakers&_osacat=0&_sop=12&_ipg=240"


print(priceFinder(URL))


# Returns - 

# New listingDesk with Movable drawers :  £0.99
# New listingIKEA Micke Desk 142x50cm In White With DrawersCharity item :  £0.99
# Stylish large modern glass table or deskCharity item :  £0.99
# Desk :  £10.99 to £11.89
# desk and draws :  £25.00
# Home Office Chair Adjustable Computer Desk Chair with Arms for Study Work Black :  £0.99
# Cherry Tree Furniture Modern Compact Desk Table Computer Workstation  ( Black) :  £42.99 to £47.99
# White/White Glass Top Desk & Chair Set Home Study PC Laptop Computer Table :  £52.99
# Adjustable Computer Desk Laptop PC Table Home Office Study Notebook Table :  £384.00 to £551.00