import ipfshttpclient

def save_to_ipfs(data):
    """
    Save data to IPFS.

    Parameters:
    - data (str): The string data to be saved.

    Returns:
    - dict: IPFS response containing the CID (Content Identifier) of the saved data.
    """
    with ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5002') as client:
    #with ipfshttpclient.connect() as client:
        result = client.add_str(data)
        return result

if __name__ == "__main__":
    data = "こんにちは、IPFS!"
    response = save_to_ipfs(data)
    print(f"Data saved to IPFS with CID: {response['Hash']}")