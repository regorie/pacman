#include "ofApp.h"
#include "ofPacman.h"
#include "ofGhost.h"
#include "ofMath.h"

int myMap[MAX_ROW][MAX_COL];

//--------------------------------------------------------------
void ofApp::setup(){
	// flags, etc
	currDir = 0;
	nextDir = 0;
	gameover = 0;
	gamewin = 0;
	num_of_food = 0;

	// background
	ofSetWindowTitle("PacMan");
	ofBackground(0, 0, 0);

	// font
	myFont.loadFont("Boo City.ttf", 20, true, true);

	// get map information
	getMapInfo();

	// pacman
	pacman.init();

	// ghost
	red.name = "red";
	orange.name = "orange";
	red.init();
	orange.init();
}

//--------------------------------------------------------------
void ofApp::update() {

	if (gameover == 0 && gamewin == 0) {
		// pacman
		movePacman();
		eatFood();
		if (pacman.score == num_of_food) {
			gamewin = 1;
		}

		if (ofDist(pacman.posX, pacman.posY, red.posX, red.posY) <= 10 || ofDist(pacman.posX, pacman.posY, orange.posX, orange.posY) <= 10) {
			// game over
			gameover = 1;
		}

		// ghost
		if (myMap[red.posY_idx][red.posX_idx] == 2 || myMap[red.posY_idx][red.posX_idx] > 4) {
			red.goingOut(myMap);
		}
		else {
			red.move(myMap, pacman.posX_idx, pacman.posY_idx);
		}
		if (red.posX_idx >= col || red.posX_idx < 0) {
			red.currDir = (red.currDir * 2) % 6;
		}
		if (red.posY_idx >= row || red.posY_idx < 0) {
			red.currDir = (red.currDir + 2) % 4;
		}

		if (myMap[orange.posY_idx][orange.posX_idx] == 2 || myMap[orange.posY_idx][orange.posX_idx] > 4) {
			orange.goingOut(myMap);
		}
		else {
			orange.move(myMap, pacman.posX_idx, pacman.posY_idx);
		}
		if (orange.posX_idx >= col || orange.posX_idx < 0) {
			orange.currDir = (orange.currDir * 2) % 6;
		}
		if (orange.posY_idx >= row || orange.posY_idx < 0) {
			orange.currDir = (orange.currDir + 2) % 4;
		}
	}
}

//-------------------------------------------------------------
void ofApp::movePacman() {
	if (currDir != 0) {

		pacman.pacmanPic_idx += 0.2;
		if (pacman.pacmanPic_idx > 3) {
			pacman.pacmanPic_idx = 0;
		}

		if (currDir == 1) {		// UP
			pacman.posY--;
			pacman.posY_idx = pacman.posY / 24 - 1;
		}
		else if (currDir == 2) { // RIGHT
			pacman.posX++;
			pacman.posX_idx = pacman.posX / 24 - 1;
		}
		else if (currDir == 3) { // DOWN
			pacman.posY++;
			pacman.posY_idx = pacman.posY / 24 - 1;
		}
		else if (currDir == 4) { // LEFT
			pacman.posX--;
			pacman.posX_idx = pacman.posX / 24 - 1;
		}

		if (pacman.posX_idx == col) {
			pacman.posX_idx = 0;
			pacman.posX = 24 * pacman.posX_idx + 36;
		}
		if (pacman.posX_idx == -1) {
			pacman.posX_idx = col - 1;
			pacman.posX = 24 * pacman.posX_idx + 36;
		}

		if (myMap[pacman.posY_idx][pacman.posX_idx] == 4 && (pacman.posX == 24 * pacman.posX_idx + 36 && pacman.posY == 24 * pacman.posY_idx + 36)) {

			if (currDir == 1) {		// UP
				if (myMap[pacman.posY_idx - 1][pacman.posX_idx] == 1 || myMap[pacman.posY_idx - 1][pacman.posX_idx] == 2)
					currDir = 0;
			}
			else if (currDir == 2) { // RIGHT
				if (myMap[pacman.posY_idx][pacman.posX_idx + 1] == 1 || myMap[pacman.posY_idx][pacman.posX_idx + 1] == 2)
					currDir = 0;
			}
			else if (currDir == 3) { // DOWN
				if (myMap[pacman.posY_idx + 1][pacman.posX_idx] == 1 || myMap[pacman.posY_idx + 1][pacman.posX_idx] == 2)
					currDir = 0;
			}
			else if (currDir == 4) { // LEFT
				if (myMap[pacman.posY_idx][pacman.posX_idx - 1] == 1 || myMap[pacman.posY_idx][pacman.posX_idx - 1] == 2)
					currDir = 0;
			}

			if (nextDir != 0) {
				if (nextDir == 1) {		// UP
					if (myMap[pacman.posY_idx - 1][pacman.posX_idx] == 0 || myMap[pacman.posY_idx - 1][pacman.posX_idx] == 4) {
						currDir = 1;
						nextDir = 0;
					}
				}
				else if (nextDir == 2) { // RIGHT
					if (myMap[pacman.posY_idx][pacman.posX_idx + 1] == 0 || myMap[pacman.posY_idx][pacman.posX_idx + 1] == 4) {
						currDir = 2;
						nextDir = 0;
					}
				}
				else if (nextDir == 3) { // DOWN
					if (myMap[pacman.posY_idx + 1][pacman.posX_idx] == 0 || myMap[pacman.posY_idx + 1][pacman.posX_idx] == 4) {
						currDir = 3;
						nextDir = 0;
					}
				}
				else if (nextDir == 4) { // LEFT
					if (myMap[pacman.posY_idx][pacman.posX_idx - 1] == 0 || myMap[pacman.posY_idx][pacman.posX_idx - 1] == 4) {
						currDir = 4;
						nextDir = 0;
					}
				}
			}
		}

	}
}

