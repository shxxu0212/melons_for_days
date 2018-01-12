"""Classes for melon orders."""
from random import randint
import time
import datetime

class AbstractMelonOrder(object):
    # qualities that are different for each melon order go in an init
    def __init__(self, species, qty):  # ,country_code
        self.species = species
        self.qty = qty
        self.shipped = False
        # if country_code:
        #     self.country_code = country_code

    def get_base_price(self):
        """ generates random base price for splurge pricing"""
        base_price = randint(5, 10)

        current_time = datetime.datetime.now()
        if 8 <= current_time.hour <= 11 and 1 <= current_time.isoweekday() <= 5:
            base_price += 4

    def get_total(self):
        """Calculate price, including tax."""

        base_price = get_base_price()  # splurge pricing option
        if self.species.lower() == "christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # qualities that are the same for all domestic melon orders go here
    order_type = "domestic"
    tax = 0.08

    # def __init__(self, order_):
      #  return super(DomesticMelonOrder, self).__init__(species,quantity,"domestic")


class GovernmentOrder(DomesticMelonOrder):
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    # qualities that are the same for all international melon orders go here
    tax = 0.17
    order_type = "international" 

    def __init__(self, species, qty, country_code):
        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty)

    def get_total(self):
        start_total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
           start_total += 3
        return start_total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

# class TooManyMelonsError(ValueError):
#     """ raise error if too many melons declared """
#     def __init__(self, qty):
#         self.qty = qty
#     if self.qty > 100:
#         raise