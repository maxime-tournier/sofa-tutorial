

def createScene( node ):
    """a scene with a single rigid body, with visual and collision models"""
    
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

    visual = obj.createChild('visual')
    model = visual.createObject('OglModel',
                                fileMesh = 'mesh/torus.obj')

    mapping = visual.createObject('RigidMapping')

    # now we add a collision model
    collision = obj.createChild('collision')

    # load a mesh into a component
    loader = collision.createObject('MeshObjLoader',
                                    name = 'loader',
                                    filename = 'mesh/torus.obj')

    # dofs for mesh vertices, with position obtained from the loader
    dofs = collision.createObject('MechanicalObject',
                                  name = 'dofs',
                                  template = 'Vec3d',
                                  position = '@loader.position')

    # map vertices rigidly from parent dofs (according to their
    # initial position)
    mapping = collision.createObject('RigidMapping')
    

    # now we extract the topology form the mesh (ie. neighbour
    # information, connectivity, etc...). this acts as a proxy
    # for different data sources (here an obj mesh)
    topology = collision.createObject('MeshTopology', 
                                      name = 'topology',
                                      triangles = '@loader.triangles')
    
    # and create a triangle model from it
    model = collision.createObject('TriangleModel', 
                                   name = 'model')


    style = node.createObject('VisualStyle')
    style.displayFlags = 'showBehavior showCollision showMapping hideVisual'

    ode = node.createObject('EulerImplicitSolver')
    num = node.createObject('CGLinearSolver')

    node.dt = 1e-2
    node.animate = 1






    return 0


