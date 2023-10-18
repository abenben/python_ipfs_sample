# IPFS連携サンプルコード（Python）

[IFPS](https://ipfs.tech/)（InterPlanetary File System）は、分散型のファイルシステムであり、インターネットの新しいプロトコルを目指しています。IPFSの主な特徴や概念について以下に簡単にまとめました：

1. **内容ベースのアドレッシング**：IPFSはファイルの内容に基づいてアドレスを生成します。これは、特定のファイルのハッシュを使って行われ、その結果、同じ内容のファイルは常に同じアドレスを持つことになります。このアドレッシング方法のおかげで、キャッシュの効率やデータの重複の削減など、多くの利点があります。

2. **分散ストレージ**：ファイルはIPFSネットワーク上のノードに分散して保存されます。これにより、中央集権的なサーバーやデータセンターに依存しないデータの保存と取得が可能となります。

3. **耐障害性**：ノードがダウンしても、他のノードがそのファイルのコピーを持っている場合、ネットワークはそのファイルを利用可能に保ちます。これにより、ネットワークはより耐障害性が高まります。

4. **高速性**：近くのノードからデータを取得することができるため、ネットワークの遅延が少なく、高速なデータアクセスが可能です。

5. **バージョニングとヒストリー**：IPFSは各ファイルの変更履歴を持つことができ、これによりファイルの異なるバージョンにアクセスすることも可能です。

6. **P2P**：IPFSはピアツーピア（P2P）プロトコルを使用しています。これにより、各ノードが等しく、ネットワーク全体の一部として機能します。

IPFSは、ウェブの分散型バージョンの構築を目指しており、現在のHTTP/HTTPSプロトコルの代替としての潜在的な役割を持っています。これにより、センサーシップのリスクが低減し、ネットワークの効率と耐障害性が向上します。

## 1. IPFSセットアップ



## 2. Pinata


## 3. Pythonコードサンプル