if ! [ -x "$(command -v pip)" ]; then
    sudo apt-get update && sudo apt-get install -qq -y python-pip libpython-dev
    curl -O https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py
fi
sudo pip install wheel
sudo pip install awscli==1.11.18