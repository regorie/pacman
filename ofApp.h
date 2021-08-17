#pragma once

#include "ofMain.h"
#include "ofPacman.h"
#include "ofGhost.h"

#define MAX_ROW 50
#define MAX_COL 50

#define UP 1;
#define RIGHT 2;
#define DOWN 3;
#define LEFT 4;

class ofApp : public ofBaseApp {

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y);
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);

		ofTrueTypeFont myFont;
		ofBuffer input_buf;
		int row, col;
		int score_posX, score_posY;
		int food[MAX_ROW][MAX_COL];
		int num_of_food;
		void getMapInfo();

		int gameover, gamewin;

		ofPacman pacman;
		int currDir, nextDir;

		void movePacman();
		void eatFood();

		ofGhost red;
		ofGhost orange;

};
