import toolbox


def createScene( node ):
    """rigid joint dofs in exponential coordinates"""
    
    toolbox.setup( node )

    # objects
    obj1 = toolbox.rigid(node,
                         name = 'object1',
                         mesh = 'mesh/torus.obj')

    # fix the first object
    obj1.createObject('FixedConstraint', indices = '0')

    frame1 = toolbox.local_frame(obj1,
                                 name = 'frame',
                                 coords = [3, 0, 0,
                                           0, 0, 0, 1])
    dofs = frame1.getObject('dofs')
    dofs.showObject = True
    dofs.showObjectScale = 1
    

    obj2 = toolbox.rigid(node,
                         name = 'object2',
                         position = [6, 0, 0,
                                     0, 0, 0, 1],
                         mesh = 'mesh/torus.obj')

    frame2 = toolbox.local_frame(obj2,
                                 name = 'frame',
                                 coords = [-3, 0, 0,
                                           0, 0, 0, 1] )
    dofs = frame2.getObject('dofs')
    dofs.showObject = True
    dofs.showObjectScale = 1

    joint = node.createChild('joint')
    dofs = joint.createObject('MechanicalObject',
                              name = 'dofs',
                              template = 'Vec6')

    # maps rigid dofs (a, b) -> log(inv(a) * b)
    mapping = joint.createObject('RigidJointMultiMapping',
                                 name = 'mapping',
                                 template = 'Rigid,Vec6',
                                 input = '@../object1/frame/dofs @../object2/frame/dofs',
                                 output = '@dofs',
                                 pairs = '0 0')

    # note: multimappings map from several input mechanical objects,
    # whereas mappings map from a single mechanical object
    
    stiffness = 1e3

    # a compliance is the inverse of a stiffness. think of it as a
    # spring that will drive the underlying dof to its zero value
    # (here the exponential coordinates of the rigid joint). a zero
    # compliance corresponds to an infinitely stiff spring, i.e. a
    # holonomic constraint.
    ff = joint.createObject('UniformCompliance',
                            compliance = 1.0 / stiffness)

    
    return 0


