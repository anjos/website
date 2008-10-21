from django.db import models
from django.utils.translation import ugettext_lazy as _
import os, logging

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

    curr_md5 = '' 

    if os.path.exists(self.data.path):
      import md5
      curr_md5 = md5.new(file(self.data.path,'rb').read()).hexdigest()

    else:
      logging.warn('File "%s" is not found. Ignoring MD5 settings.' % \
          self.data.path)

    if not self.md5:
      # calculate the md5sum for the user, based on the data we have received.
      # please note that in this case, if the transfer went wrong, so will be
      # the md5 sum.
      self.md5 = curr_md5

    else:
      # in this case, we check that the md5 sum of the data we received is
      # consistent with what the user passed us. If not, we just return
      if len(curr_md5) > 0 and self.md5 != curr_md5:
        logging.warn('File "%s" has a self calculated MD5 check sum of "%s", which does not match the user provided one "%s". Not saving.' % \
          (self.data.path, curr_md5, self.md5))
        return

    # this is called only if either the file is not available or the user
    # has supplied a matching md5 checksum.
    super(File, self).save(force_insert, force_update)

  # make it translatable
  class Meta:
    verbose_name = _('file')
    verbose_name_plural = _('files')

  def md5_checksum(self):
    """Checks and updates the MD5 if none is present"""
    if not self.md5:
      self.save()
      return True
    else:
      import md5
      return self.md5 != md5.new(file(self.data.path,'rb').read()).digest()

  def size(self):
    """Returns the size of this file, in bytes"""
    return self.data.size
  size.short_description = _('Size (bytes)')

  def __unicode__(self):
      return u'%s (%s)' % (self.name, self.date)
