#include "ofGhost.h"

ofGhost::ofGhost(){
	;
}

void ofGhost::init(){
	// initialize position
	// load image

	posX = 24 * posX_init + 36;
	posY = 24 * posY_init + 36;
	posX_idx = posX_init;
	posY_idx = posY_init;
	currDir = 2;
	findOut = 0;

	ghostPic[0].loadImage("images/ghost_" + ofToString(name) + "_up.png");
	ghostPic[0].setAnchorPercent(0.5, 0.5);

	ghostPic[1].loadImage("images/ghost_" + ofToString(name) + "_right.png");
	ghostPic[1].setAnchorPercent(0.5, 0.5);

	ghostPic[2].loadImage("images/ghost_" + ofToString(name) + "_down.png");
	ghostPic[2].setAnchorPercent(0.5, 0.5);

	ghostPic[3].loadImage("images/ghost_" + ofToString(name) + "_left.png");
	ghostPic[3].setAnchorPercent(0.5, 0.5);
}

void ofGhost::move(int myMap[][50], int posX_of_pacman, int posY_of_pacman) {

	int direction[4] = { 0 };
	if (name == "red") {
		targetX = posX_of_pacman;
		targetY = posY_of_pacman;
	}
	else if (name == "orange") {
		targetX = posX_of_pacman + 5;
		targetY = posY_of_pacman + 5;
	}

	if (myMap[posY_idx][posX_idx] != 4 || (posX == 24 * posX_idx + 36 && posY == 24 * posY_idx + 36)) {

		if (currDir == 1) { // UP
			posY--;
			posY_idx = posY / 24 - 1;
		}
		else if (currDir == 2) { // RIGHT
			posX++;
			posX_idx = posX / 24 - 1;
		}
		else if (currDir == 3) {  // DOWN
			posY++;
			posY_idx = posY / 24 - 1;
		}
		else if (currDir == 4) {  // LEFT
			posX--;
			posX_idx = posX / 24 - 1;
		}
	}
	else if (myMap[posY_idx][posX_idx] == 4) {
		if (currDir == 1) { // UP

			posY--;
			posY_idx = posY / 24 - 1;

			if(posY == 24 * posY_idx + 36) {
				// change direction
				if (myMap[posY_idx][posX_idx + 1] == 0 || myMap[posY_idx][posX_idx + 1] == 4) { // target is on right side
					direction[1] = 1;
					if (posX_idx < targetX) {
						currDir = 2; // turn right
						goto changed;
					}
				}
				if (myMap[posY_idx - 1][posX_idx] == 0 || myMap[posY_idx - 1][posX_idx] == 4) { // target is at front
					direction[0] = 1;
					if (posX_idx == targetX) {
						currDir = 1; // go straight
						goto changed;
					}
				}
				if (myMap[posY_idx][posX_idx - 1] == 0 || myMap[posY_idx][posX_idx - 1] == 4) { // target is on left side
					direction[3] = 1;
					if (posX_idx > targetX) {
						currDir = 4; // turn left
						goto changed;
					}
				}

				if (direction[0] == 1) {
					currDir = 1;
					goto changed;
				}
				
				for (int i = 0; i < 4; i++) {
					if (direction[i] == 1) {
						currDir = i + 1;
						break;
					}
				}
				goto changed;
			}
		}
		else if (currDir == 2) { // RIGHT

			posX++;
			posX_idx = posX / 24 - 1;

			if (posX == 24 * posX_idx + 36) {
				// change direction
				if (myMap[posY_idx - 1][posX_idx] == 0 || myMap[posY_idx - 1][posX_idx] == 4) { // target is higher
					direction[0] = 1;
					if (posY_idx > targetY) {
						currDir = 1; // go up
						goto changed;
					}
				}
				if (myMap[posY_idx][posX_idx + 1] == 0 || myMap[posY_idx][posX_idx + 1] == 4) { // target is at front
					direction[1] = 1;
					if (posY_idx == targetY) {
						currDir = 2; // go straight
						goto changed;
					}
				}
				if (myMap[posY_idx + 1][posX_idx] == 0 || myMap[posY_idx + 1][posX_idx] == 4) { // target is lower
					direction[2] = 1;
					if (posY_idx < targetY) {
						currDir = 3; // go down
						goto changed;
					}
				}

				if (direction[1] == 1) {
					currDir = 2;
					goto changed;
				}
				
				for (int i = 0; i < 4; i++) {
					if (direction[i] == 1) {
						currDir = i + 1;
						break;
					}
				}
				goto changed;
			}
		}
		else if (currDir == 3) {  // DOWN

			posY++;
			posY_idx = posY / 24 - 1;

			if (posY == 24 * posY_idx + 36) {
				// change direction
				if (myMap[posY_idx][posX_idx + 1] == 0 || myMap[posY_idx][posX_idx + 1] == 4) { // target is on right side
					direction[1] = 1;
					if (posX_idx < targetX) {
						currDir = 2; // turn right
						goto changed;
					}
				}
				if (myMap[posY_idx + 1][posX_idx] == 0 || myMap[posY_idx + 1][posX_idx] == 4) { // target is at front
					direction[2] = 1;
					if (posX_idx == targetX) {
						currDir = 3; // go straight
						goto changed;
					}
				}
				if (myMap[posY_idx][posX_idx - 1] == 0 || myMap[posY_idx][posX_idx - 1] == 4) { // target is on left side
					direction[3] = 1;
					if (posX_idx > targetX) {
						currDir = 4; // turn left
						goto changed;
					}
				}

				if (direction[2] == 1) {
					currDir = 3;
					goto changed;
				}
				
				for (int i = 0; i < 4; i++) {
					if (direction[i] == 1) {
						currDir = i + 1;
						break;
					}
				}
				goto changed;
			}
		}
		else if (currDir == 4) {  // LEFT

			posX--;
			posX_idx = posX / 24 - 1;

			if (posX == 24 * posX_idx + 36) {
				// change direction
				if (myMap[posY_idx - 1][posX_idx] == 0 || myMap[posY_idx - 1][posX_idx] == 4) { // target is higher
					direction[0] = 1;
					if (posY_idx > targetY) {
						currDir = 1; // go up
						goto changed;
					}
				}
				if (myMap[posY_idx][posX_idx - 1] == 0 || myMap[posY_idx][posX_idx - 1] == 4) { // target is at front
					direction[3] = 1;
					if (posY_idx == targetY) {
						currDir = 4; // go straight
						goto changed;
					}
				}
				if (myMap[posY_idx + 1][posX_idx] == 0 || myMap[posY_idx + 1][posX_idx] == 4) { // target is lower
					direction[2] = 1;
					if (posY_idx < targetY) {
						currDir = 3; // go down
						goto changed;
					}
				}

				if (direction[3] == 1) {
					currDir = 4;
					goto changed;
				}

				for (int i = 0; i < 4; i++) {
					if (direction[i] == 1) {
						currDir = i + 1;
						break;
					}
				}
				goto changed;
			}
		}
	}
changed:;
}

