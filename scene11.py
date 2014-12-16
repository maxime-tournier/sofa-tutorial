import toolbox


def createScene( node ):
    """constraints"""
    
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

    joint = toolbox.joint_dofs(node,
                               'object1/frame/dofs',
                               'object2/frame/dofs',
                               name = 'joint')
    
    constraints = joint.createChild('constraints')
    dofs = constraints.createObject('MechanicalObject',
                                    name = 'dofs',
                                    template = 'Vec1')

    mapping = constraints.createObject('MaskMapping',
                                       dofs = '1 1 1 0 0 0')
    
    ff = constraints.createObject('UniformCompliance',
                                  compliance = 0)

    
    return 0


