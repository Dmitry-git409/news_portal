from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    obscene_words = ['fuck', 'shit', 'blackman']
    for i in obscene_words:
        val = value.replace(i, '.....')
        value = val
    return val
