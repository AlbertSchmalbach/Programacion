import pandas as pd
from lxml import html

simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1-20)")

# root = html(simpsons)

print(simpsons[5].head(10))