## WEEK02 시험
WEEK02의 시험 결과를 제출하는 곳입니다.

### 시험 수행 요령
- 풀어야 할 문제가 Slack에 공지됩니다.
- 백준 사이트에서 해당 문제를 각자 풉니다. (팀별이 아닌 개인별)
- 먼저 풀었더라도 시험 종료 시점까지는 제출하지 않도록 합니다.
  - 신속히 제출할 수 있도록 준비를 해 두면 좋음
- 통과하지 못한 코드도 제출할 수 있습니다.
  - 이 경우 Pull Request 설명란에 풀지 못했다고 적어두면 reviewer가 이해하기 좋습니다.

### 결과 코드 제출 요령
- **제출 시 `main` branch를 직접 update하지 않도록 주의합니다.**
  - `main` branch에서 commit 하면 안됩니다.
  - `week02/{제출자ID}` 형태의 branch를 만들어서 작업합니다.
  - review가 완료되기 전까지 main에 merge하지 않습니다.
  - 자신의 노트북에서 command line interface를 사용하여 제출하는 경우
    `git switch main && git pull`을 수행하여
    local repository를 **최신 상태로 만든 후에 branch를 만듭니다.**

- 답안 파일은 `Week02/{제출자ID}/{문제번호}.py` 형태로 작성합니다.
- 답안을 모두 만들었다면 위에서 만든 branch를 main으로 PR(pull request)를 보냅니다.
  - pull request를 만들 때 제목에 자신의 이름을 포함해 주십시오. reviewer가 찾기 쉽습니다.
  - pull request를 만든 후 [Merge pull request] 버튼을 **누르지 않도록** 합니다.

### 코드 리뷰 요령
- reviewer는 review 할 사람을 Pull request 탭에서 찾아서 code review를 합니다.
- reviewer는 답안 파일이 `Week02/{제출자ID}/{문제번호}.py`의 규칙을 지키는지 확인하고 지키지 않는다면 수정을 요청합니다.
  - 이 규칙이 지켜지지 않은채 merge 되면 파일이 제대로 정리되지 않은 상태가 됩니다.
- reviewer는 PR 작성자의 코드를 보고 자신의 의견을 GitHub PR도구를 사용하여 작성합니다.
  - 코드 작성자는 comment를 통해 토론할 수 있습니다.
- (선택) 토론 결과에 따라 코드를 수정하거나 추가합니다.
- 모든 조건이 만족하면 [Merge pull request] 버튼을 눌러 PR 결과물을 merge합니다. (되도록 시험 당일 24시까지)
- merge 후 앞에서 만들었던 `week02/{제출자ID}` branch를 제거(delete)하여 정리 합니다.
