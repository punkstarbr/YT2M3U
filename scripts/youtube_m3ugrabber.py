#! /usr/bin/python3#!/usr/bin/env python3

import os
import sys

import requests


def print_banner():
    banner = r"""
` `     "    "                       

       .-.      _______                            
      {}``; |==|_______D                        
      / ('        /|\                       
  (  /  |        / | \                             
akg\(_)_]]      /  |  \ 
    """
    print(banner)


def is_windows():
    return 'win' in sys.platform


def grab(url):
    try:
        response = requests.get(url, timeout=15).text
        if '.m3u8' not in response:
            raise ValueError('Invalid URL')
        end = response.find('.m3u8') + 5
        tuner = 100
        while True:
            if 'https://' in response[end - tuner : end]:
                link = response[end - tuner : end]
                start = link.find('https://')
                end = link.find('.m3u8') + 5
                break
            else:
                tuner += 5
        print(f"{link[start : end]}")
    except:
        if is_windows():
            print('https://raw.githubusercontent.com/vijay6672/YT2M3U/main/assets/moose_na.m3u')
        else:
            print('https://raw.githubusercontent.com/vijay6672/YT2M3U/main/assets/moose_na.m3u')


def main():
    print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
    print_banner()

    with open('../youtube_channel_info.txt', errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('~~'):
                continue
            if not line.startswith('https:'):
                ch_name, grp_title, tvg_logo, tvg_id = map(str.strip, line.split('|'))
                print(f'\n#EXTINF:-1 group-title="{grp_title.title()}" tvg-logo="{tvg_logo}"tvg-id="{tvg_id}", {ch_name}')
            else:
                grab(line)

    if 'temp.txt' in os.listdir():
        os.remove('temp.txt')
        os.remove('watch*')


if __name__ == '__main__':
    main()
