from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from publications.models import Publication, Document
from django.utils.translation import ugettext_lazy as _

entries_per_feed = 20

from django.contrib.sites.models import Site
site = Site.objects.get_current()

class LatestPublications(Feed):
    feed_type = Atom1Feed
    title = _("Andre Anjos latest publications")
    description = _("The last %d publications I have written" % entries_per_feed)
    link = 'http://%s/publication' % site.domain

    title_template = "feeds/publications_title.html"
    description_template = "feeds/publications_description.html"

    # stuff for our synchronization between this file and urls.py
    basename = 'publications'

    def items(self):
      return Publication.objects.order_by('-date')[:entries_per_feed]

    def item_link(self, item):
      return 'http://%s/publication/%d' % (site.domain, item.id)

class LatestDocuments(Feed):
    feed_type = Atom1Feed
    title = _("Andre Anjos latest documents")
    description = _("The last %d documents I have uploaded" % entries_per_feed)
    link = 'http://%s/publication' % site.domain

    title_template = "feeds/documents_title.html"
    description_template = "feeds/documents_description.html"

    # stuff for our synchronization between this file and urls.py
    basename = 'documents'

    def items(self):
      return Document.objects.order_by('-date').filter(public=True)[:20]

    def item_link(self, item):
      return item.data.url

    def item_enclosure_url(self, item):
      return item.data.url

    def item_enclosure_length(self, item):
      return item.data.size

    item_enclosure_mime_type = 'application/octet-stream'
