import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from model.Link import Link


class Links(webapp.RequestHandler):
	""" Class Links """

	def post(self):
		link = Link()
		if users.get_current_user():
			link.user = users.get_current_user()
			link.url = self.request.get('url')
			link.tags = []
			link.notes = self.request.get('notes')
			link.is_privat = True if self.request.get('is_privat') else False
			link.put()
			self.redirect('/')


class MainPage(webapp.RequestHandler):
	""" Class MainPage """

	def get(self):
		user = users.get_current_user()
		links_query = Link.all().order('-date')
		if user:
			links_query.filter("user =", user)
			last_100_links = links_query.fetch(100)
			template_values = { 'user': user.nickname(),
								'last_100_links': last_100_links,
								'logout_url': users.create_logout_url('/') }
			path = os.path.join(os.path.dirname(__file__), 'index.html')
			self.response.out.write(template.render(path, template_values))
		else:
			self.redirect(users.create_login_url(self.request.uri))


application = webapp.WSGIApplication(
	[('/', MainPage), ('/new_link', Links)],
	 debug=True
)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()


