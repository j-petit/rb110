import pytest
from utilities import getZugfinderData
from datetime import date, timedelta

#@pytest.mark.skip(reason="no way of currently testing this")
def test_getData():
    yesterday = date.today() - timedelta(1)
    data = getZugfinderData(yesterday, "Naunhof", "Leipzig_Hbf")
    print(data.to_string())
    assert len(data.index) > 5
    assert len(data['train_no']) > 5
    assert data.shape[1] == 6
