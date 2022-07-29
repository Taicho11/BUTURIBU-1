# BUTURIBU-1
ゼロつくgithub https://github.com/oreilly-japan/deep-learning-from-scratch

※githubに載ってる順じゃなくて時系列順に説明するよ
〈foldermaking.py〉
    学習データ(になりたい写真)を集めるために必要なフォルダを作るよ。

〈ro-ba-control.py〉
    学習データ(になりたい写真)をカメラで撮影してfoldermakingで作ったフォルダに入れるよ。sikosiko。

〈dataprosess.py〉
    写真は撮ったままだとデータとして使えないから、写真の形を学習データ用に調整するよ。
    そして写真を基に教師データを出力するよ。
    最後に学習データと教師データをそれぞれ訓練データとテストデータに分類するよ。

〈learning1st.py〉
    dataprosessで作ったデータをこの子に突っ込むとAIになるよ。

〈plactice_1st.py〉
    learning1stで作ったAIを実行して、ローバーを動かすよ。

〈practice1st.py〉
    plactice_1stの補助だよ
