from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat

# Create your models here.
from files.models import File

class Publication_v1(models.Model):
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
  media = models.CharField(_('Publication name'), max_length=256)
  volume = models.CharField(_('Volume'), null=True, blank=True, max_length=16)
  number = models.CharField(_('Number'), null=True, blank=True, max_length=16)
  pages = models.CharField(_('Pages'), null=True, blank=True, max_length=16)
  abstract = models.TextField(_('Abstract'), blank=True)

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

  def __unicode__(self):
    return self.title + (' (%s)' % self.date.strftime('%b %y'))

class Publication(models.Model):
  """This model describes a publication in a magazine, journal or conference
  proceedings.
  """
 
  #
  # enumerations
  #
  publication_type =(('J', _(u'Journal')), 
                     ('C', _(u'Proceedings of Conference')),
                     ('T', _(u'Thesis')),
                     ('R', _(u'Technical Report')), 
                     ('O', _(u'Other')),
                    )

  publication_audience =(('N', _(u'National')), 
                         ('I', _(u'International')),
                        )

  title = models.CharField(_('Title of the publication'), max_length=256)
  date = models.DateField(_('Publishing date'))
  author_list = models.TextField(_('Author names'))
  publication_type = models.CharField(_('Type of publication'), max_length=1,
      null=False, blank=False, choices=publication_type)
  audience = models.CharField(_('Type of audience'), max_length=1,
      null=False, blank=False, choices=publication_audience)
  media = models.CharField(_('Publication name'), max_length=256)
  volume = models.CharField(_('Volume'), null=True, blank=True, max_length=16)
  number = models.CharField(_('Number'), null=True, blank=True, max_length=16)
  pages = models.CharField(_('Pages'), null=True, blank=True, max_length=16)
  abstract = models.TextField(_('Abstract'), blank=True)

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

  def __unicode__(self):
    return self.title + (' (%s)' % self.date.strftime('%b %y'))

class Document(File):
  """Describes a document that is associated with a publication."""
  
  # a document can only belong to a single publication
  publication=models.ForeignKey(Publication)

  def __unicode__(self):
      return u'%s (%s), belongs to "%s"' % (self.name, self.date, self.publication)

