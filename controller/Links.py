from google.appengine.api import users
from google.appengine.ext import webapp

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
