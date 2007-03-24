from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from files.models import File
from settings import MEDIA_URL
from django.utils.translation import gettext_lazy as _

class TenLastFilesUploaded(Feed):
    feed_type = Atom1Feed
    title = _("Files at %s") % Site.objects.filter(id=1)[0].domain
    link = "/"
    description = _("The last public uploads to the site")
    title_template = "feeds/files_title.html"
    description_template = "feeds/files_description.html"

    def items(self):
      return File.objects.order_by('-date').filter(public=True)[:10]

    def item_link(self, item):
      return item.url()
