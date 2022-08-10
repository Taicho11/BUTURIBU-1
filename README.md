# BUTURIBU-1
ゼロつくgithub https://github.com/oreilly-japan/deep-learning-from-scratch

※githubに載ってる順じゃなくて時系列順に説明する

１．データ収集

〈foldermaking.py〉
    学習データ(になりたい写真)を集めるために必要なフォルダを作る。

〈ro-ba-control.py〉
    学習データ(になりたい写真)をカメラで撮影してfoldermakingで作ったフォルダに入れる。

〈camera.control.py〉
    ro-ba-controlより優れた撮影プログラム
    
 ２．AI作成
 
〈dataprosess.py〉
    写真は撮ったままだとデータとして使えないから、写真の形を学習データ用に調整する。
    そして写真を基に教師データを出力する。
    最後に学習データと教師データをそれぞれ訓練データとテストデータに分類する。

〈learning1st.py〉
    dataprosessで作ったデータをこのスクリプトを用いてAIにする。
    
３．実践

〈plactice_1st.py〉
    learning1stで作ったAIを実行して、ローバーを動かす。

〈practice1st.py〉
    plactice_1stの補助。
