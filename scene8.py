import toolbox


def setup( node ):
    '''misc setup on root node'''
    
    # load plugin
    plugin = node.createObject('RequiredPlugin',
                               pluginName = 'Compliant')

    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior showCollision showMapping hideVisual'

    # these are from the Compliant plugin
    ode = node.createObject('CompliantImplicitSolver')
    num = node.createObject('SequentialSolver')

    node.dt = 1e-2
    node.animate = 0


def createScene( node ):
    """rigid-rigid mapping example"""
    
    setup( node )

    # objects
    obj1 = toolbox.rigid(node,
                         name = 'object1',
                         mesh = 'mesh/torus.obj',
                         position = '0 0 0  0 0 0 1')

    obj1.createObject('FixedConstraint',
                      indices = '0')


    frame1 = obj1.createChild('frame1')
    
    dofs = frame1.createObject('MechanicalObject',
                               name = 'dofs',
                               template = 'Rigid3d',
                               position = '0 0 0  0 0 0 1')

    # enable drawing of mapped dofs
    dofs.showObject = True
    dofs.showObjectScale = 1    # you can adjust scale with this one (big/small)
    
    mapping = frame1.createObject('AssembledRigidRigidMapping',
                                  template = 'Rigid,Rigid',
                                  input = '@../dofs',
                                  output = '@dofs')

    # input dof, translation, rotation: (i), (x y z), (x, y, z, w)
    mapping.source = '0  3 0 0   0 0 0 1'
    
    
    obj2 = toolbox.rigid(node,
                         name = 'object2',
                         position = [6, 0, 0,
                                     0, 0, 0, 1],
                         mesh = 'mesh/torus.obj')

    frame2 = obj2.createChild('frame2')
    
    dofs = frame2.createObject('MechanicalObject',
                               name = 'dofs',
                               template = 'Rigid')

    # drawing
    dofs.showObject = True
    dofs.showObjectScale = 1

    # the mapping name is not very informative, but we'll end up
    # wrapping it
    mapping = frame2.createObject('AssembledRigidRigidMapping',
                                  template = 'Rigid,Rigid',
                                  input = '@../dofs',
                                  ouput = '@dofs')

    # here we map two output rigid dofs from the input dofs. output
    # dofs are resized automatically. (beware: some mappings are not that friendly !)

    mapping.source = '''
    0  -3 0 0  0 0 0 1
    0  0 2 0  0 0 0 1 
    '''
    

    return 0