//--------------------------------------------------------------
void ofApp::eatFood() {
	if (food[pacman.posY_idx][pacman.posX_idx] == 1) {
		food[pacman.posY_idx][pacman.posX_idx] = 0;
		pacman.score++;
	}
}

//--------------------------------------------------------------
void ofApp::draw(){

	// draw map
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (myMap[i][j] != 1) {

				if (food[i][j] == 1) {
					ofSetColor(255, 255, 0);
					ofDrawCircle(12 + 24 * (j + 1), 12 + 24 * (i + 1), 2);
				}
		
				ofSetColor(0, 0, 255);
				ofSetLineWidth(5);
				if (myMap[i - 1][j] == 1) { // wall at up
					ofDrawLine(24 * (j + 1), 24 * (i + 1), 24 * (j + 2), 24 * (i + 1));
				}
				if (myMap[i][j - 1] == 1) { // wall at left
					ofDrawLine(24 * (j + 1), 24 * (i + 1), 24 * (j + 1), 24 * (i + 2));
				}
				if (myMap[i][j + 1] == 1) { // wall at right
					ofDrawLine(24 * (j + 2), 24 * (i + 1), 24 * (j + 2), 24 * (i + 2));
				}
				if (myMap[i + 1][j] == 1) { // wall at down
					ofDrawLine(24 * (j + 1), 24 * (i + 2), 24 * (j + 2), 24 * (i + 2));
				}
			}
		}
	}

	ofSetColor(255, 255, 255);

	// ghost
	red.ghostPic[red.currDir - 1].draw(red.posX, red.posY, 15, 15);
	orange.ghostPic[orange.currDir - 1].draw(orange.posX, orange.posY, 15, 15);

	// score
	myFont.drawString("Score : " + ofToString(pacman.score), score_posX, score_posY);

	// pacman
	ofPushMatrix();
	ofTranslate(pacman.posX, pacman.posY);
	ofRotate(currDir * 90 - 180);
	pacman.pacmanPic[(int)pacman.pacmanPic_idx].draw(0, 0, 15, 15);
	ofPopMatrix();
	

	// game play
	if (gameover == 1) {
		myFont.drawString("Game Over!", score_posX, score_posY + 36);
		myFont.drawString("Play Again? (Y/N)", score_posX + 400, score_posY + 36);
	}
	if (gamewin == 1) {
		myFont.drawString("Congratulations!", score_posX, score_posY + 36);
		myFont.drawString("Play Again? (Y/N)", score_posX + 400, score_posY + 36);
	}
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

	if (key == OF_KEY_ESC) {
		ofExit();
	}

	if (currDir != 0) { // pacman is moving

		if (key == OF_KEY_UP) {
			if (currDir == 3)
				currDir = 1;
			else nextDir = UP;
		}
		else if (key == OF_KEY_RIGHT) {
			if (currDir == 4)
				currDir = 2;
			else nextDir = RIGHT;
		}
		else if (key == OF_KEY_DOWN) {
			if (currDir == 1)
				currDir = 3;
			else nextDir = DOWN;
		}
		else if (key == OF_KEY_LEFT) {
			if (currDir == 2)
				currDir = 4;
			else nextDir = LEFT;
		}
	}
	else if (currDir == 0) { // pacman is not moving
		if (key == OF_KEY_UP) {
			if(myMap[pacman.posY_idx - 1][pacman.posX_idx] == 0 || myMap[pacman.posY_idx - 1][pacman.posX_idx] == 4)
				currDir = UP;
		}
		else if (key == OF_KEY_RIGHT) {
			if (myMap[pacman.posY_idx][pacman.posX_idx + 1] == 0 || myMap[pacman.posY_idx][pacman.posX_idx + 1] == 4)
				currDir = RIGHT;
		}
		else if (key == OF_KEY_DOWN) {
			if (myMap[pacman.posY_idx + 1][pacman.posX_idx] == 0 || myMap[pacman.posY_idx + 1][pacman.posX_idx] == 4)
				currDir = DOWN;
		}
		else if (key == OF_KEY_LEFT) {
			if (myMap[pacman.posY_idx][pacman.posX_idx - 1] == 0 || myMap[pacman.posY_idx][pacman.posX_idx - 1] == 4)
				currDir = LEFT;
		}
	}
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){
	if (gameover == 1 || gamewin == 1) {
		if (key == 'Y' || key == 'y') {
			// play again
			pacman.init();
			red.init();
			orange.init();

			currDir = 0;
			nextDir = 0;
			gameover = 0;
			gamewin = 0;
			for (int i = 0; i < row; i++) {
				for (int j = 0; j < col; j++) {
					if (food[i][j] != 2) {
						food[i][j] = 1;
					}
				}
			}
		}
		else if (key == 'N' || key == 'n') {
			ofExit();
		}
	}
}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}

