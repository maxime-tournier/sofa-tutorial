import toolbox
import math


def createScene( node ):
    """contacts"""
    
    toolbox.setup( node, animate = 0 )


    # enabling contacts:
    
    node.createObject('DefaultPipeline', name = 'pipeline')
    
    node.createObject('BruteForceDetection', name = 'detection')
    proximity = node.createObject('NewProximityIntersection',
                                  name = 'proximity' )

    # collision detection parameters
    proximity.alarmDistance = 0.1
    proximity.contactDistance = 0.02

    # frictional contacts + coefficient
    manager = node.createObject('DefaultContactManager',
                                name = 'manager',
                                response = "FrictionCompliantContact",
                                responseParams = "mu=0.4&horizontalConeProjection=1" )



    obj1 = toolbox.rigid(node,
                         name = 'object1',
                         mesh = 'mesh/torus.obj')

    obj1.createObject('FixedConstraint',
                      indices = '0')

    frame1 = toolbox.local_frame(obj1,
                                 name = 'frame',
                                 coords = [3, 0, 0,
                                           0, 0, 0, 1])
    dofs = frame1.getObject('dofs')
    dofs.showObject = True
    dofs.showObjectScale = 1
    

    obj2 = toolbox.rigid(node,
                         name = 'object2',
                         position = [6, 0, 0,
                                     0, 0, 0, 1],
                         mesh = 'mesh/torus.obj')

    obj3 = toolbox.rigid(node,
                         name = 'object3',
                         position = [3, 3, 0,
                                     0, 0, 0, 1],
                         mesh = 'mesh/torus.obj')


    
    frame2 = toolbox.local_frame(obj2,
                                 name = 'frame',
                                 coords = [-3, 0, 0,
                                           0, 0, 0, 1] )
    dofs = frame2.getObject('dofs')
    dofs.showObject = True
    dofs.showObjectScale = 1

    joint = toolbox.joint(node,
                          'object1/frame/dofs',
                          'object2/frame/dofs',
                          name = 'joint',
                          fixed = [1, 1, 1, 0, 0, 0])

    stiffness = 1e2
    ff = joint.createObject('UniformCompliance',
                            compliance = 1.0 / stiffness)
    
    return 0


