from slugify import slugify
from django.db import models


class SlugModel(models.Model):
    slug = models.SlugField(max_length=128, unique=True, db_index=True, blank=True, null=True)
    _slug_source = 'name'

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(SlugModel, self).__init__(*args, **kwargs)
        self._prev_slug = self._get_proposed_slug()
        self.slug = self._get_proposed_slug()

    def _get_proposed_slug(self):
        max_length = self.__class__._meta.get_field('slug').max_length
        source = getattr(self, self._slug_source)
        if source is not None:
            slug = orig = slugify(source, to_lower=True)[:max_length]

            for x in range(1):
                qs = self.__class__.objects.filter(slug=slug)
                if self.pk:
                    qs = qs.exclude(pk=self.pk)
                if not qs.exists():
                    break
                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

            return slug

    def save(self, *args, **kwargs):
        # populate slug
        if self._prev_slug != self._get_proposed_slug():
            self._prev_slug = self.slug = self._get_proposed_slug()

        return super(SlugModel, self).save(*args, **kwargs)
