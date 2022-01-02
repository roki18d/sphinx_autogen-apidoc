#!/usr/bin/env python
# coding: utf-8

class SimpleCalculator(object): 
    """SimpleCalculator

    SimpleCalculator is a simple calculator.  

    Attributes: 
        operator (str): 
            String that represents operation type. 
            Acceptable values are: {"add": addition, "sub": subtraction
            "mul": multiplication, "div": divide}
        response (dict): 
            Response for execution of API 'execute'. 
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
            raise Exception(msg)
        else: 
            self.operator = operator

        self.response = dict()


    def __add(self, num1, num2) -> None:
        self.response['results'] = {"sum": num1 + num2}
        return None

    def __sub(self, num1, num2):
        self.response['results'] = {"difference": num1 - num2}
        return None
    
    def __mul(self, num1, num2):
        self.response['results'] = {"product": num1 * num2}
        return None
    
    def __div(self, num1, num2):
        self.response['results'] = {"quotient": num1//num2, "remainder": num1%num2}
        return None


    def execute(self, num1: int, num2: int):
        """
        Interface to execute caluculation. 

        Args: 
            num1 (int): 1st operand. 
            num2 (int): 2nd operand. 

        Returns: 
            self.response (dict): 
        """

        operands = {"num1": num1, "num2": num2}
        if isinstance(num1, int) and isinstance(num2, int):
            self.response['operands'] = operands
        else: 
            msg = f"All operands should be integer, given: {operands}."
            raise Exception(msg)

        if self.operator == "add":
            _ = self.__add(num1, num2)
        elif self.operator == "sub":
            _ = self.__sub(num1, num2)
        elif self.operator == "mul":
            _ = self.__mul(num1, num2)
        elif self.operator == "div":
            _ = self.__div(num1, num2)
        
        return self.response


if __name__ == "__main__":

    my_adder = SimpleCalculator(operator="add")
    
    response = my_adder.execute(4, 2)
    print(response)

    import sys; sys.exit(0)
