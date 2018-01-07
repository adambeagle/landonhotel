"""
landonhotel.py
Author: Adam Beagle

See README.md for description.
"""
import argparse
from os import getcwd
from os.path import join

from simplesite import Page, PrettyURLsPage, SimpleStaticSiteGenerator

URL_OPTIONS = {
    'abs_production': 'http://pbcs.us/~abeagle/projects/landonhotel/',
    'abs_local': join(getcwd(), 'output/'),
    'relative': '/'
}

def make_site(urls):
    """Instantiate pages and render/write site"""
    context = { 'site_url': URL_OPTIONS[urls] }

    pages = (
        Page('index.html', **context),
        PrettyURLsPage('meetings-and-events.html', **context),
        PrettyURLsPage('roomservice.html', **context),
        PrettyURLsPage('contact.html', **context),
        PrettyURLsPage('reservations.html', **context),
        PrettyURLsPage('specials.html', **context),
        PrettyURLsPage('news.html', **context),
    )
    
    sitegen = SimpleStaticSiteGenerator(
        pages=pages,
        static_map={'images/favicon.ico': '../'},
    )
    sitegen.output_site()

# Generate and output site
if __name__ == '__main__':
    # Handle command line args
    parser = argparse.ArgumentParser(description="Landon Hotel website generator")
    parser.add_argument(
        '-u', '--urls',
        choices=URL_OPTIONS.keys(),
        default='relative',
    )
    
    args = parser.parse_args()
    make_site(args.urls)
    
