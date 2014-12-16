import toolbox

def createScene( node ):
    """some refactoring"""
    
    obj = toolbox.rigid(node,
                        name = 'object',
                        velocity = [0, 5, 0,
                                    0, 1, 0],
                        mesh = 'mesh/torus.obj')

    # key = value arguments are passed as a dictionary to the toolbox.rigid function
    
    # => { 'velocity': [0, 5, 0 ... ], 'mesh': 'mesh/torus.obj' }
    
    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior showCollision showMapping hideVisual'

    ode = node.createObject('EulerImplicitSolver')
    num = node.createObject('CGLinearSolver')

    node.dt = 1e-2
    node.animate = 1

    return 0



