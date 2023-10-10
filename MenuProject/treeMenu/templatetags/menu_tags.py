from django import template
from django.db.models import Q
from treeMenu.models import Item


register = template.Library()


@register.inclusion_tag('treeMenu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    item_pk = None
    parents = []
    if 'item' in context.request.GET:
        item_pk = context.request.GET['item']
        if 'parents' in context.request.GET:
            parents = context.request.GET['parents'].split('_')
    menu_items = Item.objects.filter(Q(menu__name=menu_name) & (
                                     Q(parent=None) |
                                     Q(parent=item_pk) |
                                     Q(parent__in=parents)))
    return {
        'menu_items': menu_items
    }
