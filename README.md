This repository contains a series of
[SOFA](https://www.sofa-framework.org) python scenes introducing rigid
bodies simulation.

# Requirements

You need an up-to-date build of the SOFA framework, compiled with the
`SofaPython` and `Compliant` plugins. To enable these, copy the
`custom_options.cmake` file to the sofa root folder (or add its
content to the existing one, if any), then re-run `cmake`:

```sh
git clone https://scm.gforge.inria.fr/anonscm/git/sofa/sofa.git
# cat /path/to/your/sofa-tutorial/custom_options.cmake >> sofa/custom_options.cmake
cd sofa
mkdir build
cd build
cmake ..
```

Then you need to enable the `SofaPython` plugin in the plugin manager.

```sh
cd sofa/build/bin
./runSofa
```

Then go to `Edit/Plugin Manager` and add the `libSofaPython` library.

# Scenes

Each scene file is self-documented.

- [scene1.py](scene1.py): an empty scene
- [scene2.py](scene2.py): node/object creation, mechanical objects, mass
- [scene3.py](scene3.py): ode and numerical solvers, time step, gravity, visual flags for display
- [scene4.py](scene4.py): mapping a visual model from rigid degrees of freedom
- [scene5.py](scene5.py): mapping collision models
- [scene6.py](scene6.py): refactoring
- [scene7.py](scene7.py): enabling plugins
- [scene8.py](scene8.py): a rigid -> rigid mapping
- [scene9.py](scene9.py): refactoring rigid mappings
- [scene10.py](scene10.py): rigid joint, exponential coordinates, compliance
- [scene11.py](scene11.py): refactoring joints, translation constraints
- [scene12.py](scene12.py): python script controllers, dynamic scene modification
- [scene13.py](scene13.py): a simple PID controller
- [scene14.py](scene14.py): frictional contacts, contact groups
