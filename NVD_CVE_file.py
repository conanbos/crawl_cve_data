
import re

import main




def get_internallinks(bs, includeUrl,ftype):
    #ftype:
    #xml:       nvdcve xml data
    #json:      all json data
    #nvdjson:   nvdcve json data
    #rss:       nvd rss analysis data
    #all:       All data

    if ftype=='xml':
        filetype='nvdcve-.*.xml.zip'
    elif ftype=='nvdjson':
        filetype = 'nvdcve-.*.json.zip'
    elif ftype=='json':
        filetype = '.*.json.zip'
    elif ftype=='rss':
        filetype = 'nvd-rss.*.xml.zip'
    else:
        filetype = '.*.zip'


    internallinks = []
    for link in bs.find_all('a', href=re.compile(filetype)):
        # print(link.attrs['href'])
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                if (link.attrs['href'].startswith('/')):
                    internallinks.append(includeUrl + link.attrs['href'])
                else:
                    internallinks.append(link.attrs['href'])
    return internallinks



