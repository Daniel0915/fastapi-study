# fastapi-study

FastAPI 학습 저장소.

- 참고: [파이썬 타입 소개](https://fastapi.tiangolo.com/ko/python-types/)
- 참고: [AI 개발 환경 세팅](https://fastapi.tiangolo.com/ko/ai-development/)

## 실행

```bash
uv sync                # 의존성 설치 (.venv 생성, uv.lock 작성)
uv run fastapi dev     # 개발 서버: http://127.0.0.1:8000, 문서: /docs
```

엔트리포인트는 `pyproject.toml`의 `[tool.fastapi] entrypoint = "main:app"`.

## Claude Code용 FastAPI 스킬 설치

```bash
uvx library-skills install --skill fastapi --yes --claude
```
