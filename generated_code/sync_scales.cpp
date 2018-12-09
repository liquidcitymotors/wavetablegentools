
#include "sync.hpp"

void ViaSync::initializeScales() {
   scaleArray[0][0] = &integerRatios;
   scaleArray[0][1] = &even_integers;
   scaleArray[0][2] = &rhythm_integers;
   scaleArray[0][3] = &odd_integers;
   scaleArray[1][0] = &modal_tetrads;
   scaleArray[1][1] = &seventhTetradsMinimalProgression;
   scaleArray[1][2] = &impressionist;
   scaleArray[1][3] = &bohlenPeirce;
   scaleArray[2][0] = &modesofroot;
   scaleArray[2][1] = &tetrad_inversions;
   scaleArray[2][2] = &harmonic_entropy;
   scaleArray[2][3] = &bohlenPeircevoct;
   scaleArray[3][0] = &simpleRhythms;
   scaleArray[3][1] = &simpleRhythms16;
   scaleArray[3][2] = &rhythmDivisionsReset;
   scaleArray[3][3] = &polyResets;
}
