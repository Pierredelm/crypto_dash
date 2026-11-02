from payment_service import process_payment_in_usd


def test_process_payment_in_usd_with_mock(mocker):
    # Step 1: Mock the external API call so it returns a fixed rate (e.g., 1.10)
    mocker.patch("payment_service.get_usd_exchange_rate", return_value=1.10)

    # Step 2: Execute the function under test
    result = process_payment_in_usd(100.0)

    # Step 3: Assert the business logic calculation works deterministically
    assert result == 110.0
