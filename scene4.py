

def createScene( node ):
    """a single rigid with a donut visual mesh"""
    
    obj = node.createChild('object')

    dofs = obj.createObject('MechanicalObject',
                            name = 'dofs',
                            template = 'Rigid3d')

    dofs.position = [0, 0, 0,
                     0, 0, 0, 1]

    dofs.velocity = [0, 5, 0,
                     0, 0, 0]

    mass = obj.createObject('UniformMass',
                            template = 'Rigid3d',
                            totalMass = 1)

    # we add a visual mesh to the object
    visual = obj.createChild('visual')
    model = visual.createObject('OglModel',
                                fileMesh = 'mesh/torus.obj')
    
    # try commenting this line to see what the mapping does
    mapping = visual.createObject('RigidMapping')


    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior'

    ode = node.createObject('EulerImplicitSolver')
    num = node.createObject('CGLinearSolver')

    node.dt = 1e-2
    node.animate = 1

    return 0


