from django.db import models

# Create your models here.
from django.db import models
from files.models import File

class Publication(models.Model):
  """This model describes a publication in a magazine, journal or conference
  proceedings.
  """
  
  title = models.CharField('Title of the publication', maxlength=256)
  date = models.DateField('Publishing date')
  author_list = models.TextField('Author names')
  media = models.CharField('Journal or proceedings', maxlength=256)
  pub_type = models.CharField('Type of publication', maxlength=64)
  abstract = models.TextField('A summary of the work')
  files = models.ManyToManyField(File, filter_interface=models.HORIZONTAL)

  # make it admin'able
  class Admin:
    list_display = ('title', 'media', 'date')
    list_filter = ['date']
    search_fields = ['title', 'media', 'date']
    date_hierarchy = 'date'
    
  def __str__(self):
    return '%s (%s)' % (self.title, self.date)
