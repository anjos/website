from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.contrib.sites.models import Site
from projects.models import Project, Download
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat
from django.core.exceptions import ObjectDoesNotExist

entries_per_feed = 20
site = Site.objects.get_current()

class LatestDownloadsForProject(Feed):
  feed_type = Atom1Feed
  basename = 'downloads'

  def get_object(self, bits):
    if len(bits) != 1:
      raise ObjectDoesNotExist
    try:
      return Project.objects.get(name=bits[0])
    except:
      raise ObjectDoesNotExist

  def title(self, obj):
    return _("%s latest downloads" % obj.name)

  def description(self, obj):
    return _("The last %d downloads available for %s" % \
        (entries_per_feed, obj.name))

  def link(self, obj):
    return "%s/project/%s" (site.domain, obj.name)

  title_template = "feeds/downloads_title.html"
  description_template = "feeds/downloads_description.html"

  def items(self, obj):
    return obj.download_set.exclude(development__exact=True).order_by('-date')[:entries_per_feed]

  def item_link(self, item):
    return item.data.url

  def item_pubdate(self, item):
    return item.date

  def item_enclosure_url(self, item):
    return item.data.url

  def item_enclosure_length(self, item):
    return item.data.size

  item_enclosure_mime_type = 'application/octet-stream'

class LatestDeveloperDownloadsForProject(LatestDownloadsForProject):
  basename = 'developer'

  def title(self, obj):
    return _("%s latest developer downloads" % obj.name)

  def description(self, obj):
    return _("The last %d developer downloads available for %s" % \
        (entries_per_feed, obj.name))

  def items(self, obj):
    return obj.download_set.order_by('-date')[:entries_per_feed]

class SparkleUpcastFeed(Rss201rev2Feed):
  """Special Sparkle Upcast feed, with all stuff that Sparkle wants to have."""

  def __init__(self, *args, **kwargs):
    super(SparkleUpcastFeed, self).__init__(*args, **kwargs)

  def root_attributes(self):
    attrs = super(SparkleUpcastFeed, self).root_attributes()
    attrs['xmlns:sparkle'] = \
        'http://www.andymatuschak.org/xml-namespaces/sparkle'
    attrs['xmlns:dc'] = 'http://purl.org/dc/elements/1.1/'
    return attrs

  def add_item_elements(self, handler, item):
    """Modifies the feed data, so it looks as we need"""
    super(SparkleUpcastFeed, self).add_item_elements(handler, item)
    handler.addQuickElement('sparkle:releaseNotesLink', contents=item['sparkle:releaseNotesLink'])
    handler.addQuickElement('enclosure', attrs=item['_enclosure'])

class SparkleUpdatesForProject(Feed):
  feed_type = SparkleUpcastFeed 
  basename = 'sparkle'

  def get_object(self, bits):
    if len(bits) != 1:
      raise ObjectDoesNotExist
    try:
      return Project.objects.get(name=bits[0])
    except:
      raise ObjectDoesNotExist

  def title(self, obj):
    return _("%s Changelog" % obj.name)

  def description(self, obj):
    return _("The last %d MacOSX Sparkle updates for %s" % \
        (entries_per_feed, obj.name))

  def link(self, obj):
    return "%s/project/%s" % (site.domain, obj.name)

  title_template = "feeds/sparkle_title.html"
  description_template = "feeds/sparkle_description.html"

  def items(self, obj):
    return obj.download_set.exclude(development__exact=True).order_by('-date')

  def item_link(self, item):
    return item.data.url 

  def item_pubdate(self, item):
    return item.date

  def item_extra_kwargs(self, item):
    attrs = {}
    attrs['sparkle:releaseNotesLink'] = \
        'http://%s/project/notes/%d' % (site.domain, item.id)
    attrs['_enclosure'] = {}
    attrs['_enclosure']['url'] = item.data.url 
    attrs['_enclosure']['length'] = str(item.data.size)
    attrs['_enclosure']['type'] = 'application/octet-stream'
    attrs['_enclosure']['sparkle:version'] = item.version 
    if item.dsa_digest:
      attrs['_enclosure']['sparkle:dsaSignature'] = item.dsa_digest
    return attrs

