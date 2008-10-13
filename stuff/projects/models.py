from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat
from files.models import File, unicode2html

class Project(models.Model):
  """Describes a software project."""
  
  name = models.CharField(_('Project name'), max_length=256,
      help_text=_('Insert a short, meaningful name for your project.'))
  date = models.DateField(_('Start date'), auto_now_add=True,
      help_text=_('The start date of this project.'))
  description = models.TextField(_('Description'), null=True, blank=True,
      help_text=_('The description of the project is presented on its detailed view page. You should be really descriptive here.'))
  vc_url = models.CharField(_('Version control repository URL'), max_length=1024,
      help_text=_('Complete URL to view your version control repository for this project'))
  trunk_dir = models.CharField(_('Version control trunk subdirectory'),
      max_length=256, default='/trunk', help_text=_('The directory within your repository that holds the main trunk of this project\'s development'))
  wiki_page = models.CharField(_('Wiki page'), max_length=1024,
      help_text=_('Complete URL for the top wiki page of your project'))
  dsa_pubkey = models.TextField(_('DSA project key'), null=True, blank=True,
      help_text=_('If you have one, insert here the <b>public</b> DSA key for this project.')) 

  def count_downloads(self):
    """Counts the number of downloads attached to this project."""
    return len(self.download_set.all())
  count_downloads.short_description = _('Downloads')

  # make it translatable
  class Meta:
    verbose_name = _('project')
    verbose_name_plural = _('projects')

  def __str__(self):
    return unicode2html(self.name + (' (%s)' % self.date.strftime('%B %Y')))

class Download(File):
  """Describes a file that is associated with a project and can be downloaded."""

  dsa_digest=models.CharField(_('DSA Digest'), max_length=256, blank=True,
      null=True,
      help_text=_('Insert the DSA digest for this download. It will be used to check the file sanity and authenticate it'))
  release_notes=models.TextField(_('Release notes'), blank=True, null=True,
      help_text=_('Be verbose and descriptive about this new download to your project.'))
  development=models.BooleanField(_('Developer release'), default=True,
    help_text=_('Mark this box if you want this download to be only visible to developers subscribing a special feed.'))
  tag_dir = models.CharField(_('VC tag directory for this release'),
      max_length=256, default='/tags', help_text=_('The directory within your repository that holds the tagged trunk of this project\'s development'))

  # a download can only belong to a single project
  project=models.ForeignKey(Project)

  # make it translatable
  class Meta:
    verbose_name = _('download')
    verbose_name_plural = _('downloads')

