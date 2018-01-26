"""
landonhotel.py
Author: Adam Beagle

See README.md for description.
"""
import argparse
from http.server import SimpleHTTPRequestHandler, test as run_server
from os import chdir, getcwd
from os.path import abspath, dirname, join

from simplesite import Page, PrettyURLsPage, SimpleStaticSiteGenerator

URL_OPTIONS = {
    'abs_production': 'http://pbcs.us/~abeagle/projects/landonhotel/',
    'abs_local': join(getcwd(), 'output/'),
    'relative': '/'
}

DEFAULT_PORT = 8000

def make_site(urls):
    """Instantiate pages and render/write site"""
    context = { 'site_url': URL_OPTIONS[urls] }
    
    context.update({
      # Add extra global context here
    })

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
    
    return sitegen

#####################################################################
if __name__ == '__main__':
    # Handle command line args
    parser = argparse.ArgumentParser(
      description="Landon Hotel Site Generator"
    )
    
    parser.add_argument(
        '-u', '--urls',
        choices=URL_OPTIONS.keys(),
        default='relative',
    )
    
    parser.add_argument(
      '-s', '--server',
      action='store_const',
      const=1,
      default=0
    )
    
    parser.add_argument(
      '-p', '--port',
      action='store',
      default=DEFAULT_PORT,
      type=int
    )
    
    parser.add_argument(
        '-b', '--bind',
        default='',
    )
    
    args = parser.parse_args()
    
    # Set cwd to this file's location
    chdir(dirname(abspath(__file__)))
    
    # Generate and write site
    sitegen = make_site(args.urls)
    
    # Run server if -s or --runserver flag present
    if args.server:
      chdir(sitegen.output_path)
      run_server(port=args.port, bind=args.bind, HandlerClass=SimpleHTTPRequestHandler)
    
