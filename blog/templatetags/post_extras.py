#앞으로 작성할 사용자 정의 템플릿 필터 파일

from django import template
import re

register = template.Library()

@register.filter
def add_spot_link(value): #사용자가 클릭한 post객체가 value(파라미터)로 들어온다.
    hashtag= value.hashtag #이 post의 hashtag 문자열은 이거고...
    tags = value.tag_set.all() #이 post의 tag_set을 모두 꺼내서 tags객체에 넣어
    for tag in tags:
        hashtag = re.sub(r'\#' + tag.name + r'\b',
                        '<a href="/spot/explore/tags/' + tag.name + '">#' + tag.name + '</a>', hashtag)
    return hashtag

@register.filter
def add_accomodation_link(value): #사용자가 클릭한 post객체가 value(파라미터)로 들어온다.
    hashtag= value.hashtag #이 post의 hashtag 문자열은 이거고...
    tags = value.tag_set.all() #이 post의 tag_set을 모두 꺼내서 tags객체에 넣어
    for tag in tags:
        hashtag = re.sub(r'\#' + tag.name + r'\b',
                        '<a href="/accomodation/explore/tags/' + tag.name + '">#' + tag.name + '</a>', hashtag)
    return hashtag



