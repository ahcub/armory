import re
from distutils.dir_util import mkpath
from logging import getLogger
from os import getcwd
from urllib.error import HTTPError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

from os.path import join, dirname, splitext

from os_utils.logging import configure_stream_logger

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0'}


logger = getLogger()
configure_stream_logger()


def dump_web_pages_recursively(site_address, dest_path, urls=None, localize_links=True, headers=None, iteration_limit=0):
    if not headers:
        headers = DEFAULT_HEADERS
    if not urls:
        urls = [site_address]

    urls_registry = set()
    next_urls = urls
    iteration = 0
    while next_urls:
        if iteration_limit and iteration >= iteration_limit:
            break
        iteration += 1
        logger.info('%s pages processed', len(urls_registry))
        logger.info('Dumping urls: %s', next_urls)
        urls = next_urls
        next_urls = set()
        for url in urls:
            if url not in urls_registry:
                logger.info('Processing url: %s', url)
                urls_registry.add(url)
                request_url = urljoin(site_address, url)
                try:
                    response = get_url_response(request_url, headers)
                except HTTPError:
                    logger.warning('Failed to load %s', request_url)

                relative_path = url if url != site_address else 'index'
                dest_file_path = get_dest_file_path(dest_path, relative_path)
                mkpath(dirname(dest_file_path))

                is_str_resp = isinstance(response, str)

                if is_str_resp:
                    for new_url in get_related_page_urls(response):
                        if new_url not in urls_registry and new_urls_filter(new_url):
                            next_urls.add(new_url)

                if localize_links and is_str_resp:
                    response = localize_links_inside_file(response, url)

                if is_str_resp:
                    file_data = response.encode('utf-8')
                else:
                    file_data = response

                with open(dest_file_path, 'wb') as dest_file:
                    dest_file.write(file_data)


def get_dest_file_path(dest_path, url):
    dest_file_path = join(dest_path, url.strip('/'))
    dest_file_path = dest_file_path.replace('/', '\\')
    if not splitext(dest_file_path)[1]:
        dest_file_path += '.html'

    return dest_file_path


def get_url_response(url, headers):
    request = Request(url, headers=headers)
    response = urlopen(request).read()
    if url.endswith('.png'):
        return response
    else:
        return response.decode('utf-8')


def localize_links_inside_file(file_context, url):
    logger.info('Localizing links')
    result = re.sub(r'((?:href|src)=(?:"|\'))([^"\']*)((?:"|\'))', url_custom_repl(url), file_context)
    return result


def url_custom_repl(url):
    steps_up_count = get_url_nesting_level(url) - 1
    steps_up = ('../' * steps_up_count)

    def custom_repl(match_obj):
        if not splitext(match_obj.group(2))[1]:
            url_path = steps_up + match_obj.group(2).strip('/') + '.html'
        else:
            url_path = steps_up + match_obj.group(2).strip('/')

        return match_obj.group(1) + url_path + match_obj.group(3)

    return custom_repl


def get_url_nesting_level(url):
    return len(urlsplit(url).path.strip('/').split('/'))


def get_related_page_urls(page_content):
    logger.info('Getting page related urls')
    urls = []
    for res in page_content.splitlines():
        pattern = re.compile(r'(?:href|src)=(?:"|\')/([^"\']*)(?:"|\')')
        for result in pattern.findall(res):
            if result is not None:
                urls.append(result)
    return urls


def new_urls_filter(new_url):
    return (new_url.startswith('reference') or new_url.startswith('assets')) and \
        (splitext(new_url)[1] in ['', '.png', '.css'])

if __name__ == '__main__':
    urls = [
        'reference/encyclopedia/chapters/slug/introduction-to-venture-capital-and-private-equity-finance',
    ]
    dump_web_pages_recursively('https://vcexperts.com', join(getcwd(), 'test'), urls=urls, iteration_limit=2)
