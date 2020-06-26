# 12.1, # 15, Find an equation of the sphere that passes through a point and has a center C as input
def sphere_equation(point, center):
    ''' Point is an array of length n where n is the number of dimensions, only 3 in this case.
    Center is the center of a sphere. This function calculuates the distance between the point and center which is the radius,
    then creates the equation of the sphere that passes through the point in first input.'''
    
    distance = 0
    for i in range(len(point)):
        distance = distance + (point[i] - center[i])**2
    # radius = sqrt(distance)
    return (print("(x-",center[0],")^2"," +"," (y-",center[1],")^2"," +", " (z-",center[2],")^2" , " = ",distance, sep = ''))

# Example 1
point1 = [4,3,-1]
center1 = [3,8,1]

sphere_equation(point1, center1) # decent formatting, should get the job done

def dot_product(vector1, vector2):
    ''' where vectors are a list of length n, calculuates dot product between the 2'''
    dotsum = 0
    for i in range(len(vector1)):
        dotsum = dotsum + (vector1[i]*vector2[i])
    return dotsum

# example 1
vector1 = [1,3,-2]
vector2 = [5,1,-3]
dot_product(vector1, vector2)

def magnitude(vector):
    mag = 0
    for i in range(len(vector)):
        mag = mag + (vector[i]**2)
    mag = math.sqrt(mag)
    return mag

# example 1
magnitude(vector1)

vector3 = [8/9, -1/9, 4/9]
magnitude(vector3)

vector4 = [-5,3,-1]
magnitude(vector4)
