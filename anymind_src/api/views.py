from logging import getLogger
import re

from django.http import JsonResponse
import requests

log = getLogger(__name__)


def srt_to_list(text):
    prog = re.compile(' \s+')
    return re.sub(prog, '|', text.strip()).split('|')


def remove_tags(array):
    log.debug(f"removing tags from the array with length: {len(array)}")
    for i, item in enumerate(array):
        gt = item.find('>')
        lt = item.find('<')
        if -1 < gt < lt:
            item = item[gt + 1:]
            log.debug("first tag flake is removed")

        while True:
            tag_s = item.find('<')
            if tag_s == -1:
                break
            tag_e = item.find('>')
            item = item[:tag_s] + item[tag_e + 1:]
        log.debug(f"Item {i} is ready")
        array[i] = srt_to_list(item)
    return array


def scrab_tweets(text, pages_size=None):
    try:
        pages_size = int(pages_size)
    except (ValueError, TypeError):
        pages_size = None
    log.debug('Scrabbing the text')
    text_list = text.replace('\n', ' ').split('<table class="tweet')
    text_list.pop(0)
    log.debug(f"Text is splitted, got array length {len(text_list)}")
    data = []
    for item in remove_tags(text_list):
        if item[3].startswith('Replying to'):
            continue
        data.append({
            'account': {
                'fullname': item[0],
                'href': f'/{item[1][1:]}',
            },
            'date': item[2],
            'hashtags': [word for word in item[3].split() if word.startswith('#')],
            'text': item[3],
        })
        if pages_size and len(data) == pages_size:
            log.debug("Page is fulfilled!")
            break

    return data


def hashtag(request, tag):
    pages_size = request.GET.get('pages_size')
    log.debug(f"Pages size: {pages_size}")
    r = requests.get(f'https://mobile.twitter.com/search?q=%23{tag}')
    return JsonResponse(
        data=scrab_tweets(r.text, pages_size),
        safe=False
    )


def users(request, user):
    pages_size = request.GET.get('pages_size')
    log.debug(f"Pages size: {pages_size}")
    r = requests.get(f'https://mobile.twitter.com/search?q=%40{user}')
    return JsonResponse(
        data=scrab_tweets(r.text, pages_size),
        safe=False
    )
