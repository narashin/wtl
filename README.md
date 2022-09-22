# 실행
```sh
docker run --rm -p 8080:8000 wantedlab:0.1
```
또는 
```sh
pip install -r requirements.txt

uvicorn assignment.main:app --reload 
```

# API 명세
* 실행 후, `localhost:8080/docs` 를 통한 swagger 문서 참고
 
# 테이블 
* corp
  * id, name
  * 회사 정보 
* corp_name
  *  id, name, lang_code, corp_id
  * 회사명의 다국어 정보 
* corp_tag
  *  corp_id, tag_id
  * 회사와 태그 연결 
* tag
  * id, name
  * 태그 정보 
* tag_name
  * id, name, lang_code, tag_id
  * 태그명의 다국어 정보