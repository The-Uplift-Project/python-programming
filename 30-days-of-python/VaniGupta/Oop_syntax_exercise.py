### TODO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects), pants that the salesperson has sold 
#   - total_sales (float), sum of sales of pants sold

class SalesPerson():
    
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.

    total_sales = 0.0
    pants_sold = []

    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary

### TODO: write a sell_pants method:
#    This method receives a Pants object and appends the object to the pants_sold attribute list
#    Args: pants (Pants object): a pants object / Returns: None

    def sell_pants(self, Obj):
        self.pants_sold.append(Obj)

### TODO: write a display_sales method:
#    This method has no input or outputs. When this method is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants line by line. 

    def display_sales(self):
        for i in range(len(self.pants_sold)):
            print("color: {}, waist_size: {}, length: {}, price: {}".format(self.pants_sold[i].color, self.pants_sold[i].waist_size,\
                                                                           self.pants_sold[i].length, self.pants_sold[i].price))

### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total. 
#      Args: None / Returns: float: total sales

    def calculate_sales(self):
        for i in range(len(self.pants_sold)):
            self.total_sales += self.pants_sold[i].price
        return self.total_sales

### TODO: write a calculate_commission method:
#   The salesperson receives a commission based on the total sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price, and then returns the commission as (percentage * total sales)
#   Args: percentage (float): comission percentage as a decimal / Returns: float: total commission

    def calculate_commission(self,val):
        return val*self.total_sales
