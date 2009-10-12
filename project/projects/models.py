from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat
from conf import settings

class Project(models.Model):
  """Describes a software project."""
  
  name = models.CharField(_('Project name'), max_length=128, help_text=_('Insert a short, meaningful unique name for your project.'))

  slug = models.SlugField(_('Slug'), max_length=32, primary_key=True, help_text=_('Insert a short, meaningful unique slug for your project. Only letters, digits and underscores.'))

  date = models.DateField(_('Start date'), help_text=_('The start date of this project.'))

  updated = models.DateField(_('Last update'), auto_now_add=True, help_text=_('The date on the last update of this project description.'))

  brief = models.CharField(_('Brief description'), max_length=1024, help_text=_('Brief description of this project (max %d characters)' % 1024))

  description = models.TextField(_('Description'), null=True, blank=True, help_text=_('The description of the project is presented on its detailed view page. You should be really descriptive here.'))

  clone_url = models.CharField(_('Clone URL'), max_length=1024, help_text=_('The cloning URL for this project.'))

  git_dir = models.FilePathField(_('Git directory'), path=PROJECTS_GIT_BASE_DIRECTORY, match=r'.*\.git$', recursive=True, max_length=1024, help_text=_('Name of the git directory containing your project. This path has to be relative to the base git directory.'))

  wiki_page = models.CharField(_('Wiki page'), max_length=1024, help_text=_('Complete URL for the top wiki page of your project'))

  dsa_pubkey = models.TextField(_('DSA project key'), null=True, blank=True, help_text=_('If you have one, insert here the <b>public</b> DSA key for this project.')) 

  def count_downloads(self):
    """Counts the number of public downloads attached to this project."""
    return len(self.public_downloads())
  count_downloads.short_description = _('Public downloads')

  def public_downloads(self):
    return self.download_set.filter(development=False)

  def count_all_downloads(self):
    """Counts the number of downloads attached to this project."""
    return len(self.download_set.all())
  count_all_downloads.short_description = _('All downloads')

  def count_screenshots(self):
    """Counts the number of screenshots attached to this project."""
    return len(self.screenshot_set.all())
  count_screenshots.short_description = _('Screenshots')

  def count_icons(self):
    """Counts the number of icons attached to this project."""
    return len(self.icon_set.all())
  count_icons.short_description = _('Icons')
  
  def updated_on(self):
    """Returns the last modification time for this project.
    
    Returns the last time a download was added to this project or the last
    time a modification was done to its description (the most recent of the two
    is returned."""
    downloads = [k.date for k in self.download_set.all()]
    screenshots = [k.date for k in self.screenshot_set.all()]
    icons = [k.date for k in self.icon_set.all()]
    latest = None
    if downloads: latest = max(downloads)
    if screenshots and max(screenshots) > latest: latest = max(screenshots)
    if icons and max(icons) > latest: latest = max(icons)

    if latest:
      from datetime import datetime, time
      uptime = datetime.combine(self.updated, time(0))
      if  uptime > latest:
        return self.updated
      return latest.date()
    else:
      return self.updated
  updated_on.short_description = _('Last updated')

  # make it translatable
  class Meta:
    verbose_name = _('project')
    verbose_name_plural = _('projects')

  def __unicode__(self):
    return self.name

# Place project files in a specific project directory 
def upload_path(instance, filename):
  path = os.path.join('projects', instance.project.slug)
  if isinstance(instance, Download): path = os.path.join(path, 'downloads')
  if isinstance(instance, Screenshot): path = os.path.join(path, 'screenshots')
  if isinstance(instance, Icon): path = os.path.join(path, 'icons')
  path = os.path.join(path, datetime.date.today().strftime('%Y-%m-%d'))
  return os.path.join(path, os.path.basename(filename).lower())

class Download(models.Model):
  """Describes a download associated with a project."""

  name = models.CharField(_('Name'), max_length=256, help_text=_('The name of the file. Can contain spaces and other special characters'))

  description = models.TextField(_('Description'), null=True, blank=True, help_text=_('Explain what this file is - be verbose!'))

  summary=models.CharField(_('Short description'), max_length=1024, blank=False, null=False, help_text=_('Enter an (obligatory) short description of this download'))

  data = models.FileField(_('Download'), upload_to=upload_path, help_text=_('Specify here the file that will be uploaded.'))

  date = models.DateTimeField(_('Upload date'), auto_now_add=True, help_text=_('Sets the insertion date of this file'))

  version=models.CharField(_('Version'), max_length=128, blank=False, null=False, help_text=_('Enter an alpha-numeric version identifier for this download (e.g. 0.3.7, or r245). Please note we may try to find the location of this tag inside your repository, so matching version names and tags is a good idea.'))

  dsa_digest=models.CharField(_('DSA Digest'), max_length=256, blank=True, null=True, help_text=_('Insert the DSA digest for this download. It will be used to check the file sanity and authenticate it'))

  development=models.BooleanField(_('Developer release'), default=True, help_text=_('Mark this box if you want this download to be only visible to developers subscribing a special feed.'))

  project=models.ForeignKey(Project, null=False, blank=False)

  # make it translatable
  class Meta:
    verbose_name = _('download')
    verbose_name_plural = _('downloads')
    unique_together = ('project', 'version')

class Screenshot(models.Model):
  """Describes a screenshot of your project"""

  name = models.CharField(_('Name'), max_length=256, help_text=_('The name of the file. Can contain spaces and other special characters'))

  data = models.ImageField(_('Screenshot'), upload_to=upload_path, help_text=_('Specify here the file that will be uploaded.'))

  date = models.DateTimeField(_('Upload date'), auto_now_add=True, help_text=_('Sets the insertion date of this file'))

  project=models.ForeignKey(Project)

  # make it translatable
  class Meta:
    verbose_name = _('screenshot')
    verbose_name_plural = _('screenshots')

class Icon(models.Model):
  """Describes an icon file associated with a project"""

  data = models.ImageField(_('Icon'), upload_to=upload_path, help_text=_('Specify here the file that will be uploaded.'))

  date = models.DateTimeField(_('Upload date'), auto_now_add=True, help_text=_('Sets the insertion date of this file'))

  project=models.ForeignKey(Project)

  # make it translatable
  class Meta:
    verbose_name = _('icon')
    verbose_name_plural = _('icons')
