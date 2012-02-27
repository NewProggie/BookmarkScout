import os

from . import render_basic_includes, get_template_path, NAV
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class About(webapp.RequestHandler):
	""" Class About """

	def get(self):
		user = users.get_current_user()

		if user:
			path_about = os.path.join( get_template_path(), 'about.html' )
			tmplt_vals = {
				'include': render_basic_includes(
					tmplt_vals_nav = { 'active': NAV.ABOUT }
				),
				'logout_url': users.create_logout_url('/')
			}
			rendered_about = template.render( path_about, tmplt_vals )
			self.response.out.write(  rendered_about )
		else:
			self.redirect(users.create_login_url(self.request.uri))
