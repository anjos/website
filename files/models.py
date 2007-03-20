from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class File(models.Model):
  """This model describes an uploaded file.
  """
  
  title = models.CharField(_('File name'), maxlength=256)
  data = models.FileField('File',
                          upload_to='%Y/%m/%d')
  date = models.DateField(_('Upload date'), auto_now_add=True)

  # make it translatable
  class Meta:
    verbose_name = _('file')
    verbose_name_plural = _('files')

  # make it admin'able
  class Admin:
    list_display = ('title', 'date')
    list_filter = ['date']
    search_fields = ['title', 'date']
    date_hierarchy = 'date'

  def __str__(self):
      return '%s (%s)' % (self.title, self.date)
