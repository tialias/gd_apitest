# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/text_whitelist.har

import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, Parameters


class TestCaseTextWhitelist(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "desc-form_token-form_data-response_code_path-response_message_path-assert_code-assert_message": "${read_yaml(text_whitelist_test)}",
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("$desc").verify(False)

    teststeps = [
        Step(
            RunRequest("/f/$form_token")
            .get("${ENV(BASE_URL)}/f/$form_token")
            .with_headers(
                **{
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "if-none-match": 'W/"8812571a97da2a7309439d1008f56920"',
                }
            )
            .with_cookies(
                **{
                    "jsj_uid": "d451b406-246d-4051-93e4-3198fced0991",
                    "start_filling_time_$form_token": "1605600585",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1605600586",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1605600586",
                    "_ga": "GA1.2.83749953.1605600586",
                    "_gid": "GA1.2.508759516.1605600586",
                    "csrf_token": "N44f+HTg++RpexYnPSzeNP7aoDp/sk6ClyCvypHavvvmNGQZXdRS81qtUtm5E+az5TdvLHltA4ASFa66ymGF+A==",
                    "_gd_session": "b1Rpc2dnQkwyYlZydlE1SlJsNFhrZXJhYzd3dlF6OC85VzVDZ0I0SGRwcTQxTHNDQ2M2ZGtwUFZPYmZmNlEzaWh5VGk0WW5IQTVkWkpMK1NjYnVZcUh0MDhBQUNWRC9paVhxekorZUZoSXZQaFRxS1MrVjNHeTJwOVR3UHpMbHk0amRvZzhoaGxnVkJtT3RRUmJRMit3PT0tLVJVYnpBUUxmcWJONE1ybUpRbGE2VlE9PQ%3D%3D--2342d49fbd0899cdf04995dcc5f4a86536559442",
                    "filled_form_scene": "form",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/graphql/f/$form_token")
            .post("${ENV(BASE_URL)}/graphql/f/$form_token")
            .with_headers(
                **{
                    "content-length": "464",
                    "accept": "*/*",
                    "x-csrf-token": "GGjMRbPEbsqjuWeiOY+JqqLRXCH/mgl1fgimM6+FjObJ0rekmvDH3ZBvI1y9sLEtuTyTN/lFRHf7PadD9D635Q==",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "${ENV(BASE_URL)}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "${ENV(BASE_URL)}/f/$form_token",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "jsj_uid": "d451b406-246d-4051-93e4-3198fced0991",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1605600586",
                    "_ga": "GA1.2.83749953.1605600586",
                    "_gid": "GA1.2.508759516.1605600586",
                    "filled_form_scene": "form",
                    "start_filling_time_$form_token": "1605600695",
                    "csrf_token": "GGjMRbPEbsqjuWeiOY+JqqLRXCH/mgl1fgimM6+FjObJ0rekmvDH3ZBvI1y9sLEtuTyTN/lFRHf7PadD9D635Q==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1605600696",
                    "_gat_gtag_UA_48208031_13": "1",
                    "_gd_session": "TkdMZEs1T1ducmNVaW14Z3ltTkhDU3R5cFF3QmJEMVpmMmlGb0lKa21qcU03NEI2VGk5OVBDOEY3SmJraXZ4amwxaldPUnFkVWNoeGNHQUJ1QnhxUDV4Tmk1TUVsekR2QmZobjZQY25DWENpY1hySEhwczBFdHJiMzkzT3JOMko4alB1aVBjWWk3ZVd2L0JQMzJ5eFVBPT0tLTZoUkFHUVZGM1hCS1RoNnZsTDdra2c9PQ%3D%3D--1ea941bad6cb08179ec588152505b3d80d502f39",
                }
            )
            .with_json(
                {
                    "operationName": "CreatePublishedFormEntry",
                    "variables": {
                        "input": {
                            "formId": "$form_token",
                            "entryAttributes": "$form_data",
                            "captchaData": None,
                            "weixinAccessToken": None,
                            "xFieldWeixinOpenid": None,
                            "weixinInfo": None,
                            "prefilledParams": "",
                            "embedded": False,
                            "backgroundImage": False,
                            "formMargin": False,
                            "hasPreferential": False,
                            "fillingDuration": 8,
                        }
                    },
                    "extensions": {
                        "persistedQuery": {
                            "version": 1,
                            "sha256Hash": "4cd6a9aef2820b2c3215f6ddfa87093869461f76f3f2016738f4307268a7df98",
                        }
                    },
                }
            )
            .validate()
            .assert_equal("$response_code_path", "$assert_code")
            .assert_equal("$response_message_path", "$assert_message")
        ),
        Step(
            RunRequest("/f/$form_token/success")
            .get("${ENV(BASE_URL)}/f/$form_token/success")
            .with_params(
                **{
                    "e_token": "eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjpbIktOcjdXaTV1IiwiNWY5ZmMwNjM1YjY1MTY0NTUwNzA3M2RmIl0sImV4cCI6MTYwNTY4NzEwNX0.xMfHrpV9evn0VMaB-BntWcPr6LbgVOYxtok6zbpfDhk"
                }
            )
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "${ENV(BASE_URL)}/f/$form_token",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "entry_token": "KNr7Wi5u",
                    "gd_ssf": "MTYwNTYwMDcwNQ%3D%3D--d27bd8bf0e53c4728da30b6e20c1e65f964bba40",
                    "formSubmitSuccess": "1",
                    "jsj_uid": "d451b406-246d-4051-93e4-3198fced0991",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1605600586",
                    "_ga": "GA1.2.83749953.1605600586",
                    "_gid": "GA1.2.508759516.1605600586",
                    "filled_form_scene": "form",
                    "csrf_token": "GGjMRbPEbsqjuWeiOY+JqqLRXCH/mgl1fgimM6+FjObJ0rekmvDH3ZBvI1y9sLEtuTyTN/lFRHf7PadD9D635Q==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1605600696",
                    "_gat_gtag_UA_48208031_13": "1",
                    "last_fill_entry_token": "KNr7Wi5u",
                    "_gd_session": "V2g5Ym0yRC9iYk4ycU9lTzY4cDZ3S2pVa1N2bThhbGUzOHlSMm4wRitEbkEzUUowdi90QU9hNU4zRnpuSTlBR3gwWnRnbG1GZVZUUXVFZFV1bTF6MkZEeUUzb1kwUjRZdkNYVnhaZW1kaktqNDRZT0gxankxSFpoYkV3R05QaTlrOUJMa2pEOGRVeXFxOGM4T1ZudkJ3PT0tLXp5QUpaUFNDWUNWNVhGRTFiVkxNUHc9PQ%3D%3D--45d90559e90fbece48d5fbcc1251e214238484c1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseTextWhitelist().test_start()
