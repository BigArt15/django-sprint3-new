from django.contrib.auth import get_user_model
from django.db import models

from .querysets import PostQuerySet, PublishedQuerySet

User = get_user_model()

MAX_LENGTH = 256


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    objects = PublishedQuerySet.as_manager()

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField("Заголовок", max_length=MAX_LENGTH)
    description = models.TextField("Описание")
    slug = models.SlugField(
        "Идентификатор",
        unique=True,
        max_length=MAX_LENGTH,
        help_text=(
            "Идентификатор страницы для URL; разрешены символы латиницы, "
            "цифры, дефис и подчёркивание."
        ),
    )

    class Meta(PublishedModel.Meta):
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Location(PublishedModel):
    name = models.CharField("Название места", max_length=MAX_LENGTH)

    class Meta(PublishedModel.Meta):
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField("Заголовок", max_length=MAX_LENGTH)
    text = models.TextField("Текст")
    pub_date = models.DateTimeField(
        "Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — можно делать "
            "отложенные публикации."
        ),
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор публикации"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name="Категория",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Местоположение",
    )

    objects = PostQuerySet.as_manager()

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title
