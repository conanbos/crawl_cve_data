import re
import main



def combine_link(origin_link):
    pop_link = ''
    pop_link = main.sites + origin_link[16:25] + origin_link[26:48]
    return pop_link


def get_internallinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(main.urlparse(includeUrl).scheme, main.urlparse(includeUrl).netloc)
    internallinks = []
    for link in bs.find_all('a', onclick=re.compile('/attached.*.zip')):
        # print(link.attrs['onclick'])
        if link.attrs['onclick'] is not None:
            if link.attrs['onclick'] not in internallinks:
                if (link.attrs['onclick'].startswith('/')):
                    internallinks.append(includeUrl + combine_link(link.attrs['onclick']))
                else:
                    internallinks.append(combine_link(link.attrs['onclick']))
    return internallinks





