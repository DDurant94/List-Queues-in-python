#Queue First in Last Out FILO


class BrowserHistory:
  def __init__ (self):
    self.history = []
    
  def push(self,webpage):
    self.history.append(webpage)
    print(f"{webpage} added to history")
  
  def pop(self):
    if not self.is_empty():
      return self.history.pop()
    
    
  def peek(self):
    if not self.is_empty():
      return self.history[-1]
    
    
  def is_empty(self):
    return len(self.history) == 0
  
  def page_count(self):
    return len(self.history)
  
webpage = BrowserHistory()  
def app():
  print("Web Browser History")
  while True:
    user_choice = input("\nChoose Option: [A]dd page, [R]emove Last Page, [N]umber of Visited Pages, [L]ast Visited, [E]nd ").upper()
    if user_choice == "A":
      website=input("\nEnter Webpage: ")
      webpage.push(website)
    elif user_choice == "R":
      webpage.pop()
    elif user_choice == "N":
      if webpage.is_empty():
        print("Browser History is Empty")
      else:
        num_pages_visited = webpage.page_count()
        print(f"You have visited {num_pages_visited} pages")
    elif user_choice == "L":
      last_page = webpage.peek()
      
    elif user_choice == "E":
      print("Leaving Browser History...")
    else:
      print("Invalid Choice")
      
app()