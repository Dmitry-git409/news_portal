from django_filters import FilterSet, CharFilter, ChoiceFilter, DateFromToRangeFilter
from news.models import Post


class PostFilter(FilterSet):
    AU = [(1, 'Victor'), (2, 'Boris')]
    title = CharFilter(label='Title', lookup_expr='icontains')
    to_author = ChoiceFilter(label='Author', lookup_expr='in', choices=AU)
    time_create = DateFromToRangeFilter(label='Time Create', lookup_expr='gte')

    class Meta:
        model = Post
        # fields = {'time_create': ['gte'],
        #           'title': ['icontains'],
        #           'to_author': ['in']
        #           }
        fields = ['title', 'to_author', 'time_create']


