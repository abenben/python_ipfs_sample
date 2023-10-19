from web3 import Web3
from ipfshttpclient import connect
import time


def save_to_ipfs(data):
    # IPFSノードに接続
    client = connect('/ip4/127.0.0.1/tcp/5002/http')

    # データをIPFSに保存
    res = client.add_str(data)

    client.close()

    return res


def get_from_ipfs(cid):
    # IPFSノードに接続
    client = connect('/ip4/127.0.0.1/tcp/5002/http')

    # データをIPFSから取得
    res = client.cat(cid)

    client.close()

    return res


def set_pin(cid):
    # IPFSノードに接続
    client = connect('/ip4/127.0.0.1/tcp/5002/http')

    res = client.pin.add(cid)

    client.close()

    return res


def rm_pin(cid):
    # IPFSノードに接続
    client = connect('/ip4/127.0.0.1/tcp/5002/http')

    res = client.pin.rm(cid)

    client.close()

    return res


def gc():
    # IPFSノードに接続
    client = connect('/ip4/127.0.0.1/tcp/5002/http')

    # ガベージコレクションを実行
    result = client.repo.gc()

    print(result)

    # 接続を閉じる
    client.close()


def main():
    # 保存するデータ
    data = "Hello, Hello, Hello, Hello, IPFS!"

    # データをIPFSに保存し、そのCIDを取得
    cid = save_to_ipfs(data)
    print(f"Data saved to IPFS with CID: {cid}")

    res = set_pin(cid)
    print(f"Data saved to IPFS with CID: {res}")

    # CIDを指定してデータをIPFSから取得
    res = get_from_ipfs(cid)
    print(f"Data retrieved from IPFS: {res}")

    # res = rm_pin(cid)
    # print(f"Data saved to IPFS with CID: {res}")
    #
    # # CIDを指定してデータをIPFSから取得
    # res = get_from_ipfs(cid)
    # print(f"Data retrieved from IPFS: {res}")
    #
    # # 無限ループ
    # while True:
    #
    #     gc()
    #
    #     # 待機
    #     time.sleep(5)


if __name__ == "__main__":
    main()
