from google.appengine.api import users
from google.appengine.ext import webapp

from model.Link import Link
import random # just for debugging purpose

class Links(webapp.RequestHandler):
    """ Class Links """

    def get_tags(self, amount):
        """ Just for debugging purposes
        """
        tags = []
        for i in range(amount):
            tags.append(random.choice(['foo', 'bar', 'else', 'choice', 'what' ,'lolcats', 'ponies', 'cunts']))
        return tags
        
    def post(self):
        link = Link()
        if users.get_current_user():
            link.user = users.get_current_user()
            link.url = self.request.get('url')
            link.tags = self.get_tags(random.randint(1,7))
            link.notes = self.request.get('notes')
            link.is_privat = True if self.request.get('is_privat') else False
            link.put()
            self.redirect('/')
