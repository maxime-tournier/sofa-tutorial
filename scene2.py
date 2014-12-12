

def createScene( node ):
    """a scene with a single node, with rigid dofs and uniform mass"""
    
    obj = node.createChild('object')


    # note the template argument: it could be Vec3d, Vec3f, Rigid3f,
    # Rigid2d, ...
    dofs = obj.createObject('MechanicalObject',
                            name = 'dofs',
                            template = 'Rigid3d')

    # initial conditions:
    
    # position/orientation (as a quaternion x y z w)
    dofs.position = [0, 0, 0,
                     0, 0, 0, 1]

    # linear/angular velocity
    dofs.velocity = [0, 1, 0,
                     0, 0, 0]

    # note the use of 'template', it should match that of the
    # dofs. you might omit it sometimes though.
    mass = obj.createObject('UniformMass',
                            template = 'Rigid3d',
                            totalMass = 1)

    
    return 0


