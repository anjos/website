from django.db import models
from django.utils.translation import gettext_lazy as _
from settings import MEDIA_URL

# Create your models here.

class File(models.Model):
  """This model describes an uploaded file.
  """
  name = models.CharField(_('Name'), maxlength=256)
  description = models.TextField(_('Description'), null=True, blank=True)
  data = models.FileField(_('File'),
                          upload_to='%Y/%m/%d')
  date = models.DateTimeField(_('Upload date'), auto_now_add=True)
  public = models.BooleanField(_('Publicly visible'), default=True)

  # make it translatable
  class Meta:
    verbose_name = _('file')
    verbose_name_plural = _('files')

  # make it admin'able
  class Admin:
    list_display = ('name', 'date', 'public')
    list_filter = ['date']
    search_fields = ['name', 'date']
    date_hierarchy = 'date'
    list_per_page = 10
    ordering = ['-date']

  def url(self):
    """Returns a valid URL for this entry"""
    return MEDIA_URL + self.data

  def __str__(self):
      return '%s (%s)' % (self.name, self.date)
