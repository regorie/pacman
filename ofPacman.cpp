#include "ofPacman.h"

ofPacman::ofPacman() {
	;
}

void ofPacman::init() {

	posX = 24 * posX_init + 36;
	posY = 24 * posY_init + 36;
	posX_idx = posX_init;
	posY_idx = posY_init;

	score = 0;
	pacmanPic_idx = 0;

	pacmanPic[0].loadImage("images/pacman_1.png");
	pacmanPic[0].setAnchorPercent(0.5, 0.5);

	pacmanPic[1].loadImage("images/pacman_2.png");
	pacmanPic[1].setAnchorPercent(0.5, 0.5);

	pacmanPic[2].loadImage("images/pacman_3.png");
	pacmanPic[2].setAnchorPercent(0.5, 0.5);

	pacmanPic[3].loadImage("images/pacman_4.png");
	pacmanPic[3].setAnchorPercent(0.5, 0.5);

}