from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()

@register.inclusion_tag('comment/block.html')
def comment_block(target):
    """
    评论块
    """
    form = CommentForm()
    comments = Comment.get_by_target(target)
    return {
        'target': target,
        'comment_form': form, 
        'comment_list': comments
    }