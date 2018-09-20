#Inputs the length of a base, the width of an object, and the desired spacing between objects.
#Outputs the distances of each object from the edge of the base.



#User Explaination:-----------------------------
print("\n                               v-----Spacing")
print(" _________________...______|______|_____ ")
print("|    O        O           O        O    |")
print("|_________________...___________________|")
print("|    |                   | |")
print("  ^---Spacing             ^---Width of Object\n")
print("Length of Base:   Length of work piece you are attaching objects to or drilling holes in\n")
print("Width of Object:  Width of object you are attaching to the work piece or the diameter of hole you are drilling\n")
print("Spacing:          Desired spacing between the centers of objects or holes (Note: the spacing between the ")
print("                  edge and first + last object will be <= spacing.)\n")


#Inputs:----------------------------------------
base_length =  float(input("Length of Base:  "))
object_width = float(input("Width of Object: "))
min_spacing =  float(input("Spacing: "))


#Calculations:----------------------------------
unit_length = min_spacing + object_width
adj_length = base_length - min_spacing
num_objects = int(adj_length / unit_length)
end_spacing = round((base_length - ((num_objects - 1) * min_spacing) - (num_objects * object_width)) / 2 , 3)

first_center = (object_width / 2) + (end_spacing)
center_distance = object_width + min_spacing

#Outputs:---------------------------------------
print("\n===============================================")
print("Number of objects: ", num_objects)
print("End spacing:       ", end_spacing)

print("\n\nCenters:----     Edges:----")
for i in range(num_objects):
   print(first_center + (i * center_distance), "\t\t", end_spacing + (i * center_distance))
   
