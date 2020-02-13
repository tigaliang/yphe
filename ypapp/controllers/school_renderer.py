def render_school(school):
    body_template = u'<h2><a href="{}" style="color:black; text-decoration:none">{}</a></h2>{}'
    item_template = u'<li>[{}]&nbsp;<a href="{}" target="_blank">{}</a></li>'
    items = []
    for news_item in school.news_list():
        items.append(
            item_template.format(
                news_item.date if news_item.date else '0000-00-00',
                news_item.url,
                news_item.title
            )
        )
    return body_template.format(
        school.home_page_url,
        school.title,
        ''.join(items)
    )
