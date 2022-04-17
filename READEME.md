# pip3 virtaulenv => 가상폴더만든후

# django amdin startprojdect [폴더명]

# python3 manage.py runserver

# python3 manage.py startapp [base]

# makemigrations => migrate 적용

# python3 manage.py createsuperuser 관리자 계정 생성

#

```
from .models import Room

admin.site.register(Room)
```

> 이런식으로 마이그레이션 한걸 적용시키면 관리자사이트에 추가 됨

# ForeignKey 는 ? 1:N 의미를 할수있다 n인 쪽에서 관ㄹ계를 선언해주며 두개의 인자가 필요로한다 .

> 하나는 대상이 되는 클래스 , 다른하나는 이슈에 대한 설정이다

- on_delete 설정은
  각각에 대한 설명은 1인쪽의 데이터가 삭제 되었을시 n,인쪽의 데이터를 어떻게 처리할 지에 대한 설정 이다 .
  > CASECADE : 이와 연결되어있는 모든 N쪽 데이터를 삭제
  > PROTECT : 1인 쪽의 데이터가 삭제가 되지 않도록 보호해줍니다.
  > SET_NULL : null 로 값을 대체하게 되어 필드에 null=True 옵션이 있어야만 가능합니다.
  > SET_DEFAULT : default 로 값을 대체하게 되어 필드에 default=True 옵션이 있어야만 가능합니다.
  > SET : 대체할 값이나 함수를 지정합니다
  > DO_NOTHING : 아무 것도 하지 않지만 db 에서 오류가 발생할 수 있습니다.

3
