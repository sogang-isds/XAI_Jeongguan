import os
import unittest
from shutil import rmtree

from celery import Celery

from config import MQ_CELERY_BROKER_URL, MQ_CELERY_BACKEND_URL, CELERY_TASK_NAME, APP_ROOT, DEFAULT_CALLBACK_URL


class TestCelery(unittest.TestCase):
    def setUp(self):
        self.app = Celery(CELERY_TASK_NAME, broker=MQ_CELERY_BROKER_URL, backend=MQ_CELERY_BACKEND_URL)

    def test_generate_answer(self):
        uid = 'test'
        idx = 0
        callback_url = DEFAULT_CALLBACK_URL

        # create a directory for the uid
        uid_path = os.path.join(APP_ROOT, 'tmp', uid)
        rmtree(uid_path, ignore_errors=True)
        os.makedirs(uid_path)

        paragraphs = [
            '신고의 접수, 기타 주식에 관한 사무절차는 이사회 결의로 정하는 「주식사무규정」에 따른다.② 회사는 명의개서 등에 관한 일체의 업무를 명의개서대리인에게 위임할 수 있다. 이 경우 제1항의 주식사무처리절차는 명의개서대리인의 「유가증권의 명의개서대행 등에 관한 규정」에 따른다.제13조(주주 등의 성명, 주소 및 인감 또는 서명의 신고) ① 주주 또는 등록질권자 및 그들의 법정대리인은 성명, 주소 및 인감 또는 서명을 회사에 신고하여야 하며 그 변경이 있을 때도 또한 같다.② 주주 또는 등록질권자가 외국에 거주할 때는 한국 내에 가주소 또는 대리인을 정하여 회사에 신고하여야 하고, 그 변경이 있을 때도 또한 같다.③ 법정대리인은 그 대리권을 증명할 서면을 제출하여야 하며 변경신고를 할 때에는 회사가 인정하는 증명서를 첨부하여야 한다.④ 회사가 명의개서대리인을 지정한 경우에는 제1항 내지 제3항에 불구하고 명의개서대리인에게 신고하여야 한다.⑤ 제1항 내지 제4항의 신 고를 태만함으로 인하여 생긴 손해에 대하여는 회사가 책임을 지지 아니한다.제14조(주주명부의 폐쇄) ① 회사는 결산기가 끝나는 다음 날로부터 그 결산에 관한 정기주주총회 종료일까지 권리에 관한 주주명부의 기재변경을 정지한다.② 회사는 임시주주총회의 소집 기타 필요한 경우 이사회의 결의로 3월을 경과하지 아니하는 일정한 기간을 정하여 권리에 관한 주주명부의 기재변경을 정지하거나 이사회의 결의로 정한 날에 주주명부에 기재되어 있는 주주를 그 권리를 행사할 주주로 할 수 있으며, 이사회가 필요하다고 인정하는 경우에는 주주명부의 기재변경 정지와 기준일의 지정을 함께 할 수 있다. 회사는 이를 2주간 전에 공고하여야 한다. 다만, 주주 전원의 동의가 있을 시에는 상기 공고절차를 생략할 수 있다.③ 회사는 매 결산기 최종일의 주주명부에 기재되어 있는 주주를 그 결산기에 관한 정기주주총회에서 권리를 행사할 주주로 한다.',
            '주주총회제19조(총회의 소집) ① 정기주주총회는 매 결산기가 끝난 후 3월 내에 소집하고 임시주주총회는 필요에 따라 이사회 결의 또는 법령에 정한 바에 의하여 수시 이를 소집한다.② 주주총회를 소집함에는 그 일시, 장소 및 회의의 목적사항을 총회일의 2주간 전에 각 주주에게 서면 또는 전자문서로 통지를 발송하여야 한다. 다만, 그 통지가 주주명부상의 주주의 주소에 계속 3년간 도달하지 아니한 때에는 해당 주주에게 주주총회의 소집을 통지하지 아니할 수 있다.③ 제2항 본문에도 불구하고 주주 전원의 동의가 있는 경우에는 통지 기간을 단축하거나 통지 절차를 생략할 수 있다.④ 주주총회는 미리 주주에게 통지한 회의의 목적사항 이외에는 결의하지 못한다. 다만, 주주 전원의 동의가 있는 경우에는 그러하지 아니하다.제20조(총회의 의장) 주주총회의 의장은 대표이사 사장으로 한다. 다만, 대표이사 사장의 유고 시에는 제31조 제5항의 규정을 준용한다.제21조(의장의 질서유지권) ① 주주총회의 의장은 고의로 의사진행을 방해하기 위한 발언·행동을 하는 등 현저히 질서를 문란하게 하는 자에 대하여 그 발언의 정지 또는 퇴장을 명할 수 있다.② 주주총회의 의장은 의사진행의 원활을 기하기 위하여 필요하다고 인정할 때에는 주주의 발언의 시간 및 회수를 제한할 수 있다.제22조(총회의 결의) 총회의 결의는 법령에 따로 규정이 있는 것을 제외하고는 출석한 주주의 의결권의 과반수와 발행주식총수의 4분의 1 이상의 수로써 하여야 한다.제23조(의결권의 대리행사) 주주는 대리인으로 하여금 의결권을 행사하게 할 수 있다. 다만, 대리인은 주주총회 전에 그 대리권을 증명하는 서면을 제출하여야 한다.제24조(총회의사록) 주주총회의 의사에 대하여는 그 경과의 요령 및 결과를 의사록에 기재하고 의장과 출석한 이사가 기명날인 또는 서명하여 본점 및 지점에 비치하여야 한다.',
            '계 산제43조 (사업연도) 회사의 사업연도는 매년 1월 1일부터 12월 31일까지로 한다.제44조 (재무제표등) ① 대표이사는 정기주주총회 회일 6주간 전에 다음 각 호의 서류와 그 부속명세서 및 영업보고서를 작성하여 감사위원회의 감사를 받아 정기주주총회에 제출하여야 한다.1. 대차대조표(주식회사의 외부감사에 관한 법률 제1조의2에서 규정하는 재무상태표)2. 손익계산서3. 그 밖에 회사의 재무상태와 경영성과를 표시하는 것으로서 「상법」시행령에서 정하는서류4. 「상법」시행령에서 정하는바에 따른 제1호 내지 제3호의 서류에 대한 연결재무제표② 감사위원회는 제1항의 서류를 받은 날로부터 4주간 내에 감사보고서를 대표이사에게 제출하여야 한다.③ 제1항에 불구하고 회사는 다음 각호의 요건을 모두 충족한 경우에는 이사회의 결의로 이를 승인할 수 있다.1. 제1항의 각 서류가 법령 및 정관에 따라 회사의 재무상태 및 경영성과를 적정하게 표시하고 있다는 외부감사인의 의견이 있을 때2. 감사위원회 위원 전원의 동의가 있을 때④ 제3항에 따라 이사회가 승인한 경우에는 대표이사는 제1항의 각 서류의 내용을 주주총 회에 보고하여야 한다.⑤ 회사는 제1항 각호의 서류를 영업보고서 및 감사보고서와 함께 정기주주총회 회일의 1주간 전부터 본점에 5년간, 그 등본을 지점에 3년간 비치하여야 한다.⑥ 회사는 제1항 각 호의 서류에 대한 정기주주총회의 승인 또는 제3항에 의한 이사회의 승인을 얻은 때에는 지체 없이 대차대조표를 공고하여야 한다.제45조(외부감사인의 선임) 회사는 감사위원회의 승인을 얻어 외부감사인을 선임하며, 선임 후 최초로 소집되는 정기주주총회에 그 사실을 보고하거나, 최근 주주명부 폐쇄일의 주주에게 서면이나 전자문서에 의한 통지 또는 회사의 인터넷 홈페이지에 공고한다.제46조(손익계산과 처분) 회사의 손익계산은 매결산기의 총수익으로부터 총비용을 공제한 나머지를 순이익금으로 하고 이에 전기이월이익잉여금을 합하여 다음 각 호의 방법에 따라 처분한다.1. 이익준비금 : 금전에 의한 이익배당액의 10분의 1 이상2. 기타의 법정적립금3. 배당금4. 임의적립금5. 기타의 이익잉여금처분액6. 차기이월이익잉여금제47조(이익배당) ① 이익의 배당은 금전과 주식 및 기타의 재산으로 할 수 있다. 다만, 주식에 의한 배당은 이익배당 총액의 2분의 1에 상당하는 금액을 초과하지 못한다.② 이익의 배당을 주식으로 하는 경우 회사가 종류주식을']

        question = '정기주주총회를 개최하는가?'

        task_name = f'{CELERY_TASK_NAME}.llm_answer'
        result = self.app.send_task(task_name, args=[uid, idx, paragraphs, question, callback_url], queue=CELERY_TASK_NAME,
                                    expires=(60 * 60 * 24))
        print(result.id)
        output = result.get()

        self.assertNotEqual(output, False)

    def test_generate_advice(self):
        uid = 'test'
        idx = 0
        callback_url = DEFAULT_CALLBACK_URL

        # create a directory for the uid
        uid_path = os.path.join(APP_ROOT, 'tmp', uid)
        rmtree(uid_path, ignore_errors=True)
        os.makedirs(uid_path)

        question = '정기주주총회를 개최하는가?'
        answer = '예, 정기주주총회는 매 결산기가 끝난 후 3월 내에 소집됩니다.'
        sangbub = """제365조(총회의 소집)
①정기총회는 매년 1회 일정한 시기에 이를 소집하여야 한다.
②연 2회 이상의 결산기를 정한 회사는 매기에 총회를 소집하여야 한다.
③임시총회는 필요있는 경우에 수시 이를 소집한다.

제542조의4(주주총회 소집공고 등)
① 상장회사가 주주총회를 소집하는 경우 대통령령으로 정하는 수 이하의 주식을 소유하는 주주에게는 정관으로 정하는 바에 따라 주주총회일의 2주 전에 주주총회를 소집하는 뜻과 회의의 목적사항을 둘 이상의 일간신문에 각각 2회 이상 공고하거나 대통령령으로 정하는 바에 따라 전자적 방법으로 공고함으로써 제363조제1항의 소집통지를 갈음할 수 있다.
② 상장회사가 이사ㆍ감사의 선임에 관한 사항을 목적으로 하는 주주총회를 소집통지 또는 공고하는 경우에는 이사ㆍ감사 후보자의 성명, 약력, 추천인, 그 밖에 대통령령으로 정하는 후보자에 관한 사항을 통지하거나 공고하여야 한다.
③ 상장회사가 주주총회 소집의 통지 또는 공고를 하는 경우에는 사외이사 등의 활동내역과 보수에 관한 사항, 사업개요 등 대통령령으로 정하는 사항을 통지 또는 공고하여야 한다. 다만, 상장회사가 그 사항을 대통령령으로 정하는 방법으로 일반인이 열람할 수 있도록 하는 경우에는 그러하지 아니하다.

제388조(이사의 보수)
이사의 보수는 정관에 그 액을 정하지 아니한 때에는 주주총회의 결의로 이를 정한다.
"""

        task_name = f'{CELERY_TASK_NAME}.llm_advice'
        result = self.app.send_task(task_name, args=[answer, uid, idx, question, sangbub, callback_url], queue=CELERY_TASK_NAME,
                                    expires=(60 * 60 * 24))

        print(result.id)
        output = result.get()

        self.assertNotEqual(output, False)

    def tearDown(self):
        pass
