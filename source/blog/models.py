from django.db import models
from django.core.urlresolvers import reverse
import markdown


CATEGORIES = (
    ('technology', 'Gadgets and General Tech'),
    ('polandliving', 'Life in Poland'),
    ('coffee','Coffee and all Related'),
    ('interesting', 'Interesting Stuff'),
    ('ramble', 'Ramblings'),
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date Published', auto_now=True)
    description = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    published = models.BooleanField(default=False)
    category = models.CharField(max_length=255, choices=CATEGORIES)

    html_content = models.TextField(blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

    def save(self, *args, **kwargs):
        self.html_content = markdown.markdown(self.content)
        super(Post, self).save(*args, **kwargs)

class Image(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to="blog-images")
    alt = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
