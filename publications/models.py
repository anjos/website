from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db import models
from files.models import File

class Publication(models.Model):
  """This model describes a publication in a magazine, journal or conference
  proceedings.
  """
  
  title = models.CharField(_('Title of the publication'), maxlength=256)
  date = models.DateField(_('Publishing date'))
  author_list = models.TextField(_('Author names'))
  pub_type = models.CharField(_('Type of publication'), maxlength=64)
  media = models.CharField(_('Journal or proceedings'), maxlength=256)
  volume = models.CharField(_('Volume'), null=True, blank=True, maxlength=16)
  number = models.CharField(_('Number'), null=True, blank=True, maxlength=16)
  pages = models.CharField(_('Pages'), null=True, blank=True, maxlength=16)
  abstract = models.TextField(_('Abstract'), blank=True)
  files = models.ManyToManyField(File, filter_interface=models.HORIZONTAL,
                                 null=True, blank=True)

  def count_files(self):
    """Counts the number of files attached to this publication."""
    return len(self.files.all())
  count_files.short_description = _('Files')

  def has_abstract(self):
    """Tells if this article has an abstract or not."""
    return len(str(self.abstract))
  has_abstract.short_description = _('Abstract')

  # make it translatable
  class Meta:
    verbose_name = _('publication')
    verbose_name_plural = _('publications')

  # make it admin'able
  class Admin:
    list_display = ('title', 'date', 'pub_type', 'has_abstract', 'count_files')
    list_filter = ['date']
    list_per_page = 10
    ordering = ['-date']
    search_fields = ['title', 'date', 'media']
    date_hierarchy = 'date'
    fields = (
        (None, {'fields': ('title', 'date', 'author_list', 
                           ('pub_type', 'media'),
                           ('volume', 'number', 'pages'), 
                           'abstract')}),
        (_('Files'), {'classes': 'collapse', 'fields': ('files',)}),
        )
    
  def __str__(self):
    return '%s (%s)' % (self.title, self.date.strftime('%B %Y'))
