from django.db import models
from django.utils.text import slugify


# Create your models here.

class Citys(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=1000, unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Şehir"
        verbose_name_plural = "Şehirler"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Citys.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Citys.DoesNotExist:
                    self.slug = slug
                    break
        super(Citys, self).save(*args, **kwargs)


class County(models.Model):
    name = models.CharField(max_length=60)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "İlçe"
        verbose_name_plural = "İlçeler"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = County.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except County.DoesNotExist:
                    self.slug = slug
                    break
        super(County, self).save(*args, **kwargs)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=1000, unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mahalle"
        verbose_name_plural = "Mahalleler"
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            slug = slugify(self.name)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Neighbourhood.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Neighbourhood.DoesNotExist:
                    self.slug = slug
                    break
        super(Neighbourhood, self).save(*args, **kwargs)
