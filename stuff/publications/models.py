from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat

# Create your models here.
from files.models import File, unicode2html

class Publication(models.Model):
  """This model describes a publication in a magazine, journal or conference
  proceedings.
  """
 
  # TODO: missing here is the implementation of:
  # a) the type of publication: journal, conference, other
  # b) the "internationality of the publication: "brazilian" (national) or
  # international

  title = models.CharField(_('Title of the publication'), max_length=256)
  date = models.DateField(_('Publishing date'))
  author_list = models.TextField(_('Author names'))
  pub_type = models.CharField(_('Type of publication'), max_length=64)
  media = models.CharField(_('Journal or proceedings'), max_length=256)
  volume = models.CharField(_('Volume'), null=True, blank=True, max_length=16)
  number = models.CharField(_('Number'), null=True, blank=True, max_length=16)
  pages = models.CharField(_('Pages'), null=True, blank=True, max_length=16)
  abstract = models.TextField(_('Abstract'), blank=True)

  # just for a second
  files = models.ManyToManyField(File, null=True, blank=True)

  def count_documents(self):
    """Counts the number of documents attached to this publication."""
    return len(self.document_set.all())
  count_documents.short_description = _('Documents')

  def has_abstract(self):
    """Tells if this article has an abstract or not."""
    return bool(len(self.abstract))
  has_abstract.short_description = _('Abstract')

  # make it translatable
  class meta:
    verbose_name = _('publication')
    verbose_name_plural = _('publications')

  def __str__(self):
    return unicode2html(self.title + (' (%s)' % self.date.strftime('%b %y')))

class Document(File):
  """Describes a document that is associated with a publication."""
  
  # a document can only belong to a single publication
  publication=models.ForeignKey(Publication)

  def __str__(self):
      return '%s (%s), belongs to "%s"' % (self.name, self.date, self.publication)

