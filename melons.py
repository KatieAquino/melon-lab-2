"""Classes for melon orders."""

class AbstractMelonOrder():
    shipped = False
    

    def __init__(self, species, qty, country_code='USA'):
        self.species = species
        self.qty = qty
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and < 10:
            total += 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False
    
    def mark_inspection(self):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = True