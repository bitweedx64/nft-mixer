# NFT Mixer

## Introduction
Actually this project has basically no connection with any NFT stuff. It's just an idea inspired by current NFT crazy 
trend that combines difference element of a same-size avatar to sell on OpenSea.

The idea is crazy, the fundamental part of this idea is to generate picture from different PNGs and blend them together.
Just in case somebody wants to make hot money, so I'll open source this short snippets ASAP. Maybe more complicated
functions will be added later on. Like simple publish directly to OpenSea or Solanart etc.



## Usage

This project is based on Python 3.8. Build using `pillow`. All operation is under the project path.

Install the dependencies before using.
```shell
pip3 install --user -r requirements.txt
```

For mixed photo generation. Place your pre-made avatars into `./jigsaw` folder under project. File structure be like: 
```
--jigsaw
    |- head - ...
    |- body - ...
    |- foot - ...
```
Then run the mixer script to start generate.

```shell
python3 mixer.py
```
