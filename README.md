# DRILL 09 · 방향키 이동과 애니메이션

**Python과 pico2d로 입력 처리, 스프라이트 애니메이션, 화면 경계를 연습한 수업 과제입니다.**

주 실행 파일은 [boy_move.py](boy_move.py)입니다. 방향키 입력을 집합으로 관리하고, 경과 시간에 따라 이동과 애니메이션을 갱신합니다.

- 상하좌우·대각선 이동과 반대 방향 동시 입력 처리
- 이동·정지 상태에 따른 좌우 애니메이션 전환
- 캐릭터 전체가 화면 안에 머무는 경계 제한
- 창 포커스를 잃으면 누른 키 상태 초기화

## 실행과 조작

Python과 pico2d가 설치된 환경에서 실행합니다.

```shell
python boy_move.py
```

`boy_move.py` 옆에 `animation_sheet.png`와 `TUK_GROUND.png`가 필요합니다. 실행 코드는 소스 파일 위치를 기준으로 이미지를 찾습니다.

| 입력 | 동작 |
| --- | --- |
| 방향키 | 캐릭터 이동 |
| Esc / 창 닫기 | 종료 |

## 파일 안내

- [boy_move.py](boy_move.py): 이번 과제의 이동·애니메이션 구현
- [PRD.md](PRD.md): 과제 요구사항, 구현 과정과 기존 확인 기록
- `character_runs_esc.py`, `move_character_with_key.py`, `move_character_with_mouse.py`: 수업 실습 파일

수업 실습 파일과 과제 구현 파일을 구분해 보관합니다. 이번 문서 정리에서는 소스와 리소스 구성을 확인했으며, GUI 실행은 새로 검증하지 않았습니다.

[프로필의 다른 프로젝트](https://github.com/yoon778)
