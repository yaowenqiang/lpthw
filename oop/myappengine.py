## building an AppEngine web application

from myappengine import webfunc, run_app


class MainPage(webfunc, RequestHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/plai"
        self.response.out.write("Welcome to the Greatest Website on the Web")


class  FAQPage(webfunc, RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = "text/plai"
        self.response.out.write("Here is the FAQ page ")


app = webfunc,WSGIApplication(
                                [('/', MainPage),
                                 ('/info', FAQPage),
                                ], 
                                debug=true)

def main():
    run_app(app)

main()
