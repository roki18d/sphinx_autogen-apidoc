#!/usr/bin/env python
# coding: utf-8

from my_module.exceptions import InvalidArgumentsError

class SimpleCalculator(object): 
    """SimpleCalculator

    SimpleCalculator is a simple calculator.  

    Attributes: 
        operator (str): 
            String that represents operation type. 
            Acceptable values are: {"add": addition, "sub": subtraction
            "mul": multiplication, "div": divide}
        response (dict): 
            Response for API execution. 
            This contains conditions (such as operands) and execution results. 
    """
    
    def __init__(self, operator: str) -> None:
        """Initialize instance
        Args: 
            operator (str): 
        """
        valid_operators = ["add", "sub", "mul", "div"]
        if operator not in valid_operators:
            msg = f"Invalid operator '{operator}' was given, choose from {valid_operators}."
            raise InvalidArgumentsError(msg)
        else: 
            self.operator = operator

        self.response = dict()


    def __add(self, num1: int, num2: int) -> None:
        self.response['results'] = {"sum": num1 + num2}
        return None

    def __sub(self, num1: int, num2: int) -> None:
        self.response['results'] = {"difference": num1 - num2}
        return None
    
    def __mul(self, num1: int, num2: int) -> None:
        self.response['results'] = {"product": num1 * num2}
        return None
    
    def __div(self, num1: int, num2: int) -> None:
        self.response['results'] = {"quotient": num1//num2, "remainder": num1%num2}
        return None

    def __handle_exceptions(self, e) -> None:
        self.response['results'] = {"error_message": e}
        return None

    def execute(self, num1: int, num2: int):
        """
        Interface to execute caluculation. 

        Args: 
            num1 (int): 1st operand. 
            num2 (int): 2nd operand. 

        Returns: 
            dict: self.response

        Raises: 
            InvalidArgumentsError: 

        Examples:
            >>> my_adder = SimpleCalculator(operator="add")
            >>> my_adder.execute(4, 2)
            {'operands': {'num1': 4, 'num2': 2}, 'results': {'sum': 6}}
        """

        try: 
            operands = {"num1": num1, "num2": num2}
            self.response['operands'] = operands
            if (not isinstance(num1, int)) or (not isinstance(num2, int)):
                msg = f"All operands should be integer, given: {operands}."
                raise InvalidArgumentsError(msg)
        except Exception as e: 
            _ = self.__handle_exceptions(e)

        try:
            if self.operator == "add":
                _ = self.__add(num1, num2)
            elif self.operator == "sub":
                _ = self.__sub(num1, num2)
            elif self.operator == "mul":
                _ = self.__mul(num1, num2)
            elif self.operator == "div":
                _ = self.__div(num1, num2)
        except Exception as e:
            _ = self.__handle_exceptions(e)
        
        return self.response


if __name__ == "__main__":

    my_adder = SimpleCalculator(operator="add")
    print('Case01:', my_adder.execute(4, 2))
    print('Case02:', my_adder.execute(5, "a"))

    my_subtractor = SimpleCalculator(operator="sub")
    print('Case03:', my_subtractor.execute(3, 5))

    my_multiplier = SimpleCalculator(operator="mul")
    print('Case04:', my_multiplier.execute(2, 7))

    my_divider = SimpleCalculator(operator="div")
    print('Case05:', my_divider.execute(17, 5))
    print('Case06:', my_divider.execute(6, 0))
    
    print('Case07:')
    my_unknown = SimpleCalculator(operator="unknown")

    import sys; sys.exit(0)
