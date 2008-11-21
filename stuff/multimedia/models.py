from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat
import files.models 

movie_extensions = ('mpg', 'avi', 'mpeg2', 'mov', 'wmv', 'mp2', 'mp4', 'xvid',
                    'divx')
audio_extensions = ('mp3', 'wma', 'wav', 'aac', 'ogg')
picture_extensions = ('jpg', 'jpeg', 'bmp', 'png', 'gif', 'pdf')

class Item(models.Model):
  """Describes an item displayed in my Multimedia gallery"""

  category_choices = (('M', _(u'Media')),
                      ('P', _(u'Personal')),
                      ('V', _(u'Varieties')),
                     )

  category = models.CharField(_('Category'), max_length=1,
      help_text=_('Choose the category of your file. Media events are the default shown in the multimedia start page.'), null=False, blank=False, choices=category_choices)

  # make it translatable
  class Meta:
    verbose_name = _('multimedia item')
    verbose_name_plural = _('multimedia item')

class Embedded(Item):
  """Describes an embedded (external link to flash-based websites) object"""
 
  name = models.CharField(_('Name'), max_length=256,
      help_text=_('The name of the file. Can contain spaces and other special characters'))
  date = models.DateTimeField(_('Upload date'), auto_now_add=True,
      help_text=_('Sets the insertion date of this object'))
  description = models.TextField(_('Description'), null=True, blank=True,
      help_text=_('Explain what this object is - be verbose!'))
  object = models.TextField(_('Embedded object'), null=False, blank=False,
      help_text=_('Paste in this field, the HTML instructions to embed the object you want.'))

  # make it translatable
  class Meta:
    verbose_name = _('embedded multimedia object')
    verbose_name_plural = _('embedded multimedia objects')

  def describe(self):
    """Describes the object in more details..."""

    # a simple approach for now...
    return self.description

  def thumbnail(self):
    return self.object

  def __unicode__(self):
    return u'%s (%s), filed under %s' % (self.name, self.date,
          self.get_category_display())

class File(files.models.File,Item):
  """Describes a multimedia file, uploaded to the website."""

  preview = models.FileField(_('Preview'), upload_to='%Y/%m/%d/preview',
      help_text=_('Specify here the preview image (300x300 pixels) that will be shown. If you don\'t specify anything, this web application will try its best to come up with a thumbnail for your entry.'))

  # make it translatable
  class Meta:
    verbose_name = _('multimedia file')
    verbose_name_plural = _('multimedia files')

  def thumbnail(self):
    """Returns the HTML object to be embedded as the preview..."""
    return '<img src="%s"/>' % self.preview.url

  def describe(self):
    """Describes the object in more details..."""

    # a simple approach for now...
    return self.description

  def __unicode__(self):
    return u'%s (%s), filed under %s' % (self.name, self.date,
          self.get_category_display())

