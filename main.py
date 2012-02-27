from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from controller.Links import Links
from model.Link import Link
from view.MainPage import MainPage
from view.About import About


application = webapp.WSGIApplication(
	[
		('/', MainPage),
		('/new_link', Links),
		('/about', About)
	],
	 debug=True
)


def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()