void ofApp::getMapInfo() {

	input_buf.allocate(930);
	input_buf = ofBufferFromFile("map/map01.txt", false);
	string line = new char[30];
	line = input_buf.getFirstLine();
	col = line.length();
	row = input_buf.size() / (col + 1);

	for (int i = 0; i < col; i++) {
		if (line[i] == '1')
			myMap[0][i] = 1;
		else if (line[i] == '0')
			myMap[0][i] = 0;
	}

	for (int i = 1; i < row; i++) {
		line = input_buf.getNextLine();

		for (int j = 0; j < col; j++) {
			if (line[j] == '1') {
				myMap[i][j] = 1;
				food[i][j] = 2;
			}
			else if (line[j] == '0') {
				myMap[i][j] = 0;
				food[i][j] = 1;
				num_of_food++;
			}
			else if (line[j] == '2') {
				myMap[i][j] = 2;
				food[i][j] = 2;
			}
			else if (line[j] == '3') {
				myMap[i][j] = 3;
				pacman.posX_init = j; pacman.posY_init = i;
				food[i][j] = 2;
			}
			else if (line[j] == '4') {
				myMap[i][j] = 4;
				food[i][j] = 1;
				num_of_food++;
			}
			else if (line[j] == '5') {
				myMap[i][j] = 5;
				red.posX_init = j; red.posY_init = i;
				food[i][j] = 2;
			}
			else if (line[j] == '6') {
				myMap[i][j] = 6;
				orange.posX_init = j; orange.posY_init = i;
				food[i][j] = 2;
			}
		}
	}

	score_posX = 36;
	score_posY = 24 * row + 64;
}