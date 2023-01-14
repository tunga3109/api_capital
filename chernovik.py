#from accessify import private, protected

#class Point:
#
#    LENGTH = 12
#    WIDTH = 15
#
#    @classmethod #обращается к атрибутам класса
#    def check(cls, num):
#        return cls.LENGTH <= num <= cls.WIDTH
#
#    def __init__(self, x, y):
#        self.x = self.y = 0
#        if self.check(x) and self.check(y):
#            self.x = x
#            self.y = y

    

    #def get_nums(self):
    #    return self.x, self.y
    #
    #@staticmethod #создание независимой ф-ции внутри класса
    #def norm2(x, y):
    #    return x**2 + y**2

    #def __getattribute__(self, item):
    #    print('_getattribute__')
    #    return object.__getattribute__(self, item)
    
#    def plus(self, dig):
#        return self.LENGTH + dig

#a = Point(13,14)
##print(a.get_nums())
##print(Point.norm2(3,4))
#print(a.plus(5))
#a = lambda b: [b ** i for i in range(3)]
#print(type(a(3)))
#
#def hello(*args):
#    print(*args)
#
#hello({'a':'b', 'c':'d'})
#
#def print_kwargs(**kwargs):
#    print(kwargs)
#
#print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
#
#a = dict(a=3, b=5, c='hello')
#print(a)

#while True:
#    try:
#        num = int(input('num: '))
#        a  = 5/num
#        print(a)
#    except ZeroDivisionError:
#        print('nelzya delit na 0')
#    except TypeError:
#        print('vvedite chislo')
#    finally:
#        print('end')
#    if num == 000:
#        break

#print("start")
#try:
#   val = int(input("input number: "))
#   tmp = 10 / val
#   print(tmp)
#except ValueError as ve:
#   print("ValueError! {0}".format(ve))
#except ZeroDivisionError as zde:
#   print("ZeroDivisionError! {0}".format(zde))
#except Exception as ex:
#   print("Error! {0}".format(ex))
#print("stop")

#try:
#   raise Exception("Some exception")
#except Exception as e:
#   print("Exception exception " + str(e))

#class NegValException(Exception):
#   pass
#
#try:
#   val = int(input("input positive number: "))
#   if val < 0:
#       raise NegValException("Neg val: " + str(val))
#   print(val + 10)
#except NegValException as e:
#  print(e)

#import requests
#from config import *
#from auth_login_pass import URL
#
#class API:
#
#    def start(self):
#        print('start session')
#
#
#
#a = API()
#a.start()

#def decorator_1(func):
#    def start(*args, **kwargs):
#        print('Function is started....')
#        a = func(*args, **kwargs)
#        print('function is finished....')
#        return a
#
#    return start
#
#@decorator_1
#def hello(name):
#    print(f'hello {name}')
#
#hello('anton')

# import requests
# from config import *
# import json

# BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
# BASE_LIVE_URL = 'https://api-capital.backend-capital.com'

# session = requests.Session() # Create session

# '''Returns the user's session details and optionally tokens.'''

# response = session.post(
#     BASE_DEMO_URL + '/api/v1/session',
#     json={"encryptedPassword": False, 'identifier': login, 'password': password},
#     headers={'X-CAP-API-KEY': API_KEY}
# )

# CST = response.headers['CST']
# X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

# def prices():
#     epic_name = input('Paste the epic name: ')
#     response = session.get(
#         BASE_DEMO_URL + f'/api/v1/prices/{epic_name}?resolution=MINUTE&max=10&from=2022-09-24T00:00:00&to=2022-09-24T05:00:00',
#         headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
#     )

#     data = json.dumps(response.json(), sort_keys=True, indent=4)
#     print(data)

# prices()



        


        
        
        

