from google.appengine.ext import db


class Link( db.Model ):
	""" Link model """

	user = db.UserProperty()
	_url = db.StringProperty()
	notes = db.StringProperty( multiline = True )
	is_privat = db.BooleanProperty()
	date = db.DateTimeProperty( auto_now_add = True )

	def get_url( self ):
		return self._url

	def set_url( self, value ):
		# If no protocol given, assume HTTP
		if not "://" in value:
			value = "http://" + value
		self._url = value

	def del_url( self ):
		del self._url

	url = property( get_url, set_url, del_url )
