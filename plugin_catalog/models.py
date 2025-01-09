from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

from app_core.models import Page


class Catalog(models.Model):
    MODEL_ARTICLE = 'article'
    MODEL_PRODUCT = 'product'
    MODEL_CHOICES = (
        (MODEL_ARTICLE, 'مقاله'),
        (MODEL_PRODUCT, 'محصول'),
    )
    TYPE_LIST = 'list'
    TYPE_GRID = 'grid'
    TYPE_CHOICES = (
        (TYPE_LIST, 'لیست'),
        (TYPE_GRID, 'گرید'),
    )

    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    model = models.CharField(max_length=255, choices=MODEL_CHOICES, verbose_name='مدل')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع کاتالوگ')
    name = models.CharField(max_length=255, verbose_name='نام کاتالوگ')
    see_all_link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک موارد بیشتر')
    with_background = models.BooleanField(default=False, verbose_name='پس‌زمینه دارد؟')
    background_color = models.CharField(max_length=255, blank=True, null=True, verbose_name='رنگ پس‌زمینه')
    with_header = models.BooleanField(default=False, verbose_name='سربرگ دارد؟')
    header_image_desktop = models.ImageField(upload_to='images/plugin/list/', default='images/plugin/list/default.png', 
                                             validators=[FileExtensionValidator(['png, jpg, jpeg, webp, svg'])], 
                                             blank=True, null=True, verbose_name='تصویر سربرگ (دسکتاپ)')
    header_image_mobile = models.ImageField(upload_to='images/plugin/list/', default='images/plugin/list/default.png', 
                                            validators=[FileExtensionValidator(['png, jpg, jpeg, webp, svg'])], 
                                            blank=True, null=True, verbose_name='تصویر سربرگ (موبایل)')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات تصویر')

    class Meta:
        verbose_name = 'کاتالوگ'
        verbose_name_plural = 'لیست کاتالوگ‌ها'

    def __str__(self):
        return self.name


class CatalogSet(models.Model):
    GENERATED_AUTO = 'auto'
    GENERATED_MANUAL = 'manual'
    GENERATED_CHOICES = (
        (GENERATED_AUTO, 'خودکار'),
        (GENERATED_MANUAL, 'دستی'),
    )

    generated = models.CharField(max_length=255, choices=GENERATED_CHOICES, verbose_name='روش تولید')
    name = models.CharField(max_length=255, verbose_name='نام گروه')
    max_items = models.IntegerField(default=0, verbose_name='حداکثر تعداد')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')

    class Meta:
        verbose_name = 'مجموعه‌ی کاتالوگ'
        verbose_name_plural = 'مجموعه‌های کاتالوگ'

    def __str__(self):
        return self.name


class CatalogSetItem(models.Model):
    set = models.ForeignKey(CatalogSet, on_delete=models.CASCADE, verbose_name='شناسه مجموعه')
    item = models.IntegerField(verbose_name='شناسه مورد')

    class Meta:
        verbose_name = 'اجزا کاتالوگ'
        verbose_name_plural = 'لیست اجزا کاتالوگ'

    def __str__(self):
        return f'{self.set.name} - {self.item}'


class CatalogContent(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='')
    set = models.F
