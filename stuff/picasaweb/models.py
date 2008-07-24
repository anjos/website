from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _str
from django.utils.translation import string_concat  as _cat
# Picasaweb support from Google (search gdata.py)
import gdata.photos.service

# Create your models here.

class UserInfo:
  """Describes the user info class"""
  def __init__(self, user, nickname, uri, available_items, last_update, feed,
      thumbnail):
    self.user = user
    self.nickname = nickname
    self.uri = uri
    self.available_items = available_items
    self.last_update = last_update
    self.feed = feed
    self.thumbnail = thumbnail
    if self.feed: self.is_valid = True
    else: self.is_valid = False

class PicasawebAccount(models.Model):
  """This model describes an user account in picasaweb."""

  email = models.CharField(_('Picasaweb e-mail'), max_length=256, unique=True,
      help_text=_('Insert the e-mail of a picasaweb user in the form of user@domain'))
  num_albums = models.PositiveSmallIntegerField(\
    _('Number of albums to display'), default=0,
    help_text=_('The special value of 0 (zero) will display all albums'))

  def _cache_userinfo(self):
    """Returns user information, packed in a special object type."""
    if not hasattr(self, '__userinfo__'):
      try:
        pws = gdata.photos.service.PhotosService()
        feed = pws.GetUserFeed(user=self.email, limit=0)
        self.__userinfo__ = UserInfo(feed.user.text,
                                     feed.nickname.text,
                                     feed.author[0].uri.text,
                                     feed.total_results.text,
                                     feed.updated.text,
                                     feed.id.text,
                                     feed.thumbnail.text)
      except gdata.photos.service.GooglePhotosException:
        self.__userinfo__ = UserInfo('', '', '', '', '', '')
    return self.__userinfo__

  # dynamic property
  userinfo = property(_cache_userinfo)

  def _cache_feed(self):
    if not hasattr(self, '__feed__'):
      try:
        pws = gdata.photos.service.PhotosService()
        limit = None
        if self.num_albums > 0: limit = self.num_albums
        self.__feed__ = \
            pws.GetUserFeed(user=self.email, limit=limit)
        # if you cache the feed, also cache user info
        self.__userinfo__ = UserInfo(self.__feed__.user.text,
                                     self.__feed__.nickname.text,
                                     self.__feed__.author[0].uri.text,
                                     self.__feed__.total_results.text,
                                     self.__feed__.updated.text,
                                     self.__feed__.id.text,
                                     self.__feed__.thumbnail.text)
      except gdata.photos.service.GooglePhotosException:
        self.__feed__ = None
    return self.__feed__

  # dynamic property
  feed = property(_cache_feed)

  def __str__(self):
    """A string representation of myself"""
    if self.num_albums:
      if self.num_albums == 1:
        return _str('Last uploaded album of %(email)s' % {'email': self.email})
      else:
        return _str('%(email)s, last %(num_albums)s albums' % \
            {'email': self.email, 'num_albums': self.num_albums})

    return _str('%(email)s' % {'email': self.email})
