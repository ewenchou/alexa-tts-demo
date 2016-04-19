# alexa-tts-demo

A simple example showing how to use [alexa-client](https://github.com/ewenchou/alexa-client) and [simple-tts](https://github.com/ewenchou/simple-tts) together to interact with Amazon Alexa Voice Service.

# Prerequisites

This demo is designed to run on Linux. In particular, Ubuntu 14.04 LTS was used to test it.

# Installation

1. Install `mpg123` and `festival` packages on Ubuntu

  ```
  sudo apt-get install mpg123 festival
  ```

2. Install Python PIP and Virtualenv

  ```
  sudo apt-get install python-pip
  sudo pip install virtualenv
  ```

3. Clone this repository and setup virtualenv

  ```
  git clone https://github.com/ewenchou/alexa-tts-demo.git
  cd alexa-tts-demo
  virtualenv env
  ```

4. Activate virtualenv and install Python requirements

  ```
  source env/bin/activate
  pip install -r requirements.txt
  ```

5. Run the demo

  ```
  python main.py
  ```

# Further Details

* [alexa-client](https://github.com/ewenchou/alexa-client)

* [simple-tts](https://github.com/ewenchou/simple-tts)
