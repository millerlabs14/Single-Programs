import tkinter as tk
import random
import time

class Window:
   def __init__(self):
      self.root = tk.Tk()
      self.root.title("QuadTree")
      self.root.geometry("510x510")

      #Create Canvas
      self.screen = tk.Canvas(self.root, height = 500, width = 500, background = "grey",
                              highlightthickness = 3, highlightbackground = "#525252")
      self.screen.pack()
      self.root.update()

class Point:
   def __init__(self,screen, x, y):
      self.x = x
      self.y = y
      self.ID = screen.create_oval(x-2, y-2, x+2, y+2, fill = "white")

class Boundary:
   def __init__(self,x,y,center_distance):
      self.x = x
      self.y = y
      self.cd = center_distance
      self.top    = y - center_distance
      self.bottom = y + center_distance
      self.left   = x - center_distance
      self.right  = x + center_distance

   def contains_pt(self, point):
      #point format: [x,y]
      return (point[0] >= self.left  and point[0] < self.right and
              point[1] >= self.top   and point[1] < self.bottom)

   def intersects(self, box):
      if (box.left   > self.right  or
          box.right  < self.left   or
          box.top    > self.bottom or
          box.bottom < self.top):
         return False
      else:
         return True

class QuadTree:
   def __init__(self, boundary):
      self.boundary = boundary
      self.capacity = 5
      self.points = []
      self.divided = False

   def query(self, search_box):
      found = []
      if not self.boundary.intersects(search_box): 
         return []
      else: 
         for point in self.points:
            if search_box.contains_pt([point.x, point.y]):
               found.append(point)

         if self.divided:
            found.extend(self.northwest.query(search_box))
            found.extend(self.northeast.query(search_box))
            found.extend(self.southwest.query(search_box))
            found.extend(self.southeast.query(search_box))

      return found

   def insert(self, point):
      #Is point inside boundary of quadtree?
      if not (self.boundary.contains_pt([point.x, point.y])): return

      #Is quadtree full?
      if len(self.points) < self.capacity:
         self.points.append(point)
      else:
         if not self.divided:
            self.subdivide()

         #Attempt to insert point into each of the new quadrents
         self.northwest.insert(point)
         self.northeast.insert(point)
         self.southwest.insert(point)
         self.southeast.insert(point)

   def subdivide(self):
      x = self.boundary.x
      y = self.boundary.y
      cd = self.boundary.cd

      nw = Boundary((x - cd/2), (y - cd/2), (cd/2))
      ne = Boundary((x + cd/2), (y - cd/2), (cd/2))
      sw = Boundary((x - cd/2), (y + cd/2), (cd/2))
      se = Boundary((x + cd/2), (y + cd/2), (cd/2))

      self.northwest = QuadTree(nw)
      self.northeast = QuadTree(ne)
      self.southwest = QuadTree(sw)
      self.southeast = QuadTree(se)

      self.divided = True

   def show(self, screen):
      screen.create_rectangle(self.boundary.left, self.boundary.top, self.boundary.right, self.boundary.bottom)

      if self.divided:
         self.northwest.show(screen)
         self.northeast.show(screen)
         self.southwest.show(screen)
         self.southeast.show(screen)




def update(event, search_box):
   search_box.x = event.x
   search_box.y = event.y
   search_box.top    = search_box.y - search_box.cd
   search_box.bottom = search_box.y + search_box.cd
   search_box.left   = search_box.x - search_box.cd
   search_box.right  = search_box.x + search_box.cd


window = Window()

qtree = QuadTree(Boundary(250,250,250))

points = []
for i in range(100):
   point = Point(window.screen, random.randint(0,window.screen.winfo_width()), random.randint(0,window.screen.winfo_height()))
   points.append(point)
   qtree.insert(point)
 
qtree.show(window.screen)
search = Boundary(100,100, 50)
box = window.screen.create_rectangle(search.left, search.top, search.right, search.bottom, outline = "green")

window.screen.bind('<Motion>', lambda event: update(event, search))

while True:
   t1 = time.time()
   close = qtree.query(search)
   t2 = time.time()

   for point in points:
      window.screen.itemconfig(point.ID, fill = "white")

   for point in close:
      window.screen.itemconfig(point.ID, fill = "blue")
      window.screen.coords(box, search.left, search.top, search.right, search.bottom)


   window.root.update()

# time.sleep(5)
# window.root.destroy()