import urllib2, json, facebook, simplejson

def main():

#use Facebook API
    access_token = 'CAACEdEose0cBAGP05DCpxBugR8YLTjD6aKchT6GwwFBfMZBgM3bQySUpaf2J1IB4PBiXIZCj6bRZAdSLlbFsbI5PcKFpKDXGvKkOdBjw1PjFIyFfrK2e8ggtTpypSdeOPKGjZB8NZBxCnu7gcuQxEbKjJRZAL3T3awFl8Rx6PG6xNrZBlBK9szpasvuReYwMdfHIcn0WJYN6QZDZD'
    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object('me')
    group = graph.get_connections('me', 'friends')
    GROUPID = '177368322311892'

#read Facebook URL, load JSON string for each family member
    url = "https://graph.facebook.com/177368322311892/members?access_token=%s" % (access_token)
    response = urllib2.urlopen(url)
    response_string = json.load(response)
#open file to write out
    firstnames = open('firstnames.txt', 'w')

#list of first names
    firstnamelist = []

#for each json dictionary key value pair, grab first index of name, append to first name list
    for key, value in response_string.items():
        if key == 'data':
            for member in value:
                for k, v in member.items():
                    if k == 'name':
                        v = v.split()
                        firstnamelist.append(v[0])
#iterate through first name, convert to string, write to file
    for item in firstnamelist:
        item = unicode(item)
        item = str(item)
        firstnames.write(item + '\n')


if __name__ == "__main__":
    main()
