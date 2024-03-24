#ifndef CORE_PMA_H
#define CORE_PMA_H
#include <Arduino.h>
#include "profet_pmm.h"

/* Class definition of CorePMA for L4 Buoy Power Management Array
 * CorePMA utilizes the ProfetPMM class module to create interfaces
 * to Infineon Profet hardware
 */

/* A PROFET module connected directly to an arduino has the following pin configuration
 * > Battery Voltage Sense: A1
 * > CH 1: Trigger Pin D9;  Is Pin A2; DEN Pin D6
 * > CH 2: Trigger Pin D10; Is Pin A2; DEN Pin D8
 * > CH 3: Trigger Pin D11; Is Pin A3; DEN Pin D6
 * > CH 4: Trigger Pin D3;  Is Pin A3; DEN Pin D8
*/
const int N_OF_MODULES = 4;
const int N_OF_CHANNELS = 16;
const int M1_P_CH_1[4] = {31,31,1,13};
const int M1_P_CH_2[4] = {32,32,1,12};
const int M1_P_CH_3[4] = {33,33,2,13};
const int M1_P_CH_4[4] = {34,34,2,12};
const int M2_P_CH_1[4] = {35,35,4,11};
const int M2_P_CH_2[4] = {36,36,4,10};
const int M2_P_CH_3[4] = {37,37,5,11};
const int M2_P_CH_4[4] = {38,38,5,10};
const int M3_P_CH_1[4] = {39,39,7,9};
const int M3_P_CH_2[4] = {40,40,7,8};
const int M3_P_CH_3[4] = {41,41,8,9};
const int M3_P_CH_4[4] = {42,42,8,8};
const int M4_P_CH_1[4] = {44,44,10,7};
const int M4_P_CH_2[4] = {45,45,10,6};
const int M4_P_CH_3[4] = {46,46,11,7};
const int M4_P_CH_4[4] = {47,47,11,6};

class CorePMA {

  public:
      // ProfetPMM imcs_pmm_1[4] = { ProfetPMM(1,1, ...), ... };
      ProfetPMM imcs_channels[N_OF_CHANNELS] = {
      ProfetPMM(1,1,M1_P_CH_1[0],M1_P_CH_1[1],M1_P_CH_1[2],1,M1_P_CH_1[3]),
      ProfetPMM(1,2,M1_P_CH_2[0],M1_P_CH_2[1],M1_P_CH_2[2],1,M1_P_CH_2[3]),
      ProfetPMM(1,3,M1_P_CH_3[0],M1_P_CH_3[1],M1_P_CH_3[2],1,M1_P_CH_3[3]),
      ProfetPMM(1,4,M1_P_CH_4[0],M1_P_CH_4[1],M1_P_CH_4[2],1,M1_P_CH_4[3]),
      ProfetPMM(2,5,M2_P_CH_1[0],M2_P_CH_1[1],M2_P_CH_1[2],1,M2_P_CH_1[3]),
      ProfetPMM(2,6,M2_P_CH_2[0],M2_P_CH_2[1],M2_P_CH_2[2],1,M2_P_CH_2[3]),
      ProfetPMM(2,7,M2_P_CH_3[0],M2_P_CH_3[1],M2_P_CH_3[2],1,M2_P_CH_3[3]),
      ProfetPMM(2,8,M2_P_CH_4[0],M2_P_CH_4[1],M2_P_CH_4[2],1,M2_P_CH_4[3]),
      ProfetPMM(3,9,M3_P_CH_1[0],M3_P_CH_1[1],M3_P_CH_1[2],1,M3_P_CH_1[3]),
      ProfetPMM(3,10,M3_P_CH_2[0],M3_P_CH_2[1],M3_P_CH_2[2],1,M3_P_CH_2[3]),
      ProfetPMM(3,11,M3_P_CH_3[0],M3_P_CH_3[1],M3_P_CH_3[2],1,M3_P_CH_3[3]),
      ProfetPMM(3,12,M3_P_CH_4[0],M3_P_CH_4[1],M3_P_CH_4[2],1,M3_P_CH_4[3]),
      ProfetPMM(4,13,M4_P_CH_1[0],M4_P_CH_1[1],M4_P_CH_1[2],1,M4_P_CH_1[3]),
      ProfetPMM(4,14,M4_P_CH_2[0],M4_P_CH_2[1],M4_P_CH_2[2],1,M4_P_CH_2[3]),
      ProfetPMM(4,15,M4_P_CH_3[0],M4_P_CH_3[1],M4_P_CH_3[2],1,M4_P_CH_3[3]),
      ProfetPMM(4,16,M4_P_CH_4[0],M4_P_CH_4[1],M4_P_CH_4[2],1,M4_P_CH_4[3]),
    };

    CorePMA();
    int MODE;
    void init();
    void run(); 
    String core_status(bool verbose);
    void set_power_ch(int channel,bool state);
    void cycle_power_ch(int channel);
    void toggle_power_ch(int channel);
    void setMode(int mode);


};


#endif