void ofGhost::goingOut(int myMap[][50]) {

	if (!findOut) {
		if (currDir == 2) { // RIGHT
			if (myMap[posY_idx - 1][posX_idx] != 1 && posX == 24 * posX_idx + 36) {
				currDir = 1;
				findOut = 1;
				posX--;
			}
			else {
				if (myMap[posY_idx][posX_idx + 1] == 1 && posX == 24 * posX_idx + 36) {
					currDir = 3;
				}
				else {
					posX++;
					posX_idx = posX / 24 - 1;
				}
			}
		}
		else if (currDir == 3) { // DOWN
			if (myMap[posY_idx][posX_idx + 1] != 1 && posY == 24 * posY_idx + 36) {
				currDir = 2;
				findOut = 1;
				posY--;
			}
			else {
				if (myMap[posY_idx + 1][posX_idx] == 1 && posY == 24 * posY_idx + 36) {
					currDir = 4;
				}
				else {
					posY++;
					posY_idx = posY / 24 - 1;
				}
			}
		}
		else if (currDir == 4) {  // LEFT
			if (myMap[posY_idx + 1][posX_idx] != 1 && posX == 24 * posX_idx + 36) {
				currDir = 3;
				findOut = 1;
				posX++;
			}
			else {
				if (myMap[posY_idx][posX_idx - 1] == 1 && posX == 24 * posX_idx + 36) {
					currDir = 1;
				}
				else {
					posX--;
					posX_idx = posX / 24 - 1;
				}
			}
		}
		else if (currDir == 1) {  // UP
			if (myMap[posY_idx][posX_idx - 1] != 1 && posY == 24 * posY_idx + 36) {
				currDir = 4;
				findOut = 1;
				posY++;
			}
			else {
				if (myMap[posY_idx - 1][posX_idx] == 1 && posY == 24 * posY_idx + 36) {
					currDir = 2;
				}
				else {
					posY--;
					posY_idx = posY / 24 - 1;
				}
			}
		}
	}
	else{
		if (myMap[posY_idx][posX_idx] != 0) {
			if (currDir = 1) { // UP
				posY--;
				posY_idx = posY / 24 - 1;
			}
			else if (currDir = 2) {  // RIGHT
				posX++;
				posX_idx = posX / 24 - 1;
			}
			else if (currDir = 3) {  // DOWN
				posY++;
				posY_idx = posY / 24 - 1;
			}
			else if (currDir = 4) {  // LEFT
				posX--;
				posX_idx = posX / 24 - 1;
			}
		}
	}
}