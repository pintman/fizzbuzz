import os
import bottle

# change working directory
os.chdir(os.path.dirname(__file__))

# create the app
application = bottle.Bottle()

@application.route("/<number:int>")
def fizzbuzz_web_route(number):    
    results = []
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            results.append("fizzbuzz")
        elif i % 3 == 0:
            results.append("fizz")
        elif i % 5 == 0:
            results.append("buzz")
        else:
            results.append(i)

    html = """
        <!DOCTYPE html>
        <html>
          <body>
            <h1>FizzBuzz Numbers up to {{max}}</h1>
            <table>
            % for r in results:
              <tr><td> {{r}} </td></tr>
            %end
            </table>
          </body>
        </html>
        """

    return bottle.template(html, max=number, results=results)
