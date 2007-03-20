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
  pub_type = models.CharField(_('Type of publication'), maxlength=64)
  abstract = models.TextField(_('A summary of the work'))
  files = models.ManyToManyField(File, filter_interface=models.HORIZONTAL)

  # make it translatable
  class Meta:
    verbose_name = _('publication')
    verbose_name_plural = _('publications')

  # make it admin'able
  class Admin:
    list_display = ('title', 'media', 'date')
    list_filter = ['date']
    search_fields = ['title', 'media', 'date']
    date_hierarchy = 'date'
    
  def __str__(self):
    return '%s (%s)' % (self.title, self.date)
