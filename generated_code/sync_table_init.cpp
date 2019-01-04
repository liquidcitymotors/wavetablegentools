#include "sync.hpp"


void ViaSync::fillWavetableArray(void) {

	wavetableArray[	0][0] = &wavetableSet.additive_evens;
	wavetableArray[	0][1] = &wavetableSet.mountains;
	wavetableArray[	0][2] = &wavetableSet.newBounce;
	wavetableArray[	0][3] = &wavetableSet.circular_257;
	wavetableArray[	1][0] = &wavetableSet.impevens;
	wavetableArray[	1][1] = &wavetableSet.additive_tri_to_pulse;
	wavetableArray[	1][2] = &wavetableSet.new_perlin;
	wavetableArray[	1][3] = &wavetableSet.csound_formants;
	wavetableArray[	2][0] = &wavetableSet.additive_pairs;
	wavetableArray[	2][1] = &wavetableSet.moogSquare;
	wavetableArray[	2][2] = &wavetableSet.test_fm;
	wavetableArray[	2][3] = &wavetableSet.trains;
	wavetableArray[	3][0] = &wavetableSet.sharpExpoSym;
	wavetableArray[	3][1] = &wavetableSet.gammaAsym;
	wavetableArray[	3][2] = &wavetableSet.newest_steps;
	wavetableArray[	3][3] = &wavetableSet.block_test;
	wavetableArrayGlobal[0] = &wavetableSet.triOdd;
	wavetableArrayGlobal[1] = &wavetableSet.sinwavefold_257;
	wavetableArrayGlobal[2] = &wavetableSet.euclidean_test;
	wavetableArrayGlobal[3] = &wavetableSet.skipSaw;
}

constexpr Wavetable SyncWavetableSet::newBounce;
constexpr Wavetable SyncWavetableSet::euclidean_test;
constexpr Wavetable SyncWavetableSet::impevens;
constexpr Wavetable SyncWavetableSet::additive_tri_to_pulse;
constexpr Wavetable SyncWavetableSet::additive_pairs;
constexpr Wavetable SyncWavetableSet::newest_steps;
constexpr Wavetable SyncWavetableSet::mountains;
constexpr Wavetable SyncWavetableSet::additive_evens;
constexpr Wavetable SyncWavetableSet::csound_formants;
constexpr Wavetable SyncWavetableSet::test_fm;
constexpr Wavetable SyncWavetableSet::new_perlin;
constexpr Wavetable SyncWavetableSet::gammaAsym;
constexpr Wavetable SyncWavetableSet::triOdd;
constexpr Wavetable SyncWavetableSet::trains;
constexpr Wavetable SyncWavetableSet::skipSaw;
constexpr Wavetable SyncWavetableSet::moogSquare;
constexpr Wavetable SyncWavetableSet::circular_257;
constexpr Wavetable SyncWavetableSet::sharpExpoSym;
constexpr Wavetable SyncWavetableSet::sinwavefold_257;
constexpr Wavetable SyncWavetableSet::block_test;

constexpr uint16_t SyncWavetableSet::moogSquareShiftAttackFamily[9][257];

constexpr uint16_t SyncWavetableSet::moogSquareShiftReleaseFamily[9][257];

constexpr uint16_t SyncWavetableSet::trioddAttackFamily[9][257];

constexpr uint16_t SyncWavetableSet::gammaAsymAttackFamily[9][257];

constexpr uint16_t SyncWavetableSet::gammaAsymReleaseFamily[9][257];

constexpr uint16_t SyncWavetableSet::sharpExpoSymAttackFamily[9][257];

constexpr uint16_t SyncWavetableSet::impshort[9][257];

constexpr uint16_t SyncWavetableSet::skipsaw[5][257];

constexpr uint16_t SyncWavetableSet::sinwavefold_257_Family[9][257];

constexpr uint16_t SyncWavetableSet::additive_tri_to_pulseFamily[5][257];

constexpr uint16_t SyncWavetableSet::newBounceFamily[5][257];

constexpr uint16_t SyncWavetableSet::circular_257_slopes[4][257];

constexpr uint16_t SyncWavetableSet::test_fm_attack[5][257];

constexpr uint16_t SyncWavetableSet::test_fm_release[5][257];

constexpr uint16_t SyncWavetableSet::trains_attack[9][257];

constexpr uint16_t SyncWavetableSet::trains_release[9][257];

constexpr uint16_t SyncWavetableSet::csound_formants_attack[9][257];

constexpr uint16_t SyncWavetableSet::csound_formants_release[9][257];

constexpr uint16_t SyncWavetableSet::new_perlin_slope[9][257];

constexpr uint16_t SyncWavetableSet::new_perlin_slope_2[9][257];

constexpr uint16_t SyncWavetableSet::additive_pairs_slopes[9][257];

constexpr uint16_t SyncWavetableSet::euclidean_test_slopes[6][257];

constexpr uint16_t SyncWavetableSet::block_test_attack[9][257];

constexpr uint16_t SyncWavetableSet::block_test_release[9][257];

constexpr uint16_t SyncWavetableSet::newest_steps_attack[9][257];

constexpr uint16_t SyncWavetableSet::newest_steps_release[9][257];

constexpr uint16_t SyncWavetableSet::mountains_attack[4][257];

constexpr uint16_t SyncWavetableSet::mountains_release[4][257];

constexpr uint16_t SyncWavetableSet::additive_evens_attack[9][257];


// declare functions to set the currently active tables
void ViaSync::switchWavetable(const Wavetable * table) {
	wavetableSet.loadWavetableWithDiff(table, (uint32_t *) wavetableRead);
	syncWavetable.tableSize = table->numWaveforms - 1;
}

// declare functions to set the currently active tables
void ViaSync::switchWavetableGlobal(const Wavetable * table) {
	wavetableSet.loadWavetableWithDiff(table, (uint32_t *) wavetableRead);
	syncWavetable.tableSize = table->numWaveforms - 1;
}

//// declare functions to set the currently active tables
//void ViaSync::initPhaseDistTable(void) {
//	loadPhaseDistTable(&phaseDistPWM, phaseDistRead);
//}

