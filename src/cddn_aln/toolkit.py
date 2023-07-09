from random_user_agent.user_agent import UserAgent
import random
from scrapy import Request, Spider
import json
import pandas as pd
import regex as re
from random_user_agent.user_agent import UserAgent
import random
from os import remove

class UserAgents:
    def __init__(self):
        user_agent_rotator = UserAgent(software_names=['chrome'], operating_systems=['windows', 'linux'])
        self.user_agents = user_agent_rotator.get_user_agents()
        self.il = logger.InfoLogger()
    def get_rand_UA(self):
        return random.choice(self.user_agents)['user_agent']
    def get_rand_UA_list(self):
        return self.user_agents

#on => https://x5rhfuesar27hwcohtxu2x+Xsq94Hcw:x940jt4upr
class BatuProxy:
    def __init__(self):        
        self.prx = "lum-customer-c_679e93f2-zone-ticketmaster-country-us:nxv1of25qjto@zproxy.lum-superproxy.io:22225"
    def get_username(self):
        return "lum-customer-c_679e93f2-zone-ticketmaster-country-us"
    def get_passwd(self):
        return 'nxv1of25qjto'
    def get_proxy(self):
        return random.choice(self.cleaned_proxy_list)
    def proxy_reorganizer(self, proxy, http = True):
        '''Works with proxies with auth details.'''
        items_list = proxy.split(':')
        real_size = len(items_list)
        if'@' in proxy:
            raise("---proxy_reorganizer--- : Invalid proxy.")
        elif real_size == 5:
            if not 'http' in proxy:
                raise("---proxy_reorganizer--- : Invalid proxy.")
            new_url = "https://" + ":".join([items_list[3] , items_list[4]]) + '@' + ":".join([items_list[1][2:] ,items_list[2]])
            
        elif real_size == 4:
            new_url = "https://" + ":".join([items_list[2] , items_list[3]]) + '@' + ":".join([items_list[0] ,items_list[1]])
        if not http:
                new_url.strip('https://')
        return new_url        
    def proxy_reorganizer_parsed(self, proxy, http = True):
        '''Works with proxies with auth details.'''
        proxy = proxy.strip()
        items_list = proxy.split(':')
        main_proxy = items_list[0] + ':' + items_list[1]
        userid = items_list[2]
        passwd = items_list[3]
        return main_proxy, userid, passwd       
        return d
if __name__ == '__main__':
    pass