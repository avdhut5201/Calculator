import unittest
from unittest import result 
from Source import Calculator


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator.Calculator()
    def test_add_method(self):
        result = self.calculator.addition(4, 2)
        self.assertEqual(6, result)
    def test_subtract_method(self):
        result = self.calculator.subtract(4, 2)
        self.assertEqual(2, result)
    def test_multiplication_method(self):
        result = self.calculator.multiplication(4, 2)
        self.assertEqual(8, result)
    def test_divide_method(self):
        result = self.calculator.divide(4, 2)
        self.assertEqual(2, result)
    def test_divide_method_when_second_arguement_is_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = self.calculator.divide(4, 0)
    def test_expression(self):
        inputexpr="1+2"
        result=self.calculator.get_Calculator(inputexpr)
        self.assertEquals(inputexpr,result["expression"])
        self.assertTrue(result["is_infix"])
    
    def test_should_return_false_when_there_is_single_digit(self):
         equation= self.calculator.get_Calculator("2")
         result=self.calculator.is_valid_infix(equation)
         self.assertFalse(result)
    
    def test_given_equation_should_return_falsewhen_unknown_operator_occurs(self):
        inputexpr="2 + 2 - 2 * 4 / 5 ^ 1 % 5"
        equation=self.calculator.get_Calculator(inputexpr)
        result=self.calculator.is_valid_infix(equation)
        self.assertFalse(result)
    
    def test_given_equation_should_return_falsewhen_triple_digiit_occurs(self):
        inputexpr="222"
        equation=self.calculator.get_Calculator(inputexpr)
        result=self.calculator.is_valid_infix(equation)
        self.assertFalse(result)
    

    def test_given_equation_should_return_falsewhen_more_than_triple_digiit_occurs(self):
        inputexpr="2222"
        equation=self.calculator.get_Calculator(inputexpr)
        result=self.calculator.is_valid_infix(equation)
        self.assertFalse(result)
    
    
    def test_given_equation_should_return_falsewhen_partial_infix_occurs(self): # New Test 
        inputexpr="222 -"
        equation=self.calculator.get_Calculator(inputexpr)
        result=self.calculator.is_valid_infix(equation)
    


    def test_given_equation_isinfix(self):
        inputexpr="223 + 21 - 432 * 40 / 5 ^ 1"
        equation=self.calculator.get_Calculator(inputexpr)
        result=self.calculator.is_valid_infix(equation)
        self.assertTrue(result)
    
    def test_Postfix_Evaluation(self):
        equation= "2 3 4 * 5 / +"
        expression=self.calculator.get_Calculator(equation)
        result=self.calculator.evaluation(expression)
        self.assertEquals(4.4,result)


    
    


        
    

        



    
    

    
    

    
    


    

if __name__ == '__main__':
    unittest.main()
