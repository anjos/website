from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
import feedparser 

class DeliciousAccount(models.Model):
  """This model describes an user account in del.icio.us."""

  account = models.CharField(_('Del.icio.us account'), max_length=256,                               unique=True, 
                             help_text=_('Insert the del.icio.us account name you want added to this website'))
  num_posts = models.PositiveSmallIntegerField(\
    _('Number of posts to display'), default=0,
    help_text=_('Number of posts to retrieve. The special value zero retrieves the default number of posts allowed by delicious (currently is 15).'))

  def _cache_feed(self):
    if not hasattr(self, '__feed__'):
      try:
        data = self.account 
        if self.num_posts > 0: data += '?count=%d' % self.num_posts 
        self.__feed__ = \
            feedparser.parse('http://feeds.delicious.com/v2/rss/%s' % data)
      except Exception: 
        self.__feed__ = None
    return self.__feed__

  # dynamic property
  feed = property(_cache_feed)

  def __unicode__(self):
    """A string representation of myself"""
    if self.feed:
      if self.num_posts == 0:
        return ugettext(u'%(account)s@del.icio.us, default number of posts' % {'account': self.account})
      else:
        return ugettext('%(account)s@del.icio.us, last %(num_posts)s ' % \
            {'account': self.account, 'num_posts': self.num_posts})

    return ugettext('%(account)s@del.icio.us [unknown user?]' % {'account': self.account})
