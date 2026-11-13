def test_search_returns_results(client):
    resp = client.get("/products/search", params={"q": "Mouse"})
    assert resp.status_code == 200
    assert resp.json()["count"] >= 1
