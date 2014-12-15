import toolbox

def createScene( node ):
    """plugins"""
    
    obj = node.createChild('object')

    toolbox.rigid(obj,
                  velocity = [0, 5, 0,
                              0, 1, 0],
                  mesh = 'mesh/torus.obj')

    # forces sofa to load a plugin before continuing
    plugin = node.createObject('RequiredPlugin',
                               pluginName = 'Compliant')
    
    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior showCollision showMapping hideVisual'

    # these are from the Compliant plugin
    ode = node.createObject('CompliantImplicitSolver')
    num = node.createObject('SequentialSolver')

    node.dt = 1e-2
    node.animate = 1

    return 0


