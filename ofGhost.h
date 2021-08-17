#ifndef _OF_GHOST
#define _OF_GHOST

#include "ofMain.h"

class ofGhost {
	public:
		ofGhost();
		void init();
		void move(int myMap[][50], int, int);
		void goingOut(int myMap[][50]);

		string name;
		int findOut;
		int targetX, targetY;
		int posX_init, posY_init;
		int posX, posY;
		int posX_idx, posY_idx;
		int currDir;
		
		ofImage ghostPic[4];
};

#endif