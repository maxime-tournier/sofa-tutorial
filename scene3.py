

def createScene( node ):
    """now we add a ode solver and numerical solver to the scene"""
    
    obj = node.createChild('object')

    dofs = obj.createObject('MechanicalObject',
                            name = 'dofs',
                            template = 'Rigid3d')

    # initial conditions
    dofs.position = [0, 0, 0,
                     0, 0, 0, 1]

    dofs.velocity = [0, 5, 0,
                     0, 0, 0]

    mass = obj.createObject('UniformMass',
                            template = 'Rigid3d',
                            totalMass = 1)

    # checkboxes in the visual style widget
    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior hideCollision'

    # these are reasonable defaults in the absence of contacts
    ode = node.createObject('EulerImplicitSolver')
    num = node.createObject('CGLinearSolver')

    # simulation time-step
    node.dt = 1e-2


    # gravity
    node.gravity = [0, -9.81, 0]

    # if for some reason this fails, you can use character strings instead
    # node.gravity = '0 -9.81 0'
    
    # start animation automatically
    node.animate = 1
    
    return 0


