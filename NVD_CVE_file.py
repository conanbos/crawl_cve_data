
import re

import main




def get_internallinks(bs, includeUrl):
    # includeUrl = '{}://{}'.format(main.urlparse(includeUrl).scheme, main.urlparse(includeUrl).netloc)
    internallinks = []
    for link in bs.find_all('a', href=re.compile('/feeds/xml/cve/trans/es/nvdcve-.*.xml.zip')):
        # print(link.attrs['href'])
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                if (link.attrs['href'].startswith('/')):
                    internallinks.append(includeUrl + link.attrs['href'])
                else:
                    internallinks.append(link.attrs['href'])
    return internallinks



