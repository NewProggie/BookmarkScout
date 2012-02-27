import os

from google.appengine.ext.webapp import template


# This looks really dirty and I don't mean it in an erotic way.
# Maybe there is a better way to do this.
class NAV:
	NONE = -1
	HOME = 0
	ABOUT = 1
	CONTACT = 2


def render_basic_includes( tmplt_vals_start = None, tmplt_vals_nav = None, tmplt_vals_end = None ):
	"""
	Renders the template parts that are (probably) needed
	in every template, like the start and end part of an HTML
	document or the navigation.

	tmplt_vals_start -- Argument to pass to the template renderer for start.html.
	tmplt_vals_nav -- Argument to pass to the template renderer for nav.html.
	tmplt_vals_end -- Argument to pass to the template renderer for end.html.
	"""

	# If missing, set default "active" value for tmplt_vals_nav
	if tmplt_vals_nav is None:
		tmplt_vals_nav = { 'active': NAV.NONE }
	elif 'active' not in tmplt_vals_nav:
		tmplt_vals_nav['active'] = NAV.NONE

	# The elements for the navigation
	nav_links = [
		{ 'url': '/', 'name': 'Home', 'class': '' },
		{ 'url': '/about', 'name': 'About', 'class': '' },
		{ 'url': '/contact', 'name': 'Contact', 'class': '' }
	]

	# Give "active" class to the chosen one
	for i in range( len( nav_links ) ):
		if i == tmplt_vals_nav['active']:
			nav_links[i]['class'] = ' class="active"'

	tmplt_vals_nav['nav_links'] = nav_links

	# Paths to the template parts
	path_template = os.path.join( os.path.dirname( __file__ ), 'template' )
	path_start = os.path.join( path_template, 'start.html' )
	path_nav = os.path.join( path_template, 'nav.html' )
	path_end = os.path.join( path_template, 'end.html' )

	# Render the template parts (still no web output!)
	tmplt_include = {
		'start': template.render( path_start, tmplt_vals_start ),
		'nav': template.render( path_nav , tmplt_vals_nav ),
		'end': template.render( path_end, tmplt_vals_end )
	}

	return tmplt_include


def get_template_path():
	""" Returns the path to the template directory. """
	return os.path.join( os.path.dirname( __file__ ), 'template' )



__all__ = ['About', 'MainPage']