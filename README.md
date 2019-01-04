# BridgeMaster
## Playing flow
- Connect BridgeMaster Base with the BridgeMaster Dealer
- BridgeMaster Base connect a wifi
- Player login website and input a BridgeMaster Base code
- Select playing mode on website
- Auction on the BridgeMaster Base
- Analysis on the website
## Bridge Master Base
- dealer
- auction input (by keyboard)
- monitor output (by oled)
### module design
- [Python Tutorial 第二堂（3）函式、模組、類別與套件](http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-3-function-module-class-package)
## Web server
- django==2.0.5
### admin
- account: admin
- password: bridge1234
### app
- Member system  徐煒博
  - rank
  - member data
- Auction learning system 李孟叡
  - web crawler
  - visualize learning
  - [ACBL learn to play bridge](http://www.learn2playbridge.com/)
- Analysis system 吳凱倫
  - auction best case
  - playing best case
- Playing mode 廖敏翔
  - random or classic game
    - round要加入首引的玩家和牌(classic game)
    - 最後的合約(classic game)
    - lead_player=NULL(classic game)
    - bid要紀錄4家(歷史牌局)
  - classic game explaintion
### ER schema
- Tid
- bid (have first bid player)
- N
- E
- S
- W
- vulnerable
- contract
- leader
- ---------------
- Rnumber(new)
- declarer
- result (declarer's win trick)
- score (declarer's score)
