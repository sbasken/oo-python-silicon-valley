from .funding_round import FundingRound

class Startup:

   all = []
   domains = []

   def __init__(self, name, founder, domain):
      if type(name) == str:
         self.name = name
      self.founder = founder
      self.domain = domain
      Startup.all.append(self)

   @property
   def founder(self):
      return self._founder
   
   @founder.setter
   def founder(self, founder):
      if not hasattr(self, "_founder"):
         if type(founder) == str:
            self._founder = founder
      else:
         print("You cannot change the founder's name!")

   @property
   def domain(self):
      return self._domain

   @domain.setter
   def domain(self, domain):
      if not hasattr(self, "_domain"):
         if type(domain) == str:
            self._domain = domain 
            Startup.domains.append(domain)
      else:
         print("You cannot change the domain!")

   def pivot(self, domain, name):
      if type(domain) == str and type(name) == str:
         self._domain = domain
         self._name = name

   @classmethod
   def find_by_founder(cls, founder):
      return [ comp for comp in Startup.all if comp.founder == founder][0]



