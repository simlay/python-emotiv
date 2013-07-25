#!/bin/bash
sudo cp -r ~/source/np_epoc/osx/EmotivNullDriver.kext /System/Library/Extensions/
sudo kextutil /System/Library/Extensions/EmotivNullDriver.kext

emotive_uninstall() {
	sudo rm -rf /System/Library/Extensions/EmotivNullDriver.kext
}
