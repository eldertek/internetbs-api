from unittest.mock import MagicMock, patch

from internetbs import Account, DNS, Domain, Forwarding, Host


def _mock_response(payload):
    resp = MagicMock()
    resp.status_code = 200
    resp.json.return_value = payload
    return resp


def test_default_and_custom_timeouts_passed_to_requests():
    with patch("requests.get", return_value=_mock_response({"status": "SUCCESS", "balance": [{"currency": "EUR", "amount": "10.00"}]})) as m_get:
        acc = Account("qa-key", "qa-secret", test_mode=False, timeout=12)
        acc.get_balance()
        _, kwargs = m_get.call_args
        assert kwargs["timeout"] == 12
        assert kwargs["verify"] is True

    with patch("requests.get", return_value=_mock_response({"status": "SUCCESS", "transactid": "1", "records": []})) as m_get:
        dns = DNS("qa-key", "qa-secret", timeout=8)
        dns.list_records("sentinel.example")
        _, kwargs = m_get.call_args
        assert kwargs["timeout"] == 8

    with patch("requests.get", return_value=_mock_response({"status": "AVAILABLE", "transactid": "1", "domain": "sentinel.example", "minregperiod": 1, "maxregperiod": 10, "registrarlockallowed": "YES", "privatewhoisallowed": "YES", "realtimeregistration": "YES"})) as m_get:
        dom = Domain("qa-key", "qa-secret")
        dom.check_availability("sentinel.example")
        _, kwargs = m_get.call_args
        assert kwargs["timeout"] == 30


def test_get_last_request_url_masks_credentials_by_default():
    with patch("requests.get", return_value=_mock_response({"status": "SUCCESS", "balance": [{"currency": "EUR", "amount": "5.00"}]})):
        acc = Account("secret-api-key-probe", "secret-pass-probe", test_mode=False)
        acc.get_balance()
        masked = acc.get_last_request_url(reveal=False)
        assert "secret-api-key-probe" not in masked
        assert "secret-pass-probe" not in masked
        assert "ApiKey=%2A%2A%2A" in masked
        revealed = acc.get_last_request_url(reveal=True)
        assert "secret-api-key-probe" in revealed

    with patch("requests.get", return_value=_mock_response({"status": "SUCCESS"})):
        fwd = Forwarding("secret-fwd-key", "secret-fwd-pass", test_mode=False)
        fwd.add_url_forward("sentinel.example", "https://sentinel.example/target")
        masked = fwd.get_last_request_url(reveal=False)
        assert "secret-fwd-key" not in masked
        assert "secret-fwd-pass" not in masked
        assert "Domain=sentinel.example" in masked

    with patch("requests.get", return_value=_mock_response({"status": "SUCCESS"})):
        host = Host("secret-host-key", "secret-host-pass", test_mode=False)
        host.get_host_info("ns1.sentinel.example")
        masked = host.get_last_request_url(reveal=False)
        assert "secret-host-key" not in masked
        assert "secret-host-pass" not in masked
        assert "Host=ns1.sentinel.example" in masked
