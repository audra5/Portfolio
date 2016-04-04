
import webapp2
import os
import logging
import jinja2
from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.path
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class Page1Handler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render())

class Page2Handler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
        self.response.write(template.render())

class Page3Handler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/faq.html')
        self.response.write(template.render())

class Page4Handler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({"msg": "Sign-up for e-mail updates"}))
    def post(self):

        email1 = self.request.get("email1")
        email2 = self.request.get("email2")

        if email1 == email2:
            template = JINJA_ENVIRONMENT.get_template('templates/success.html')
            self.response.write(template.render())

            message = mail.EmailMessage(sender="achr@umich.edu",
                                subject="Audranda")

            message.to = email1
            message.body = """
            Hello! 

            Thank you for signing up with Audranda! Please, enjoy this goofy picture of Audra and Amanda face-swapping. 


            Yours truly,
            Audranda

            """

            message.send()
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
            self.response.write(template.render({"msg": "Your e-mail addresses did not match - try again"}))

           


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/about.html', Page1Handler),
    ('/gallery.html', Page2Handler),
    ('/faq.html', Page3Handler),
    ('/contact.html', Page4Handler)
], debug=True)
