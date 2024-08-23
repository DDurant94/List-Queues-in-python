#Stack First in First Out FIFO

class Kitchen:
  def __init__ (self):
    self.orders = []
    
  def enqueue(self,order):
    self.orders.append(order)
    print(f"\nOrder# {self.amount_of_orders()+1} has been placed! Order contents: {order}\n")
  
  def dequeue(self):
    if not self.is_empty():
      print('\nOrder up\n', self.orders[0])
      self.orders.pop(0)
      
  
  def view_orders(self):
    print("\nOrders In Kitchen:")
    for count,order in enumerate(self.orders):
      print(f"{count + 1}. {order}")
      print('<------------------------------------>')
  
  def amount_of_orders(self):
    return len(self.orders)
    
  def is_empty(self):
    return len(self.orders) == 0
  

order_manager = Kitchen()
drinks = ['water', 'tea', 'lemonade', 'coke', 'pepsi','no drink']
meals = [{'hamburger':{"prep time": 10}},{'steak':{"prep time": 15}}, {'chicken strips':{"prep time": 8}},{'Taco':{"prep time": 5}},{'No meal':{"prep time": 0}}]
priorities = ['Low', 'Medium', 'High', 'Emergency']  

def add_order():
  order = {'Drink':[], "Meal":[],'Priority':{}}
  order_number = order_manager.amount_of_orders()+1
  print(f"Starting New Order: Order #{order_number}")
  while True:
    add_order_choice = input(f"Add to Order #{order_number} [Y]es, [C]omplete Order, [E]xit \n").upper()
    if add_order_choice == "Y":
      try:
        for count,drink in enumerate(drinks):
          print(f"[{count+1}]: {drink}")
        drink_choice = int(input("\nEnter Drink Number: "))
        order['Drink'].append(drinks[drink_choice -1])
        for count2, meal  in enumerate(meals):
          print(f"[{count2+1}]: {meal}")
        meal_choice = int(input("\nEnter Meal Number: "))
        order['Meal'].append(meals[meal_choice -1])
      except ValueError as e:
        print("Invalid Input")
    
    elif add_order_choice == "C":
      for count3,priority in enumerate(priorities):
        print(f"[{count3+1}]: {priority}")
      priority_choice = int(input("\nEnter Priority Number: "))
      order['Priority'] = priorities[priority_choice -1]
      order_manager.enqueue(order)
      print("Returning to main menu...")
      break
    
    elif add_order_choice == "E":
      print("Returning to main menu...")
      break
    else:
      print("Invalid Choice") 

def app():
  print("Welcome to Order Management System")
  while True:
    user_choice = input("\nChoose Menu Option:\n[A]dd order, [R]emove Order, [V]eiw All Orders, [O]rder Count, [E]nd \n").upper()
    if user_choice == "A":
      add_order()
    elif user_choice == "R":
      order_manager.dequeue()
    elif user_choice == "V":
      order_manager.view_orders()
    elif user_choice == "O":
      print(f"Current Order Count in Kitchen is {order_manager.amount_of_orders()}")
    elif user_choice == "E":
      print("Thank you for using Order Management System")
      break
    else:
      print("Invalid Input")
      
      
app()