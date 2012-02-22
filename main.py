import os
from google.appengine.api import users
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class Link(db.Model):
    user = db.UserProperty()
    url = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class Links(webapp.RequestHandler):

    def post(self):
        link = Link()
        if users.get_current_user():
            link.user = users.get_current_user()

        link.url = self.request.get('url')
        link.put()
        self.redirect('/')

class MainPage(webapp.RequestHandler):

    def get(self):
        links_query = Link.all().order('-date')
        last_100_links = links_query.fetch(100)
        user = users.get_current_user()
        if user:
            template_values = { 'user': user.nickname(),
                                'last_100_links': last_100_links,
                                'logout_url': users.create_logout_url('/') }
            path = os.path.join(os.path.dirname(__file__), 'index.html')
            self.response.out.write(template.render(path, template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication(
    [('/', MainPage),
     ('/new_link', Links)],
     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

        
