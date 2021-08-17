#ifndef _OF_PACMAN
#define _OF_PACMAN

#include "ofMain.h"

class ofPacman {
	public:
		ofPacman();
		void init();

		int posX_init, posY_init;
		int posX, posY;
		int posX_idx, posY_idx; // index if map[][]
		int score;

		float pacmanPic_idx;
		ofImage pacmanPic[4];
};

#endif