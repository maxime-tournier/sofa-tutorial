"""various helper functions for the tutorial"""


def rigid(parent, **kwargs):
    """build a rigid object under node 'parent'"""

    name = kwargs.get('name', 'unnamed')

    position = kwargs.get('position', None )
    velocity = kwargs.get('velocity', None )

    mass = kwargs.get('mass', 1.0)

    mesh = kwargs.get('mesh', None)
    template = kwargs.get('template', 'Rigid3d')

    dofs = parent.createObject('MechanicalObject',
                               name = name,
                               template = template)

    if position: dofs.position = position
    if velocity: dofs.velocity = velocity

    mass = parent.createObject('UniformMass',
                               template = template,
                               totalMass = mass)
    if mesh:
        
        # visual
        visual = parent.createChild('visual')
        model = visual.createObject('OglModel',
                                    fileMesh = mesh)
        mapping = visual.createObject('RigidMapping')

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

