# BridgeMaster
## Playing flow
- Connect BridgeMaster Base with the BridgeMaster Dealer
- BridgeMaster Base connect a wifi
- Player login website and input a BridgeMaster Base code
- Select playing mode on website
- Auction on the BridgeMaster Base
- Analysis on the website
## Web server
- django==2.0.5
### admin
- account: admin
- password: 1234
### app
- Member system  徐煒博
  - rank
  - member data
- Auction learning system 李孟叡
  - web crawler
  - visualize learning
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
## BridgeMaster Base
### function
- Recognition poker 徐煒博
- Auction input 賴冠穎
- Calculate scores 賴冠穎
- Connect to server 賴冠穎
- LCD monitor output 吳凱倫
## BridgeMaster Dealer
### funtion
- Deal cards 廖敏翔, 李孟叡
