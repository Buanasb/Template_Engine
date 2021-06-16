from django.db import models

# Create your models here.


class logo_navbar(models.Model):
    name = models.CharField(max_length=10, null=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class btn_navbar(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


class desc_content(models.Model):
    title = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title


class btn_content(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class desc_offer(models.Model):
    title = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title


class content_offer(models.Model):
    title = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.title


class desc_mountain(models.Model):
    title = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title


class content_mountain(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=30, null=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class desc_tool(models.Model):
    title = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title


class content_tool(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=30, null=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class title_cta(models.Model):
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title


class btn_cta(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


class content_footer(models.Model):
    title = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.title
