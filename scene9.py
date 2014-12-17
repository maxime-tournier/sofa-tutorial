import toolbox


def createScene( node ):
    """refactoring"""
    
    toolbox.setup( node )

    # objects
    obj1 = toolbox.rigid(node,
                         name = 'object1',
                         mesh = 'mesh/torus.obj')

    obj1.createObject('FixedConstraint',
                      indices = '0')

    # we wrap the local frame creation in this helper function, see
    # toolbox.py for details
    frame1 = toolbox.local_frame(obj1,
                                 coords = [3, 0, 0,
                                           0, 0, 0, 1])
    # access an object under a node given its name
    dofs = frame1.getObject('dofs')
    dofs.showObject = True
    dofs.showObjectScale = 1

    obj2 = toolbox.rigid(node,
                         name = 'object2',
                         position = [6, 0, 0,
                                     0, 0, 0, 1],
                         mesh = 'mesh/torus.obj')

    frame2 = toolbox.local_frame(obj2,
                                 coords = [-3, 0, 0,
                                           0, 0, 0, 1] )
    dofs = frame2.getObject('dofs')
    dofs.showObject = True
    dofs.showObjectScale = 1

    return 0


