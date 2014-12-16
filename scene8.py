import toolbox


def setup( node ):
    
    # load plugin
    plugin = node.createObject('RequiredPlugin',
                               pluginName = 'Compliant')

    plugin = node.createObject('RequiredPlugin',
                               pluginName = 'pouf')


    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior showCollision showMapping hideVisual'

    # these are from the Compliant plugin
    ode = node.createObject('CompliantImplicitSolver')
    num = node.createObject('SequentialSolver')

    node.dt = 1e-2
    node.animate = 1


def createScene( node ):
    """local frames example"""
    
    setup( node )

    # objects
    obj1 = toolbox.rigid(node,
                         name = 'object1',
                         mesh = 'mesh/torus.obj')

    obj1.createObject('FixedConstraint',
                      indices = '0')


    frame1 = obj1.createChild('frame1')
    
    dofs = frame1.createObject('MechanicalObject',
                               name = 'dofs',
                               template = 'Rigid')

    dofs.showObject = True
    dofs.showObjectScale = 1
    
    mapping = frame1.createObject('LocalFrameMapping',
                                  template = 'Rigid, Rigid')

    mapping.source = '0'
    mapping.coords = '3 0 0 0 0 0 1'

    obj2 = toolbox.rigid(node,
                         name = 'object2',
                         position = [6, 0, 0,
                                     0, 0, 0, 1],
                         mesh = 'mesh/torus.obj')

    frame2 = obj2.createChild('frame2')
    
    dofs = frame2.createObject('MechanicalObject',
                               name = 'dofs',
                               template = 'Rigid')

    dofs.showObject = True
    dofs.showObjectScale = 1
    
    mapping = frame2.createObject('LocalFrameMapping',
                                  template = 'Rigid, Rigid')

    mapping.source = '0'
    mapping.coords = '-3 0 0 0 0 0 1'

    return 0


