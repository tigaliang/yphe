import webapp2

from ypapp.controllers import page_renderer


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        # self.response.write('welcome!!!')
        self.response.write(page_renderer.render_main_page())


app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/', MainPage)
    ],
    config={
        'webapp2_extras.sessions': {'secret_key': 'F1DFFCE5D977BB04B544897FDB65B37F0DAC913C99598F0337A7FC2875391772'}
    },
    debug=True
)
