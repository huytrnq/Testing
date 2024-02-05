
class Employee:
    """Employee class
    """
    # Annual raise amount 
    raise_amt = 1.05
    
    def __init__(self, first, last, pay) -> None:
        """__init__ method

        Args:
            first (str): first name
            last (str): last name
            pay (str): pay amount
        """
        self.first = first
        self.last = last
        self.pay = pay
        
    ### email is a property just like first and last. 
    # This means you can access it like an attribute without parentheses 
    # The benefit of using a property is that you can calculate the value dynamically when first and last change
    @property
    def email(self):
        """Get email address

        Returns:
            str: email address
        """
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        """Get full name

        Returns:
            str: full name
        """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Apply raise
        """
        self.pay = int(self.pay * self.raise_amt)