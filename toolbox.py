"""various helper functions for the tutorial"""


def rigid(node, **kwargs):
    """build a rigid object under node 'parent'"""

    name = kwargs.get('name', 'unnamed')

    position = kwargs.get('position', None )
    velocity = kwargs.get('velocity', None )

    mass = kwargs.get('mass', 1.0)

    mesh = kwargs.get('mesh', None)
    template = kwargs.get('template', 'Rigid')

    parent = node.createChild(name)
    
    dofs = parent.createObject('MechanicalObject',
                               name = 'dofs',
                               template = template)

    if position: dofs.position = position
    if velocity: dofs.velocity = velocity

    mass = parent.createObject('UniformMass',
                               name = 'mass',
                               template = template,
                               totalMass = mass)
    if mesh:
        
        # visual
        visual = parent.createChild('visual')
        model = visual.createObject('OglModel',
                                    name = 'model',
                                    fileMesh = mesh)
        
        mapping = visual.createObject('RigidMapping',
                                      name = 'mapping')

        # collision
        collision = parent.createChild('collision')

        loader = collision.createObject('MeshObjLoader',
                                        name = 'loader',
                                        filename = mesh)
        
        dofs = collision.createObject('MechanicalObject',
                                      name = 'dofs',
                                      position = '@loader.position')

        mapping = collision.createObject('RigidMapping')
        topology = collision.createObject('MeshTopology', 
                                          name = 'topology',
                                          triangles = '@loader.triangles')
    
        model = collision.createObject('TriangleModel', 
                                       name = 'model')

    return parent

def cat(x):
    if type(x) is list:
        return ' '.join(map(cat, x))
    else: return str(x)


def local_frame(node, **kwargs):

    source = kwargs.get('source', 0)
    coords = kwargs['coords']
    
    name = kwargs.get('name', 'unnamed')
    template = kwargs.get('template', 'Rigid')
    
    frame = node.createChild(name)
    
    dofs = frame.createObject('MechanicalObject',
                              name = 'dofs',
                              template = template)
    
    mapping = frame.createObject('LocalFrameMapping',
                                  template = '{},{}'.format(template, template) )
    
    mapping.source = str(source)
    mapping.coords = cat(coords)
    
    return frame


def joint_dofs(node, parent_path, child_path, **kwargs):
    """path are relative to node"""
    
    name = kwargs.get('name', 'unnamed')

    res = node.createChild(name)
    dofs = res.createObject('MechanicalObject',
                            name = 'dofs',
                            template = 'Vec6')
    mapping = res.createObject('RigidJointMultiMapping',
                               name = 'mapping',
                               template = 'Rigid,Vec6',
                               input = '@../{} @../{}'.format(parent_path, child_path),
                               output = '@dofs',
                               pairs = '0 0')

    return res

def joint(node, parent_path, child_path, **kwargs):
    fixed = kwargs.get('fixed', None)
    compliance = kwargs.get('compliance', 0)
    
    res = joint_dofs(node, parent_path, child_path, **kwargs)
    if fixed:
        constraints = res.createChild('constraints')
        dofs = constraints.createObject('MechanicalObject',
                                        name = 'dofs',
                                        template = 'Vec1')

        mapping = constraints.createObject('MaskMapping',
                                           dofs = cat(fixed))
        
        ff = constraints.createObject('UniformCompliance',
                                      compliance = compliance)

    return res

def setup( node, **kwargs ):

    # load plugin
    plugin = node.createObject('RequiredPlugin',
                               pluginName = 'Compliant')

    plugin = node.createObject('RequiredPlugin',
                               pluginName = 'pouf')


    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior showCollisionModels hideMapping hideVisual'

    # these are from the Compliant plugin
    # ode = node.createObject('CompliantImplicitSolver')
    # num = node.createObject('SequentialSolver',
    #                         iterations = 50,
    #                         precision = 0)

    # these are from the pouf plugin
    ode = node.createObject('pouf_solver')
    num = node.createObject('pouf.pgs',
                            iterations = 50,
                            precision = 0)


    dt = kwargs.get('dt', 1e-2)
    node.dt = dt

    animate = kwargs.get('animate', True)
    node.animate = animate
