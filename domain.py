from urlparse import urlparse


def get_domain_name(url):
    try:
        result = get_sub_domain_name(url).split('.')
        return result[-2] + '.' + result[-1]
    except Exception,e:
        print str(e)
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).path
    except Exception, e:
        print str(e)
        return ''