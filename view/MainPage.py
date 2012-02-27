import os

from . import render_basic_includes, get_template_path, NAV
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from model.Link import Link


class MainPage(webapp.RequestHandler):
	""" Class MainPage """

	def get(self):
		user = users.get_current_user()
		links_query = Link.all().order('-date')

		if user:
			links_query.filter('user =', user)
			last_100_links = links_query.fetch(100)

			path_index = os.path.join( get_template_path(), 'index.html' )
			tmplt_vals = {
				'include': render_basic_includes(
					tmplt_vals_nav = { 'active': NAV.HOME }
				),
				'user': user.nickname(),
				'last_100_links': last_100_links,
				'logout_url': users.create_logout_url('/')
			}
			rendered_index = template.render( path_index, tmplt_vals )
			self.response.out.write( rendered_index )
		else:
			self.redirect(users.create_login_url(self.request.uri))
