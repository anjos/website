from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from publications.models import Publication, File
from django.utils.translation import ugettext_lazy as _

entries_per_feed = 20

from django.contrib.sites.models import Site
site = Site.objects.get_current()

class LatestPublications(Feed):
    feed_type = Atom1Feed
    title = _("Andre Anjos latest publications")
    description = _("The last %d publications I have written" % entries_per_feed)
    link = '/publication'

    title_template = "publications/feeds/title.html"
    description_template = "publications/feeds/description.html"

    # stuff for our synchronization between this file and urls.py
    basename = 'publications'

    def items(self):
      return Publication.objects.order_by('-date')[:entries_per_feed]

    def item_link(self, item):
      return '/publication/%d' % (item.id)

class LatestFiles(Feed):
    feed_type = Atom1Feed
    title = _("Andre Anjos latest files")
    description = _("The last %d documents I have uploaded" % entries_per_feed)
    link = '/publication'

    title_template = "publications/feeds/files_title.html"
    description_template = "publications/feeds/files_description.html"

    # stuff for our synchronization between this file and urls.py
    basename = 'files'

    def items(self):
      return File.objects.order_by('-date').filter(public=True)[:20]

    def item_link(self, item):
      return item.data.url

    def item_enclosure_url(self, item):
      return item.data.url

    def item_enclosure_length(self, item):
      return item.data.size

    item_enclosure_mime_type = 'application/octet-stream'
