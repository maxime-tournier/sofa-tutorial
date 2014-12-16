import toolbox
import Sofa

class Script(Sofa.PythonScriptController):

    def onBeginAnimationStep(self, dt):
        global shared

        print 'position', shared.dofs.position
        print 'velocity', shared.dofs.velocity

        shared.ff.forces = 1e2
        
        return 0


    def onEndAnimationStep(self, dt):
        return 0

    def reset(self):
        return 0


class Shared: pass
shared = Shared()
    
def createScene( node ):
    """pid control"""
    
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

    ff = z.createObject('ConstantForceField', forces = '0')
    
    python = node.createObject('PythonScriptController',
                               filename = __file__,
                               classname = 'Script')

    global shared
    shared.dofs = dofs
    shared.ff = ff
    
    # WARNING: it is important that you share data *AFTER* the python
    # script controller is created

    return 0


