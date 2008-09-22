from django.db import models
from django.utils.translation import ugettext_lazy as _
from settings import MEDIA_ROOT
import os

# Create your models here.

class File(models.Model):
  """This model describes an uploaded file.
  """
  name = models.CharField(_('Name'), max_length=256,
      help_text=_('The name of the file. Can contain spaces and other special characters'))
  description = models.TextField(_('Description'), null=True, blank=True,
      help_text=_('Explain what this file is - be verbose!'))
  data = models.FileField(_('File'), upload_to='%Y/%m/%d',
      help_text=_('Specify here the file that will be uploaded.'))
  date = models.DateTimeField(_('Upload date'), auto_now_add=True,
      help_text=_('Sets the insertion date of this file'))
  public = models.BooleanField(_('Publicly visible'), default=True,
      help_text=_('Sets the visibility of this file for not anonymous users.'))
  md5 = models.CharField(_('MD5 checksum'), max_length=256, null=True, blank=True,
      help_text=_('Insert an optional MD5 checksum. If you leave it blank I\'ll calculate the checksum based on the file contents I stored'))

  def save(self, force_insert=False, force_update=False):

    curr_md5 = None

    if os.path.exists(self.path()):
      import md5
      curr_md5 = md5.new(file(self.path(),'rb').read()).hexdigest()

    else:
      return

    if not self.md5:
      # calculate the md5sum for the user, based on the data we have received.
      # please note that in this case, if the transfer went wrong, so will be
      # the md5 sum.
      self.md5 = curr_md5

    else:
      # in this case, we check that the md5 sum of the data we received is
      # consistent with what the user passed us. If not, we just return
      if self.md5 != curr_md5: return

    super(File, self).save(force_insert, force_update)

  # make it translatable
  class Meta:
    verbose_name = _('file')
    verbose_name_plural = _('files')

  def url(self):
    """Returns a valid URL for this entry"""
    return self.data.url

  def path(self):
    """Returns a valid URL for this entry"""
    return os.path.join(MEDIA_ROOT, self.data.name)

  def md5_checksum(self):
    """Checks and updates the MD5 if none is present"""
    if not self.md5:
      self.save()
      return True
    else:
      import md5
      return self.md5 != md5.new(file(self.path(),'rb').read()).digest()

  def __str__(self):
      return '%s (%s)' % (self.name, self.date)
