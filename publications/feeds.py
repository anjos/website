from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from publications.models import Publication
from settings import MEDIA_URL

class TenLastPublications(Feed):
    feed_type = Atom1Feed
    #title = unicode("Publications at " + Site.objects.filter(id=1)[0].name, 'utf-8').encode('ascii', 'xmlcharrefreplace')
    title = "Publications at " + Site.objects.filter(id=1)[0].domain
    link = "/publication/"
    description = "The last things I wrote"
    title_template = "feeds/publications_title.html"
    description_template = "feeds/publications_description.html"

    def items(self):
      return Publication.objects.order_by('-date')[:10]

    def item_link(self, item):
      return '/publication/' + str(item.id) + '/'

