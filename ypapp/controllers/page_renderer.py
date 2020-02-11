from ypapp import schools
from ypapp.controllers import school_renderer


def render_main_page():
    html = u'<html><body>{}</body></html>'
    schools_html = []
    school_list = \
        [
            schools.Szsy()
        ]
    for school in school_list:
        schools_html.append(school_renderer.render_school(school))
    return html.format('<br>'.join(schools_html))
