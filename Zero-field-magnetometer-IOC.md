## Purpose

The magnetometer reads magnetic field strengths from the beamline. This IOC takes the magnetometer signal, applies corrections and performs a check to make sure that the magnetometer has not been overloaded.

The corrected field strengths are exposed as PVs  when the sequencer controlling the auto-feedback of the zero field is 

## Corrections applied to the input fields

The maths which defines these operations is described in finer detail [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Zero-field-controller#zero-field-controller-feedback-loop).

1. Magnetometer range scaling
   - The three field components are multiplied by a scaling factor to transform the input on to the range of the magnetemeter. The scaling factor is set by the macro `$(RANGE)`, and is held in the PV `$(P)RANGE`.

2. Applying offsets
   - Each component has a unique offset which is subtracted from the scaled data. These offsets are set as the macros `$(OFFSETX), $(OFFSETY), $(OFFSETZ)`. These can also be set by the PVs `$(P):X:OFFSET` and from the OPI.

3. Multiply with sensor matrix
   - To obtain the corrected field strengths, the scaled and offset values need to be multiplied by a 'field sensor' matrix.
   - Macros define the sensor matrix: `$(MATRIX_X_Y)`, where X and Y are the row and column indices.
   - PVs hold the elements of the sensor matrix: `$(P)SENSORMATRIX:XY`. These PVs can also be changed on the OPI.
   - The multiplication iteslf is done as an aSub record. This allows us to use the libraries available to us through GSL.
   - Set up using GSL vector and matrix structures, performing the matrix multiplication is a relatively straightforward call to a vector/matrix multiplication BLAS routine in GSL.
   - The documentation for GSL data structures used is [here](https://www.gnu.org/software/gsl/doc/html/vectors.html).
   - The GSL documentation for BLAS routines is lacking (see [documenatation](https://www.gnu.org/software/gsl/doc/html/blas.html)). To get more in-depth information about the arguments used I would look up the routine in the [BLAS documentation](http://www.netlib.org/blas/).

4. Output
   - The corrected field strengths are written directly to the PVs `$(P)X:CORRECTEDFIELD` from the aSub record.
   - The aSub record also calculates the magnitude of the corrected field and places it in `$(P)FIELDSTRENGTH`.

