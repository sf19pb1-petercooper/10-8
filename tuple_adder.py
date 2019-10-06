"""

Takes items from a given URL and returns the title and URL to a named tuple, Game.

"""

from collections import namedtuple
import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')
game_list=[]
def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    content = feedparser.parse(FEED_URL)
    dict_object = dict(content)
    for key in dict_object:
        print(key for key in dict_object['entries'])
        for key in dict_object['entries']:
            list_link_dirty = (key['summary'])
            list_clean_link = (list_link_dirty.split()[1])
            for url in list_clean_link.split():
                if len(url.split('>')) <= 1:
                    continue
                else:
                    game_list.append(Game((url.split('>')[1]), url[6:47]))
    pass

get_games()
print(game_list)
