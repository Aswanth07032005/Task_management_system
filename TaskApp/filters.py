import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_search',
        label='Search Tasks'
    )

    class Meta:
        model = Task
        fields = []

    def filter_search(self, queryset, name, value):
        from django.db.models import Q

        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value)
        )