import toolbox
import Sofa
import math


class Script(Sofa.PythonScriptController):

    # def __init__(self):
    #     Sofa.PythonScriptController.__init__(self)
    #     self.integral = 0

    def onBeginAnimationStep(self, dt):
        global shared

        print 'position', shared.dofs.position
        print 'velocity', shared.dofs.velocity
        print 'integral', self.integral

        
        error = shared.ref - shared.dofs.position[0][0]
        derror = 0 - shared.dofs.velocity[0][0]

        self.integral += dt * error

        tau = shared.kp * error + shared.kd * derror + shared.ki * self.integral
        shared.ff.forces = tau
        
        return 0


    def onEndAnimationStep(self, dt):
        return 0

    def reset(self):

        self.integral = 0
        shared.ff.forces = 0
        
        return 0


class Shared: pass
shared = Shared()
    
def createScene( node ):
    """control"""
    
    toolbox.setup( node, animate = 0 )

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

    shared.kp = 100
    shared.kd = 10
    shared.ki = 0.5
    shared.ref = math.pi / 3.0
    
    # WARNING: it is important that you share data *AFTER* the python
    # script controller is created

    return 0


