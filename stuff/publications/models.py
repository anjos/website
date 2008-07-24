from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat

# Create your models here.
from files.models import File

def unicode2html(s):
  """Converts the unicode string given as input into HTML entities."""
  from htmlentitydefs import codepoint2name as c2n
  r = u''
  for k in s:
    if c2n.has_key(ord(k)): r += '&' + c2n[ord(k)] + ';'
    else: r += k
  return r

class Publication(models.Model):
  """This model describes a publication in a magazine, journal or conference
  proceedings.
  """
  
  title = models.CharField(_('Title of the publication'), max_length=256)
  date = models.DateField(_('Publishing date'))
  author_list = models.TextField(_('Author names'))
  pub_type = models.CharField(_('Type of publication'), max_length=64)
  media = models.CharField(_('Journal or proceedings'), max_length=256)
  volume = models.CharField(_('Volume'), null=True, blank=True, max_length=16)
  number = models.CharField(_('Number'), null=True, blank=True, max_length=16)
  pages = models.CharField(_('Pages'), null=True, blank=True, max_length=16)
  abstract = models.TextField(_('Abstract'), blank=True)
  files = models.ManyToManyField(File, null=True, blank=True)

  def count_files(self):
    """Counts the number of files attached to this publication."""
    return len(self.files.all())
  count_files.short_description = _('Files')

  def has_abstract(self):
    """Tells if this article has an abstract or not."""
    return bool(len(self.abstract))
  has_abstract.short_description = _('Abstract')

  # make it translatable
  class Meta:
    verbose_name = _('publication')
    verbose_name_plural = _('publications')

  def __str__(self):
    return unicode2html(self.title + (' (%s)' % self.date.strftime('%B %Y')))
