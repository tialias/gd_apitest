# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/normal_submit.har
import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters


class TestCaseNormalSubmit(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "desc-form_token-form_data-response_code_path-response_message_path-assert_code-assert_message": "${read_yaml(text_normal_submit_test)}",
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("$desc").verify(False)

    teststeps = [
        Step(
            RunRequest("打开表单")
            .get("${ENV(BASE_URL)}/f/$form_token")
            .with_headers(
                **{
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "${ENV(BASE_URL)}/f/$form_token",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_cookies(
                **{
                    "entry_token": "22QXNuno",
                    "gd_ssf": "MTYwMzcwNTcxNg%3D%3D--64adbf3dd471a46788cb64107bf79dd727a1def2",
                    "_ga": "GA1.2.669479930.1597286832",
                    "_smt_uid": "5f4c6fcb.35bf55f7",
                    "change_theme_btn_clicked_midautumn": "1579600505",
                    "jsj_locale": "zh-CN",
                    "_gd_sid_usd": "IjVmNzNlNjUzZTVjZGM0MjlkZDRiN2RmNyI%3D--e94c00da46872bc61395523f6815fb36551bc6be",
                    "_gd_sid_mo": "IjVmOGZlMGIxNWI2NTE2NjZkOGI0ZTQ4YyI%3D--8228f70e23423567053db53f1b2e443dbee61cf7",
                    "_jinshuju_ut": "IjVjOGI2YTBkOTYwMjY4N2U0OGI4Zjg4YSI%3D--3d0d333baebbb142e894251a445237f0e74cb611",
                    "jsj_uid": "ec5ce3b2-5149-4620-b475-e2a633d5dccf",
                    "_gd_sid_fusion": "IjVmOTBlODU2MGJjMmIzNjI2ZTE0ZGZiYSI%3D--dcfd5b67261ee167eca04cea0aeabbfe075b7f61",
                    "_gd_sid_staging": "IjVmOTE0MTY4NmVjNWQ5NTAxZDI1OTJiNCI%3D--10e12a95c567454d8c89a8c774bb36d3e3fc25a0",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1602214492,1602224981,1602225263,1603435846",
                    "country_code": "CN",
                    "filled_form_scene": "form",
                    "_gd_sid_uat": "IjVmOTJhOTdjZDQ5NmNlMzU4NDc4NjY0MiI%3D--0259d10c97406fcd717636d370ea8c2a1c050843",
                    "_gid": "GA1.2.1051440085.1603676790",
                    "has_visited_dashboard_in_two_days": "true",
                    "_gd_sid": "IjVmOTY5MzBkZGUxZDBkZDQ3ZDRjNWM3NyI%3D--161a2f947d29a2fe1af6f33233e436d694461f43",
                    "_caid": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3NCI%3D--d141bd1f24ec3955b11ea186700716f2a6e71db6",
                    "mixpanel_event_history": "form_updated",
                    "last_fill_entry_token": "22QXNuno",
                    "start_filling_time_$form_token": "1603705773",
                    "csrf_token": "tEhH5ma7oLqw5JRt6QBlAqCiM0aQQeN44nXUSpvHIS1aTOsDbckkbAhdI27niVaAogNpmKWTBYPlMZXgtTjJmA==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603705775",
                    "_gd_session": "YWI0aCtEa3U2aG9ocWRReHR6RmFIcUE5cFlucE9XdTBPWGxjcGI5Z05hLy9Bd0tkdmpBWjVPcU9VSEN6M3dXUm02cDUyV3FGanFFM3FTZGJhY1ROWm93cDdLY2lFeHFDVG15bDh3QzBCUEFidkZvQXFiTjAyVWx2ZktEcmpqYlJ6R1lTczNlUXBkNHZoRkhtQ1REZjZRPT0tLUwxT0EwbE1NZnk3cFMvSG1rNWtzdFE9PQ%3D%3D--2400ec31c69ecde61968e2153e52738476655b88",
                }
            )
            .extract()
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("提交数据")
            .post("${ENV(BASE_URL)}/graphql/f/$form_token")
            .with_headers(
                **{
                    "content-length": "464",
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "accept": "*/*",
                    "x-gd-ssf": "MTYwMzcwNTcxNg==--64adbf3dd471a46788cb64107bf79dd727a1def2",
                    "x-csrf-token": "9hmfWFLktYZ8bc8n+Wa9kxxN3lGHEuzhh3ELQ06nOpcYHTO9WZYxUMTUeCT3744RHuyEj7LAChqANUrpYFjSIg==",
                    "x-entry-token": "22QXNuno",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "${ENV(BASE_URL)}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "${ENV(BASE_URL)}/f/$form_token",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_cookies(
                **{
                    "_ga": "GA1.2.669479930.1597286832",
                    "_smt_uid": "5f4c6fcb.35bf55f7",
                    "change_theme_btn_clicked_midautumn": "1579600505",
                    "jsj_locale": "zh-CN",
                    "_gd_sid_usd": "IjVmNzNlNjUzZTVjZGM0MjlkZDRiN2RmNyI%3D--e94c00da46872bc61395523f6815fb36551bc6be",
                    "_gd_sid_mo": "IjVmOGZlMGIxNWI2NTE2NjZkOGI0ZTQ4YyI%3D--8228f70e23423567053db53f1b2e443dbee61cf7",
                    "_jinshuju_ut": "IjVjOGI2YTBkOTYwMjY4N2U0OGI4Zjg4YSI%3D--3d0d333baebbb142e894251a445237f0e74cb611",
                    "jsj_uid": "ec5ce3b2-5149-4620-b475-e2a633d5dccf",
                    "_gd_sid_fusion": "IjVmOTBlODU2MGJjMmIzNjI2ZTE0ZGZiYSI%3D--dcfd5b67261ee167eca04cea0aeabbfe075b7f61",
                    "_gd_sid_staging": "IjVmOTE0MTY4NmVjNWQ5NTAxZDI1OTJiNCI%3D--10e12a95c567454d8c89a8c774bb36d3e3fc25a0",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1602214492,1602224981,1602225263,1603435846",
                    "country_code": "CN",
                    "filled_form_scene": "form",
                    "_gd_sid_uat": "IjVmOTJhOTdjZDQ5NmNlMzU4NDc4NjY0MiI%3D--0259d10c97406fcd717636d370ea8c2a1c050843",
                    "_gid": "GA1.2.1051440085.1603676790",
                    "has_visited_dashboard_in_two_days": "true",
                    "_gd_sid": "IjVmOTY5MzBkZGUxZDBkZDQ3ZDRjNWM3NyI%3D--161a2f947d29a2fe1af6f33233e436d694461f43",
                    "_caid": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3NCI%3D--d141bd1f24ec3955b11ea186700716f2a6e71db6",
                    "mixpanel_event_history": "form_updated",
                    "last_fill_entry_token": "22QXNuno",
                    "start_filling_time_$form_token": "1603705891",
                    "csrf_token": "9hmfWFLktYZ8bc8n+Wa9kxxN3lGHEuzhh3ELQ06nOpcYHTO9WZYxUMTUeCT3744RHuyEj7LAChqANUrpYFjSIg==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603705893",
                    "_gat_gtag_UA_48208031_13": "1",
                    "_gd_session": "MGwxamNkNU9NSkd2UkZTZEtKd1d0MmgrTy9PejVxL0RWMWM3TkNsSnNBR3NGWnhkeTljU0M5d3VqOHZ1TkdSSkk3ZzBTMWV4YXdBNDFwSFBXV0xiMFN2dEwweGNMYmpOcFRneGRZUFpQb3A4a1pieFBDRlFJUThnRnNwY3VzWGw0MTBwMyt6L1JwYkYxZkxpV0JSUmxRPT0tLWY4RDh2UXpLRXE4dXRuSnllMEprSmc9PQ%3D%3D--430c782dbfd2a67de3931a28d60ca0534ea6836f",
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
                            "fillingDuration": 5,
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
            .assert_equal("status_code", "$assert_code")
        ),
        Step(
            RunRequest("跳转到success")
            .get("${ENV(BASE_URL)}/f/$form_token/success")
            .with_headers(
                **{
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "${ENV(BASE_URL)}/f/$form_token",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_cookies(
                **{
                    "entry_token": "m7eYgiUO",
                    "gd_ssf": "MTYwMzcwNTg5OA%3D%3D--b99a57c5bc2f57b64a2c49d8fcbedce01cdcf723",
                    "formSubmitSuccess": "1",
                    "_ga": "GA1.2.669479930.1597286832",
                    "_smt_uid": "5f4c6fcb.35bf55f7",
                    "change_theme_btn_clicked_midautumn": "1579600505",
                    "jsj_locale": "zh-CN",
                    "_gd_sid_usd": "IjVmNzNlNjUzZTVjZGM0MjlkZDRiN2RmNyI%3D--e94c00da46872bc61395523f6815fb36551bc6be",
                    "_gd_sid_mo": "IjVmOGZlMGIxNWI2NTE2NjZkOGI0ZTQ4YyI%3D--8228f70e23423567053db53f1b2e443dbee61cf7",
                    "_jinshuju_ut": "IjVjOGI2YTBkOTYwMjY4N2U0OGI4Zjg4YSI%3D--3d0d333baebbb142e894251a445237f0e74cb611",
                    "jsj_uid": "ec5ce3b2-5149-4620-b475-e2a633d5dccf",
                    "_gd_sid_fusion": "IjVmOTBlODU2MGJjMmIzNjI2ZTE0ZGZiYSI%3D--dcfd5b67261ee167eca04cea0aeabbfe075b7f61",
                    "_gd_sid_staging": "IjVmOTE0MTY4NmVjNWQ5NTAxZDI1OTJiNCI%3D--10e12a95c567454d8c89a8c774bb36d3e3fc25a0",
                    "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1602214492,1602224981,1602225263,1603435846",
                    "country_code": "CN",
                    "filled_form_scene": "form",
                    "_gd_sid_uat": "IjVmOTJhOTdjZDQ5NmNlMzU4NDc4NjY0MiI%3D--0259d10c97406fcd717636d370ea8c2a1c050843",
                    "_gid": "GA1.2.1051440085.1603676790",
                    "has_visited_dashboard_in_two_days": "true",
                    "_gd_sid": "IjVmOTY5MzBkZGUxZDBkZDQ3ZDRjNWM3NyI%3D--161a2f947d29a2fe1af6f33233e436d694461f43",
                    "_caid": "IjVkZDYyNjU0NjZhYjMzNDZhNzI5MjA3NCI%3D--d141bd1f24ec3955b11ea186700716f2a6e71db6",
                    "mixpanel_event_history": "form_updated",
                    "csrf_token": "9hmfWFLktYZ8bc8n+Wa9kxxN3lGHEuzhh3ELQ06nOpcYHTO9WZYxUMTUeCT3744RHuyEj7LAChqANUrpYFjSIg==",
                    "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1603705893",
                    "_gat_gtag_UA_48208031_13": "1",
                    "last_fill_entry_token": "m7eYgiUO",
                    "_gd_session": "OTByL3BlbnJkVS9MblRkU0U4NFVPTW9PaWwvQlQ1cFlLdTZuYWgrUWV0Zmk5MUhTQStmRUVtNEE4UHp3cmdSOVJqMlVrY01ZMFBIaFhvL1oyMXpGQWtXOEgrSlpGNnhXSDcxS2x4OFRPcUE1Ynlsb3BycmRDdDUzQzg1S29ySnI5c2VNd3M0QUhiOXJFWE8rd0ZCMUhRPT0tLWR5N2N2NVBZNW5iWWxQM1Z6RXptS1E9PQ%3D%3D--b0f1d6296b8a00b8bb7bbefd08092ce62519c04e",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseNormalSubmit().test_start()
