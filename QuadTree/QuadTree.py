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
      self.items = []
      self.divided = False

   def query(self, search_box):
      found = []
      if not self.boundary.intersects(search_box): 
         return []
      else: 
         for item in self.items:
            if search_box.contains_pt([item.x, item.y]):
               found.append(item)

         if self.divided:
            found.extend(self.northwest.query(search_box))
            found.extend(self.northeast.query(search_box))
            found.extend(self.southwest.query(search_box))
            found.extend(self.southeast.query(search_box))

      return found

   def insert(self, item):
      #Is item inside boundary of quadtree?
      if not (self.boundary.contains_pt([item.x, item.y])): return

      #Is quadtree full?
      if len(self.items) < self.capacity:
         self.items.append(item)
      else:
         if not self.divided:
            self.subdivide()

         #Attempt to insert item into each of the new quadrents
         self.northwest.insert(item)
         self.northeast.insert(item)
         self.southwest.insert(item)
         self.southeast.insert(item)

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
