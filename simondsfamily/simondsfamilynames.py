from os import path
import sys
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

def main():

#open/read file
    direct = path.dirname(__file__)
    simondsfirstnames = open(path.join(direct, 'firstnames.txt')).read()
#use pytagcloud module to create tags based on name counts, create image. 
    simondstags = make_tags(get_tag_counts(simondsfirstnames), maxsize=150)
    create_tag_image(simondstags, 'simondsfirstnames.png', size=(1200, 1200))

if __name__ == "__main__":
    main()