from task import task

def test_task():
    assert task((106, 74, 35))
    assert task((17,19,18))
    assert task((54,35,21))
    assert not task((170,113,39))
    assert not task((154,167,167))