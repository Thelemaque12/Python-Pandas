from bs4 import BeautifulSoup
import pandas as pd

years = list(range(2001,2023))
url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html#per_game_stats::pts_per_g'

for year in years:
    url = url.format(year)
    data = requests.get(url)
    
    with open("mvps/{}.html".format(year), "w+") as f:
        f.write(data.text)
        

df = []

for year in years:
    with open("mvps/{}.html".format(year)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    pts_table = soup.find_all(id="per_game_stats")
    pts = pd.read_html(str(pts_table))[0]
    pts["Year"] = year
    df.append(pts)
