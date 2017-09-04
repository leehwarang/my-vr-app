#앞으로 작성할 사용자 정의 템플릿 필터 파일

from django import template
import re

register = template.Library()

@register.filter
def add_link(value): #post객체가 value(파라미터)로 들어온다.
    hashtag= value.hashtag
    tags = value.tag_set.all()
    for tag in tags:
        hashtag = re.sub(r'\#' + tag.name + r'\b',
                        '<a href="/post/explore/tags/' + tag.name + '">#' + tag.name + '</a>', hashtag)
    return hashtag