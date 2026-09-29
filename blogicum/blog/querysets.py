from django.db import models
from django.utils import timezone


class PublishedQuerySet(models.QuerySet):
    """Базовый QuerySet для моделей с флагом is_published."""

    def published(self):
        return self.filter(is_published=True)


class PostQuerySet(PublishedQuerySet):
    """Кастомный QuerySet с бизнес-фильтрами для Post."""

    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )
