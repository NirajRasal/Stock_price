from nsetools import Nse
nse = Nse()

q = nse.get_quote('infy')

#print(q)

hist = nse.history(period="5d")
print(hist)