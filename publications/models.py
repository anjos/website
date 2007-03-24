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
  media = models.CharField(_('Journal or proceedings'), maxlength=256)
  number = models.TextField(_('Number'), null=True, blank=True, maxlength=16)
  volume = models.TextField(_('Volume'), null=True, blank=True, maxlength=16)
  pages = models.TextField(_('Pages'), null=True, blank=True, maxlength=16)
  pub_type = models.CharField(_('Type of publication'), maxlength=64)
  abstract = models.TextField(_('A summary of the work'), blank=True)
  files = models.ManyToManyField(File, filter_interface=models.HORIZONTAL,
                                 null=True, blank=True)

  def count_files(self):
    """Counts the number of files attached to this publication."""
    return len(self.files.all())

  # make it translatable
  class Meta:
    verbose_name = _('publication')
    verbose_name_plural = _('publications')

  # make it admin'able
  class Admin:
    list_display = ('title', 'media', 'date', 'count_files')
    list_filter = ['date']
    ordering = ['-date']
    search_fields = ['title', 'media', 'date']
    date_hierarchy = 'date'
    
  def __str__(self):
    return '%s (%s)' % (self.title, self.date.strftime('%B %Y'))
