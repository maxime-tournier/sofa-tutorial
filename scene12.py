import toolbox
import Sofa

class Script(Sofa.PythonScriptController):
    
    def onBeginAnimationStep(self, dt):
        '''this is called before every simulation step'''
        global shared

        # print some values
        print 'position', shared.dofs.position
        print 'velocity', shared.dofs.velocity

        # change the forcefield force value
        shared.ff.forces = 1e2
        
        return 0


    def onEndAnimationStep(self, dt):
        '''this is called after every simulation step'''
        return 0

    def reset(self):
        '''this is called when resetting the scene'''
        return 0

    # there are more entry points, see the documentation for the
    # SofaPython plugin under sofa/applications/plugins/SofaPython/doc
    

    
class Shared: pass
shared = Shared()
    
def createScene( node ):
    """controlling a scene dynamically"""
    
    toolbox.setup( node )

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

    z = joint.createChild('free')
    dofs = z.createObject('MechanicalObject',
                          template = 'Vec1')
    
    mapping = z.createObject('MaskMapping',
                             dofs = '0 0 0 0 0 1')

    # this will apply a constant force to its neighbor mechanical
    # object, here the z rotation of the joint
    ff = z.createObject('ConstantForceField', forces = '0')

    # the script controller will allow you to modify the scene during
    # simulation
    python = node.createObject('PythonScriptController',
                               filename = __file__,
                               classname = 'Script')

    # this is a shared data structure between the scene creation and
    # the script controller
    global shared
    shared.dofs = dofs
    shared.ff = ff
    
    # WARNING: it is important that you share data *AFTER* the python
    # script controller is created

    return 0


