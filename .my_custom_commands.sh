#! D:\Program Files\Git

function clone() {
    cd 
    cd d:/dev
    git clone $1
}

function create() {
    cd
    cd d:/dev/GitAutomator
    python gitAuto.py $1 $2 $3
}