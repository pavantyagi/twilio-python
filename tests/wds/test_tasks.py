import unittest

from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.wds.tasks import Tasks, Task


AUTH = ("AC123", "token")
BASE_URI = "https://wds.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
TASK_SID = "WTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class TaskTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_create(self, request):
        resp = create_mock_json('tests/resources/wds/tasks_instance.json')
        resp.status_code = 201
        request.return_value = resp

        tasks = Tasks(BASE_URI, AUTH)
        tasks.create("attributes", "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        exp_params = {
            'Attributes': "attributes",
            'WorkflowSid': "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }

        request.assert_called_with("POST", "{}/Tasks".format(BASE_URI), data=exp_params, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_instance(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{}/Tasks/{}".format(BASE_URI, TASK_SID)
        list_resource = Tasks(BASE_URI, AUTH)
        task = Task(list_resource, TASK_SID)
        task.delete()
        request.assert_called_with("DELETE", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_delete_list(self, request):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        request.return_value = resp

        uri = "{}/Tasks/{}".format(BASE_URI, TASK_SID)
        list_resource = Tasks(BASE_URI, AUTH)
        list_resource.delete(TASK_SID)
        request.assert_called_with("DELETE", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/wds/tasks_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/Tasks/{}".format(BASE_URI, TASK_SID)
        list_resource = Tasks(BASE_URI, AUTH)
        list_resource.get(TASK_SID)
        request.assert_called_with("GET", uri, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/wds/tasks_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/Tasks".format(BASE_URI)
        list_resource = Tasks(BASE_URI, AUTH)
        list_resource.list()
        request.assert_called_with("GET", uri, params={}, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_instance(self, request):
        resp = create_mock_json('tests/resources/wds/tasks_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{}/Tasks/{}".format(BASE_URI, TASK_SID)
        list_resource = Tasks(BASE_URI, AUTH)
        workflow = Task(list_resource, TASK_SID)
        workflow.update(attributes='attributes', workflow_sid='WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        exp_params = {
            'Attributes': "attributes",
            'WorkflowSid': "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_update_list(self, request):
        resp = create_mock_json('tests/resources/wds/tasks_instance.json')
        resp.status_code = 201
        request.return_value = resp

        uri = "{}/Tasks/{}".format(BASE_URI, TASK_SID)
        list_resource = Tasks(BASE_URI, AUTH)
        list_resource.update(TASK_SID, attributes='attributes', workflow_sid='WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        exp_params = {
            'Attributes': "attributes",
            'WorkflowSid': "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }

        request.assert_called_with("POST", uri, data=exp_params, auth=AUTH)
