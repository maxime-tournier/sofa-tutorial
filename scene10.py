import toolbox


def createScene( node ):
    """joint dofs in exponential coordinates"""
    
    toolbox.setup( node )

    # objects
    obj1 = toolbox.rigid(node,
                         name = 'object1',
                         mesh = 'mesh/torus.obj')

    obj1.createObject('FixedConstraint',
                      indices = '0')

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

    mapping = joint.createObject('RigidJointMultiMapping',
                                 name = 'mapping',
                                 template = 'Rigid,Vec6',
                                 input = '@../object1/frame/dofs @../object2/frame/dofs',
                                 output = '@dofs',
                                 pairs = '0 0')

    stiffness = 1e3
    
    ff = joint.createObject('UniformCompliance',
                            compliance = 1.0 / stiffness)


    
    return 0


